import tkinter as tk
import tkinter.font as tkFont
import time
from WSdata import *
from tkinter.filedialog import askdirectory
from PIL import ImageGrab
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Wiki Solubility')
window.resizable(width = False, height = False)

prev = 0
curr = 0

ft1 = tkFont.Font(family='Arial', size=10)
ft2 = tkFont.Font(family='Arial', size=12, weight = tkFont.BOLD)
ft3 = tkFont.Font(family='Arial', size=9, weight = tkFont.BOLD)

frame = tk.Frame(bg = "#FFFFFF")
frame.grid(row = 0, column = 0)

var = tk.StringVar()
var.set('')

varpc = tk.StringVar()

ctrdrw = False

isdark = False

C = tk.Canvas(frame, bg = '#FFFFFF', width = 550, height = 550, highlightbackground = '#FFFFFF', highlightcolor = '#FFFFFF', bd = 1)
C.grid(row = 1, column = 6, rowspan = 3)

def draw(m):
	global isdark
	ifdec = False
	dectemp = 0
	ifmis = False
	mistemp = 0
	C.delete('all')
	max = 0
	min = 2000
	points = []
	for i in range(0, 101, 5):
		temp = str(i) + '°C'
		try:
			slb = sublist[m].solub[temp]
		except:
			continue
		try:
			points.append( [i, float(slb)] )
			if float(slb) > max:
				max = float(slb)
			if float(slb) < min:
				min = float(slb)
		except:
			if slb == 'N/A':
				continue
			elif slb.find('×10') != -1:#some data is in the form of num×10num
				slblist = slb.partition('×10')
				slbfloat = round(float(slblist[0]), 3) * (10 ** int(slblist[2]))
				points.append( [i, slbfloat] )
				if slbfloat > max:
					max = slbfloat
				if slbfloat < min:
					min = slbfloat
			elif slb.find('ml') != -1:#some data is in the form of num ml
				slblist = slb.partition('ml')
				slbfloat = round(float(slblist[0]),2)
				points.append( [i, slbfloat] )
				if slbfloat > max:
					max = slbfloat
				if slbfloat < min:
					min = slbfloat
			elif slb.endswith(')'):
				slblist = slb.replace('°C)', '').partition('(')
				slbtemp = int(slblist[2])
				slbfloat = float(slblist[0])
				points.append([slbtemp, slbfloat])
				if slbfloat > max:
					max = slbfloat
				if slbfloat < min:
					min = slbfloat
			elif slb == 'dec':
				ifdec = True
				dectemp = i
			elif slb == 'miscible':
				ifmis = True
				mistemp = i
			else:
				continue
	return [points, max, min, ifdec, dectemp, ifmis, mistemp, m]

def realdraw(imformlist: list, dotcolor: str, textcolor: str, linecolor: str):
	global ctrdrw, sublist
	points = imformlist[0]
	max = imformlist[1]
	min = imformlist[2]
	ifdec = imformlist[3]
	dectemp = imformlist[4]
	ifmis = imformlist[5]
	mistemp = imformlist[6]
	m = imformlist[7]
	lastx = int
	lasty = int
	for i in range(len(points)):
		#print(points[i])
		x = points[i][0] * 4.75 + 25
		if max != min:
			y = 445 - (points[i][1] - min) / (max - min) * 420
		else:
			y = 445 - points[i][1] / max * 420
		if i != 0:
			C.create_line(lastx, lasty, x, y, width = 3, tag = 'line', fill = linecolor)
		C.create_oval(x-3, y-3, x+3, y+3, fill = dotcolor, width = 0)
		C.create_text(x+20, y, text = str(points[i][0]) + '°C\n' + str(points[i][1]), fill = textcolor, font = ft3, tag = 'text')
		lastx = x
		lasty = y
	if ifdec:
		x = dectemp * 4.75 + 25
		y = 25
		C.create_oval(x-3, y-3, x+3, y+3, fill = '#FF0000', width = 0)
		C.create_text(x+5, y, text = sublist[m].formula +'\nDecomposes\nAt ' + str(dectemp) + '°C', fill = '#FF0000', font = ft3, tag = 'text', anchor = 'w')
	if ifmis:
		x = mistemp * 4.75 + 25
		y = 25
		C.create_oval(x-3, y-3, x+3, y+3, fill = '#0000FF', width = 0)
		C.create_text(x+5, y, text = sublist[m].formula + '\nMiscibles\n At ' + str(mistemp) + '°C', fill = '#0000FF', font = ft3, tag = 'text', anchor = 'w')
	C.lift('text')
	C.lower('line')
	window.update()

def cvstitle(m1, m2):
	if m2 == -1:
		if isdark:
			C.create_text(275, 530, text = 'Solubility Fold Line Diagram of\n%s (%s)' % ((sublist[m1].name), sublist[m1].formula), font = ft2, fill = '#FFFFFF')
		else:
			C.create_text(275, 530, text = 'Solubility Fold Line Diagram of\n%s (%s)' % ((sublist[m1].name), sublist[m1].formula), font = ft2, fill = '#0F102E')
	else:
		if isdark:
			C.create_text(275, 510, text = 'Solubility Comparison Fold Line Diagram of\n%s (%s) and\n%s (%s)' % ((sublist[m1].name), sublist[m1].formula, (sublist[m2].name), sublist[m2].formula), font = ft2, fill = '#FFFFFF')
		else:
			C.create_text(275, 510, text = 'Solubility Comparison Fold Line Diagram of\n%s (%s) and\n%s (%s)' % ((sublist[m1].name), sublist[m1].formula, (sublist[m2].name), sublist[m2].formula), font = ft2, fill = '#0F102E')
	window.update()

prevcpr = False

def normdraw(m):
	global prevcpr, isdark
	lista = draw(m)
	if isdark:
		realdraw(lista, '#FFFFEE', '#00FFEE', '#FF6699')
	else:
		realdraw(lista, '#332255', '#40709F', '#284E6F')
	m1 = lista[7]
	cvstitle(m1, -1)
	prevcpr = False

def contradraw(m1, m2):
	list1 = draw(m1)
	list2 = draw(m2)
	if list1[1] > list2[1]:
		list2[1] = list1[1]
	else:
		list1[1] = list2[1]
	if list1[2] < list2[2]:
		list2[2] = list1[2]
	else:
		list1[2] = list2[2]
	cvstitle(m1, m2)
	if isdark:
		realdraw(list1, '#FFFFEE', '#EE00FF', '#FF6699')
		realdraw(list2, '#FFFFEE', '#00FFEE', '#9966FF')
		C.create_text(275, 477, text = sublist[m1].formula, fill = '#FF6699', font = ft3)
		C.create_text(275, 465, text = sublist[m2].formula, fill = '#9966FF', font = ft3)
	else:
		realdraw(list1, '#332255', '#40709F', '#284E68')
		realdraw(list2, '#332255', '#9F7040', '#897983')
		C.create_text(275, 477, text = sublist[m1].formula, fill = '#284E68', font = ft3)
		C.create_text(275, 465, text = sublist[m2].formula, fill = '#897983', font = ft3)
	T.delete(0.0, 'end')
	T.insert('end', '%s\n\n%s' % (sublist[prev].getInform(),sublist[curr].getInform()))

def search(ev = None):
	global curr, prev
	T.delete(0.0, 'end')
	key = str(E.get())
	keylist = key.split()
	allsubdict = {}
	match = -1
	if key == '':
		return
	for i in range(0, len(keylist)):
		if keylist[i].casefold() == 'ferric':
			keylist[i] = 'iron(iii)'
		if keylist[i].casefold() == 'ferrous':
			keylist[i] = 'iron(ii)'
		if keylist[i].casefold() == 'cupric':
			keylist[i] = 'copper(ii)'
		if keylist[i].casefold() == 'cuprous':
			keylist[i] = 'copper(i)'
		if keylist[i].casefold() == 'aluminum':
			keylist[i] = 'aluminium'
		if keylist[i].casefold() == 'dichloride':
			keylist[i] = '(ii) chloride'
		if keylist[i].casefold() == 'trichloride':
			keylist[i] = '(iii) chloride'
	for i in range(0, 665):
		allnamesub = True
		allformulasub = True
		for j in range(0, len(keylist)):#check if all substring is contained in formula or name
			if (str(sublist[i].name).casefold().find(keylist[j].casefold()) == -1):
				allnamesub = False
			if (str(sublist[i].formula).casefold().find(keylist[j].casefold()) == -1):
				allformulasub = False
		if allnamesub or allformulasub:
			if (str(sublist[i].name).casefold() == key.casefold()) or (str(sublist[i].formula).casefold() == key.casefold()):
				prev = curr
				curr = i
				varpc.set('Previous: %s\nCurrent:%s' %(sublist[prev].formula, sublist[curr].formula))
				T.insert('end', sublist[i].getInform())#check if it is exactly the same substance
				normdraw(i)
				return
			else:
				allsubdict[sublist[i].name] = sublist[i].formula#add to possble list
				match = i
	if len(allsubdict) == 1:#only one possible
		prev = curr
		curr = match
		varpc.set('Previous: %s\nCurrent:%s' %(sublist[prev].formula, sublist[curr].formula))
		T.insert('end', 'No exact matching substance. Closest result:\n%s' % sublist[match].getInform())
		normdraw(match)
		return
	elif len(allsubdict) != 0:#multiple possibilities
		if len(allsubdict) > 50:
			T.insert('end', 'Too many possible results(%d in total). Try again with something more precise.' % len(allsubdict))
			return
		else:
			T.insert('end', 'Multiple results found. Please determine which you\'are looking for and then search again.\n%s' % str(allsubdict))
			return
		return
	else:#nothing matches
		T.insert('end', 'No result found. Please try again.')
		return

def compare():
	global prev, curr, prevcpr
	contradraw(prev, curr)
	prevcpr = True

def backgr():
	global isdark, prev, curr, prevcpr
	if isdark:
		isdark = False
		frame['bg'] = '#CDD7E2'
		C['bg'] = '#CDD7E2'
		L['bg'] = '#CDD7E2'
		L['fg'] = '#0F102E'
		E['bg'] = '#CDD7E2'
		E['fg'] = '#0F102E'
		E['insertbackground'] = '#000000'
		T['bg'] = '#CDD7E2'
		T['fg'] = '#0F102E'
		T['insertbackground'] = '#000000'
		B['bg'] = '#CDD7E2'
		B['fg'] = '#0F102E'
		Bbg['bg'] = '#CDD7E2'
		Bbg['fg'] = '#0F102E'
		Linf['bg'] = '#CDD7E2'
		Linf['fg'] = '#0F102E'
		Bcp['bg'] = '#CDD7E2'
		Bcp['fg'] = '#0F102E'
		Bex['bg'] = '#CDD7E2'
		Bex['fg'] = '#0F102E'
		Lcpr['bg'] = '#CDD7E2'
		Lcpr['fg'] = '#0F102E'
	else:
		isdark = True
		frame['bg'] = '#000022'
		C['bg'] = '#000022'
		L['bg'] = '#000022'
		L['fg'] = '#FFFFFF'
		E['bg'] = '#000022'
		E['fg'] = '#FFFFFF'
		E['insertbackground'] = '#FFFFFF'
		T['bg'] = '#000022'
		T['fg'] = '#FFFFFF'
		T['insertbackground'] = '#FFFFFF'
		B['bg'] = '#000022'
		B['fg'] = '#FFFFFF'
		Bbg['bg'] = '#000022'
		Bbg['fg'] = '#FFFFFF'
		Bcp['bg'] = '#000022'
		Bcp['fg'] = '#FFFFFF'
		Bex['bg'] = '#000022'
		Bex['fg'] = '#FFFFFF'
		Linf['bg'] = '#000022'
		Linf['fg'] = '#FFFFFF'
		Lcpr['bg'] = '#000022'
		Lcpr['fg'] = '#FFFFFF'
	if prevcpr:
		compare()
	else:
		normdraw(curr)
	window.update()

def getter(widget, path):
	x=frame.winfo_rootx()+widget.winfo_x()
	y=frame.winfo_rooty()+widget.winfo_y()
	x1=x+widget.winfo_width()
	y1=y+widget.winfo_height()
	ImageGrab.grab().crop((x,y,x1,y1)).save(path)

def export():
	global prevcpr, prev, curr
	if prevcpr:
		pngpath = '%s/%s_%s_comparision.png' % (askdirectory(), sublist[prev].formula, sublist[curr].formula)
	else:
		pngpath = '%s/%s_chart.png' % (askdirectory(), sublist[curr].formula)
	window.wm_attributes('-topmost', 1)
	getter(C, pngpath)
	showinfo('Export Successful', 'Successfully exported to %s' % pngpath)
	return

L = tk.Label(frame, text = 'Enter substance name or formula:', font = ft2, bg = '#CDD7E2')
L.grid(row = 1, column = 1, sticky = 'e')

E = tk.Entry(frame, width = 20, font = ft1, bg = '#CDD7E2', relief = 'groove')
E.grid(row = 1, column = 2, sticky = 'w')

T = tk.Text(frame, width = 70, height = 25, font = ft2, bg = '#CDD7E2')
T.grid(row = 2, column = 1, columnspan = 5)

B = tk.Button(frame, text = 'Find', command = search, font = ft1, bg = '#CDD7E2')
B.grid(row = 1, column = 3)

Bbg = tk.Button(frame, text = 'Change Background', command = backgr, font = ft1, bg = '#CDD7E2')
Bbg.grid(row = 1, column = 4)

Bcp = tk.Button(frame, text = 'Compare', command = compare, font = ft1, bg = '#CDD7E2')
Bcp.grid(row = 1, column = 5)

Linf = tk.Label(frame, text = 'This gadget is created by HFer-Kerman.\nAll data is from Wikipedia and follows CC BY-SA 3.0.\nVersion 0.2.2   2018/07/16   License: MIT', font = ft3)
Linf.grid(row = 3, column = 1, columnspan = 2)

Lcpr = tk.Label(frame, textvariable = varpc, font = ft3)
Lcpr.grid(row = 3, column = 3, columnspan = 2)

Bex = tk.Button(frame, text = 'Export', command = export, font = ft1, bg = '#CDD7E2')
Bex.grid(row = 3, column = 5)

E.bind('<KeyPress-Return>', search)

backgr()

window.mainloop()