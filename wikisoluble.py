import tkinter as tk
import tkinter.font as tkFont
import time
from WSdata import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo

try:
    # ImageGrab is not available on linux
    from PIL import ImageGrab
except Exception as e:
    pass

window = tk.Tk()
window.title('Wiki Solubility')
window.resizable(width=False, height=False)

prev = 0
curr = 0

ft_normal = tkFont.Font(family='Arial', size=10)
ft_bold = tkFont.Font(family='Arial', size=12, weight=tkFont.BOLD)
ft_subtitle = tkFont.Font(family='Arial', size=9, weight=tkFont.BOLD)

frame = tk.Frame(bg="#FFFFFF")
frame.grid(row=0, column=0)

var = tk.StringVar()
var.set('')

varpc = tk.StringVar()

ctrdrw = False

isdark = False

ttlcolor = '#FFFFFF'
cprcolor1 = '#FF6699'
cprcolor2 = '#9966FF'
cprtxtcolor1 = '#183E58'
cprtxtcolor2 = '#796973'

normdot = '#FFFFEE'
normtext = '#00FFEE'
normline = '#FF6699'

# set canvas
C = tk.Canvas(frame,
              bg='#FFFFFF',
              width=550,
              height=550,
              highlightbackground='#FFFFFF',
              highlightcolor='#FFFFFF',
              bd=1)
C.grid(row=1, column=6, rowspan=3)


def draw(index: int):
    global isdark
    C.delete('all')

    ifdec = False
    dectemp = 0
    ifmis = False
    mistemp = 0

    max_slb = 0
    min_slb = 2000
    points = []

    for temp_str, slb in sublist[index].solub.items():

        if slb == 'N/A':
            continue

        temp = int(temp_str.replace('°C', ''))

        try:
            slb_float = float(slb)
        except Exception:
            if slb.find('×10') != -1:  # some data is in the form of num×10num
                base, exponent = map(float, slb.split('×10'))
                slb_float = round(base, 3) * pow(10, exponent)
            elif slb.find('ml') != -1:  # some data is in the form of num ml
                slblist = slb.partition('ml')
                slb_float = round(float(slblist[0]), 2)
            elif slb.endswith(')'):
                slblist = slb.replace('°C)', '').partition('(')
                temp = int(slblist[2])
                slb_float = float(slblist[0])
            elif slb == 'dec':
                ifdec = True
                dectemp = temp
            elif slb == 'miscible':
                ifmis = True
                mistemp = temp
            else:
                continue

        finally:
            points.append([temp, slb_float])
            max_slb = max(slb_float, max_slb)
            min_slb = min(slb_float, min_slb)

    return [points, max_slb, min_slb, ifdec, dectemp, ifmis, mistemp, index]


def realdraw(imformlist: list, dotcolor: str, textcolor: str, linecolor: str):
    global ctrdrw, sublist
    points = imformlist[0]
    max_slb = imformlist[1]
    min_slb = imformlist[2]
    ifdec = imformlist[3]
    dectemp = imformlist[4]
    ifmis = imformlist[5]
    mistemp = imformlist[6]
    m = imformlist[7]
    lastx = int
    lasty = int

    # draw axis
    C.create_line(50, 445, 525, 445, width=3, tag='line', fill=normline)
    C.create_line(50, 445, 50, 25, width=3, tag='line', fill=normline)
    for i in range(0, 11, 1):
        C.create_oval(47 + 47.5 * i,
                      442,
                      53 + 47.5 * i,
                      448,
                      fill=normdot,
                      width=0)
        C.create_text(50 + 47.5 * i,
                      460,
                      text=str(i * 10) + '°C',
                      fill=normtext,
                      font=ft_subtitle,
                      tag='text')
    for i in range(0, 11, 1):
        C.create_oval(47,
                      442 - 42 * i,
                      50,
                      448 - 42 * i,
                      fill=normdot,
                      width=0)
        C.create_text(25,
                      445 - 42 * i,
                      text=str(round(min_slb + (max_slb - min_slb) / 10 * i, 2)),
                      fill=normtext,
                      font=ft_subtitle,
                      tag='text')

    for i in range(len(points)):
        # print(points[i])
        x = points[i][0] * 4.75 + 25
        if max_slb != min_slb:
            y = 445 - (points[i][1] - min_slb) / (max_slb - min_slb) * 420
        else:
            y = 445 - points[i][1] / max_slb * 420
        if i != 0:
            C.create_line(lastx,
                          lasty,
                          x,
                          y,
                          width=3,
                          tag='line',
                          fill=linecolor)
        C.create_oval(x - 3, y - 3, x + 3, y + 3, fill=dotcolor, width=0)
        C.create_text(x + 20,
                      y,
                      text=str(points[i][0]) + '°C\n' + str(points[i][1]),
                      fill=textcolor,
                      font=ft_subtitle,
                      tag='text')
        lastx = x
        lasty = y
    if ifdec:
        x = dectemp * 4.75 + 25
        y = 25
        C.create_oval(x - 3, y - 3, x + 3, y + 3, fill='#FF0000', width=0)
        C.create_text(x + 5,
                      y,
                      text=sublist[m].formula + '\nDecomposes\nAt ' +
                      str(dectemp) + '°C',
                      fill='#FF0000',
                      font=ft_subtitle,
                      tag='text',
                      anchor='w')
    if ifmis:
        x = mistemp * 4.75 + 25
        y = 25
        C.create_oval(x - 3, y - 3, x + 3, y + 3, fill='#0000FF', width=0)
        C.create_text(x + 5,
                      y,
                      text=sublist[m].formula + '\nMiscibles\n At ' +
                      str(mistemp) + '°C',
                      fill='#0000FF',
                      font=ft_subtitle,
                      tag='text',
                      anchor='w')
    C.lift('text')
    C.lower('line')
    window.update()


def cvstitle(m1, m2):
    if m2 == -1:
        if isdark:
            C.create_text(275,
                          530,
                          text='Solubility Fold Line Diagram of\n%s (%s)' %
                          ((sublist[m1].name), sublist[m1].formula),
                          font=ft_bold,
                          fill='#FFFFFF')
        else:
            C.create_text(275,
                          530,
                          text='Solubility Fold Line Diagram of\n%s (%s)' %
                          ((sublist[m1].name), sublist[m1].formula),
                          font=ft_bold,
                          fill='#0F102E')
    else:
        if isdark:
            C.create_text(
                275,
                510,
                text=
                'Solubility Comparison Fold Line Diagram of\n%s (%s) and\n%s (%s)'
                % ((sublist[m1].name), sublist[m1].formula,
                   (sublist[m2].name), sublist[m2].formula),
                font=ft_bold,
                fill='#FFFFFF')
        else:
            C.create_text(
                275,
                510,
                text=
                'Solubility Comparison Fold Line Diagram of\n%s (%s) and\n%s (%s)'
                % ((sublist[m1].name), sublist[m1].formula,
                   (sublist[m2].name), sublist[m2].formula),
                font=ft_bold,
                fill='#0F102E')
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
    C.create_text(275, 530, text = 'Solubility Fold Line Diagram of\n%s (%s)' % ((sublist[m1].name), sublist[m1].formula), font = ft_bold, fill = ttlcolor)
    prevcpr = False


def contradraw(m1: int, m2: int):
    list1 = draw(m1)
    list2 = draw(m2)

    list1[1] = max(list1[1], list2[1])
    list2[1] = max(list1[1], list2[1])
    list1[2] = min(list1[2], list2[2])
    list2[2] = min(list1[2], list2[2])

    cvstitle(m1, m2)
    C.create_text(275, 510, text = 'Solubility Comparison Fold Line Diagram of', font = ft_bold, fill = ttlcolor)
    C.create_text(275, 525, text = '%s (%s)' % ((sublist[m1].name), sublist[m1].formula), font = ft_bold, fill = cprcolor1)
    C.create_text(275, 540, text = '%s (%s)' % ((sublist[m2].name), sublist[m2].formula), font = ft_bold, fill = cprcolor2)

    if isdark:
        # dark mode
        realdraw(list1, '#FFFFEE', '#EE00FF', '#FF6699')
        realdraw(list2, '#FFFFEE', '#00FFEE', '#9966FF')
        C.create_text(275,
                      477,
                      text=sublist[m1].formula,
                      fill='#FF6699',
                      font=ft_subtitle)
        C.create_text(275,
                      465,
                      text=sublist[m2].formula,
                      fill='#9966FF',
                      font=ft_subtitle)
    else:
        # light mode
        realdraw(list1, '#332255', '#40709F', '#284E68')
        realdraw(list2, '#332255', '#9F7040', '#897983')
        C.create_text(275,
                      477,
                      text=sublist[m1].formula,
                      fill='#284E68',
                      font=ft_subtitle)
        C.create_text(275,
                      465,
                      text=sublist[m2].formula,
                      fill='#897983',
                      font=ft_subtitle)

    T.delete(0.0, 'end')
    T.insert(
        'end',
        '%s\n\n%s' % (sublist[prev].getInform(), sublist[curr].getInform()))


def search(ev=None):
    global curr, prev
    T.delete(0.0, 'end')
    key = str(E.get())
    keylist = key.split()
    allsubdict = {}
    match = -1

    if key == '':
        return

    for (i, key) in enumerate(keylist):
        if key.casefold() == 'ferric':
            keylist[i] = 'iron(iii)'
        if key.casefold() == 'ferrous':
            keylist[i] = 'iron(ii)'
        if key.casefold() == 'cupric':
            keylist[i] = 'copper(ii)'
        if key.casefold() == 'cuprous':
            keylist[i] = 'copper(i)'
        if key.casefold() == 'aluminum':
            keylist[i] = 'aluminium'
        if key.casefold() == 'dichloride':
            keylist[i] = '(ii) chloride'
        if key.casefold() == 'trichloride':
            keylist[i] = '(iii) chloride'
    for i in range(0, 665):
        allnamesub = True
        allformulasub = True
        for j in range(
                0, len(keylist)
        ):  # check if all substring is contained in formula or name
            if (str(sublist[i].name).casefold().find(
                    keylist[j].casefold()) == -1):
                allnamesub = False
            if (str(sublist[i].formula).casefold().find(
                    keylist[j].casefold()) == -1):
                allformulasub = False
        if allnamesub or allformulasub:
            if (str(sublist[i].name).casefold() == key.casefold()) or (str(
                    sublist[i].formula).casefold() == key.casefold()):
                prev = curr
                curr = i
                varpc.set('Previous: %s\nCurrent:%s' %
                          (sublist[prev].formula, sublist[curr].formula))
                T.insert('end', sublist[i].getInform()
                         )  # check if it is exactly the same substance
                normdraw(i)
                return
            else:
                allsubdict[sublist[i].
                           name] = sublist[i].formula  # add to possble list
                match = i

    if len(allsubdict) == 1:  # only one possible
        prev = curr
        curr = match
        varpc.set('Previous: %s\nCurrent:%s' %
                  (sublist[prev].formula, sublist[curr].formula))
        T.insert(
            'end', 'No exact matching substance. Closest result:\n%s' %
            sublist[match].getInform())
        normdraw(match)
        return

    elif len(allsubdict) != 0:  # multiple possibilities
        if len(allsubdict) > 50:
            T.insert(
                'end',
                'Too many possible results(%d in total). Try again with something more precise.'
                % len(allsubdict))
            return
        else:
            T.insert(
                'end',
                'Multiple results found. Please determine which you\'are looking for and then search again.\n%s'
                % str(allsubdict))
            return
        return
    else:  # nothing matches
        T.insert('end', 'No result found. Please try again.')
        return


def compare():
    global prev, curr, prevcpr
    contradraw(prev, curr)
    prevcpr = True


def backgr():
    global isdark, prev, curr, prevcpr, ttlcolor, cprcolor1, cprcolor2, normdot, normtext, normline, cprtxtcolor1, cprtxtcolor2
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
        Lcpr['bg'] = '#CDD7E2'
        Lcpr['fg'] = '#0F102E'
        ttlcolor = '#0F102E'
        cprcolor1 = '#284E68'
        cprcolor2 = '#897983'
        cprtxtcolor1 = '#082E48'
        cprtxtcolor2 = '#695963'
        normdot = '#332255'
        normtext = '#40709F'
        normline = '#284E6F'
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
        Linf['bg'] = '#000022'
        Linf['fg'] = '#FFFFFF'
        Lcpr['bg'] = '#000022'
        Lcpr['fg'] = '#FFFFFF'
        ttlcolor = '#FFFFFF'
        cprcolor1 = '#FF6699'
        cprcolor2 = '#9966FF'
        cprtxtcolor1 = '#DF4679'
        cprtxtcolor2 = '#7946DF'
        normdot = '#FFFFEE'
        normtext = '#00FFEE'
        normline = '#FF6699'
    if prevcpr:
        compare()
    else:
        normdraw(curr)
    window.update()


def getter(widget, path):
    x = frame.winfo_rootx() + widget.winfo_x()
    y = frame.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    # ImageGrab.grab().crop((x, y, x1, y1)).save(path)


def export():
    global prevcpr, prev, curr
    if prevcpr:
        pngpath = '%s/%s_%s_comparision.png' % (
            askdirectory(), sublist[prev].formula, sublist[curr].formula)
    else:
        pngpath = '%s/%s_chart.png' % (askdirectory(), sublist[curr].formula)
    window.wm_attributes('-topmost', 1)
    getter(C, pngpath)
    showinfo('Export Successful', 'Successfully exported to %s' % pngpath)
    return


L = tk.Label(frame,
             text='Enter substance name or formula:',
             font=ft_bold,
             bg='#CDD7E2')
L.grid(row=1, column=1, sticky='e')

E = tk.Entry(frame, width=20, font=ft_normal, bg='#CDD7E2', relief='groove')
E.grid(row=1, column=2, sticky='w')

T = tk.Text(frame, width=70, height=25, font=ft_bold, bg='#CDD7E2')
T.grid(row=2, column=1, columnspan=5)

B = tk.Button(frame, text='Find', command=search, font=ft_normal, bg='#CDD7E2')
B.grid(row=1, column=3)

Bbg = tk.Button(frame,
                text='Change Background',
                command=backgr,
                font=ft_normal,
                bg='#CDD7E2')
Bbg.grid(row=1, column=4)

Bcp = tk.Button(frame,
                text='Compare',
                command=compare,
                font=ft_normal,
                bg='#CDD7E2')
Bcp.grid(row=1, column=5)

Linf = tk.Label(
    frame,
    text=
    'This gadget is created by HFer-Kerman.\nAll data is from Wikipedia and follows CC BY-SA 3.0.\nVersion 0.2.2   2018/07/16   License: MIT',
    font=ft_subtitle)
Linf.grid(row=3, column=1, columnspan=2)

Lcpr = tk.Label(frame, textvariable=varpc, font=ft_subtitle)
Lcpr.grid(row=3, column=3, columnspan=2)

Bex = tk.Button(frame,
                text='Export',
                command=export,
                font=ft_normal,
                bg='#CDD7E2')
Bex.grid(row=3, column=5)

E.bind('<KeyPress-Return>', search)

backgr()

window.mainloop()
