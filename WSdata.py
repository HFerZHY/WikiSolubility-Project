class substance():
    def __init__(self, name, formula):
        self.solub = {}
        self.name = name
        self.formula = formula

    def setName(self, name):
        self.name = name

    def setFormula(self, formula):
        self.formula = formula

    def getInform(self):
        return ('Name: %s\nFormula: %s\nSolubility: %s' %
                (self.name, self.formula, str(self.solub)))


sublist = []

#Here goes all the data!

s0 = substance('Actinium(III) hydroxide', 'Ac(OH)3')
s0.solub['0°C'] = 'N/A'
s0.solub['10°C'] = 'N/A'
s0.solub['15°C'] = 'N/A'
s0.solub['20°C'] = '0.0021'
s0.solub['30°C'] = 'N/A'
s0.solub['40°C'] = 'N/A'
s0.solub['50°C'] = 'N/A'
s0.solub['60°C'] = 'N/A'
s0.solub['70°C'] = 'N/A'
s0.solub['80°C'] = 'N/A'
s0.solub['90°C'] = 'N/A'
s0.solub['100°C'] = 'N/A'
sublist.append(s0)

s1 = substance('Aluminium chloride', 'AlCl3')
s1.solub['0°C'] = '43.9'
s1.solub['10°C'] = '44.9'
s1.solub['15°C'] = 'N/A'
s1.solub['20°C'] = '45.8'
s1.solub['30°C'] = '46.6'
s1.solub['40°C'] = '47.3'
s1.solub['50°C'] = 'N/A'
s1.solub['60°C'] = '48.1'
s1.solub['70°C'] = 'N/A'
s1.solub['80°C'] = '48.6'
s1.solub['90°C'] = 'N/A'
s1.solub['100°C'] = '49.0'
sublist.append(s1)

s2 = substance('Aluminium fluoride', 'AlF3')
s2.solub['0°C'] = '0.57'
s2.solub['10°C'] = '0.56'
s2.solub['15°C'] = 'N/A'
s2.solub['20°C'] = '0.67'
s2.solub['30°C'] = '0.78'
s2.solub['40°C'] = '0.91'
s2.solub['50°C'] = 'N/A'
s2.solub['60°C'] = '1.1'
s2.solub['70°C'] = 'N/A'
s2.solub['80°C'] = '1.32'
s2.solub['90°C'] = 'N/A'
s2.solub['100°C'] = '1.72'
sublist.append(s2)

s3 = substance('Aluminium hydroxide', 'Al(OH)3')
s3.solub['0°C'] = 'N/A'
s3.solub['10°C'] = 'N/A'
s3.solub['15°C'] = 'N/A'
s3.solub['20°C'] = '0.0001'
s3.solub['30°C'] = 'N/A'
s3.solub['40°C'] = 'N/A'
s3.solub['50°C'] = 'N/A'
s3.solub['60°C'] = 'N/A'
s3.solub['70°C'] = 'N/A'
s3.solub['80°C'] = 'N/A'
s3.solub['90°C'] = 'N/A'
s3.solub['100°C'] = 'N/A'
sublist.append(s3)

s4 = substance('Aluminium nitrate', 'Al(NO3)3')
s4.solub['0°C'] = '60'
s4.solub['10°C'] = '66.7'
s4.solub['15°C'] = 'N/A'
s4.solub['20°C'] = '73.9'
s4.solub['30°C'] = '81.8'
s4.solub['40°C'] = '88.7'
s4.solub['50°C'] = '96.0'
s4.solub['60°C'] = '106'
s4.solub['70°C'] = '120'
s4.solub['80°C'] = '132'
s4.solub['90°C'] = '153'
s4.solub['100°C'] = '160'
sublist.append(s4)

s5 = substance('Aluminium perchlorate', 'Al(ClO4)3')
s5.solub['0°C'] = '122'
s5.solub['10°C'] = '128'
s5.solub['15°C'] = 'N/A'
s5.solub['20°C'] = '133'
s5.solub['30°C'] = 'N/A'
s5.solub['40°C'] = 'N/A'
s5.solub['50°C'] = 'N/A'
s5.solub['60°C'] = 'N/A'
s5.solub['70°C'] = 'N/A'
s5.solub['80°C'] = 'N/A'
s5.solub['90°C'] = 'N/A'
s5.solub['100°C'] = 'N/A'
sublist.append(s5)

s6 = substance('Aluminium sulfate', 'Al2(SO4)3')
s6.solub['0°C'] = '31.2'
s6.solub['10°C'] = '33.5'
s6.solub['15°C'] = 'N/A'
s6.solub['20°C'] = '36.4'
s6.solub['30°C'] = '40.4'
s6.solub['40°C'] = '45.8'
s6.solub['50°C'] = '52.2'
s6.solub['60°C'] = '59.2'
s6.solub['70°C'] = '66.2'
s6.solub['80°C'] = '73'
s6.solub['90°C'] = '80.8'
s6.solub['100°C'] = '89.0'
sublist.append(s6)

s7 = substance('Ammonia', 'NH3')
s7.solub['0°C'] = '1176'
s7.solub['10°C'] = '900'
s7.solub['15°C'] = 'N/A'
s7.solub['20°C'] = '702'
s7.solub['30°C'] = '565'
s7.solub['40°C'] = '428'
s7.solub['50°C'] = '333'
s7.solub['60°C'] = '252'
s7.solub['70°C'] = '188'
s7.solub['80°C'] = '138'
s7.solub['90°C'] = '100'
s7.solub['100°C'] = '88'
sublist.append(s7)

s8 = substance('Ammonium acetate', 'NH4C2H3O2')
s8.solub['0°C'] = '102'
s8.solub['10°C'] = 'N/A'
s8.solub['15°C'] = 'N/A'
s8.solub['20°C'] = '143'
s8.solub['30°C'] = 'N/A'
s8.solub['40°C'] = '204'
s8.solub['50°C'] = 'N/A'
s8.solub['60°C'] = '311'
s8.solub['70°C'] = 'N/A'
s8.solub['80°C'] = '533'
s8.solub['90°C'] = 'N/A'
s8.solub['100°C'] = 'N/A'
sublist.append(s8)

s9 = substance('Ammonium azide', 'NH4N3')
s9.solub['0°C'] = '16'
s9.solub['10°C'] = 'N/A'
s9.solub['15°C'] = 'N/A'
s9.solub['20°C'] = '25.3'
s9.solub['30°C'] = 'N/A'
s9.solub['40°C'] = '37.1'
s9.solub['50°C'] = 'N/A'
s9.solub['60°C'] = 'N/A'
s9.solub['70°C'] = 'N/A'
s9.solub['80°C'] = 'N/A'
s9.solub['90°C'] = 'N/A'
s9.solub['100°C'] = 'N/A'
sublist.append(s9)

s10 = substance('Ammonium benzoate', 'NH4C7H5O2')
s10.solub['0°C'] = 'N/A'
s10.solub['10°C'] = '19.6'
s10.solub['15°C'] = 'N/A'
s10.solub['20°C'] = '21.3'
s10.solub['30°C'] = 'N/A'
s10.solub['40°C'] = 'N/A'
s10.solub['50°C'] = 'N/A'
s10.solub['60°C'] = 'N/A'
s10.solub['70°C'] = 'N/A'
s10.solub['80°C'] = 'N/A'
s10.solub['90°C'] = 'N/A'
s10.solub['100°C'] = '83'
sublist.append(s10)

s11 = substance('Ammonium bicarbonate', 'NH4HCO3')
s11.solub['0°C'] = '11.9'
s11.solub['10°C'] = '16.1'
s11.solub['15°C'] = 'N/A'
s11.solub['20°C'] = '21.7'
s11.solub['30°C'] = '28.4'
s11.solub['40°C'] = '36.6'
s11.solub['50°C'] = 'N/A'
s11.solub['60°C'] = '59.2'
s11.solub['70°C'] = 'N/A'
s11.solub['80°C'] = '109'
s11.solub['90°C'] = 'dec'
s11.solub['100°C'] = 'N/A'
sublist.append(s11)

s12 = substance('Ammonium bromide', 'NH4Br')
s12.solub['0°C'] = '60.6'
s12.solub['10°C'] = '68.1'
s12.solub['15°C'] = 'N/A'
s12.solub['20°C'] = '76.4'
s12.solub['30°C'] = '83.2'
s12.solub['40°C'] = '91.2'
s12.solub['50°C'] = '99.2'
s12.solub['60°C'] = '108'
s12.solub['70°C'] = '117'
s12.solub['80°C'] = '125'
s12.solub['90°C'] = '135'
s12.solub['100°C'] = '145'
sublist.append(s12)

s13 = substance('Ammonium carbonate', '(NH4)2CO3.H2O')
s13.solub['0°C'] = '55.8'
s13.solub['10°C'] = 'N/A'
s13.solub['15°C'] = 'N/A'
s13.solub['20°C'] = '100'
s13.solub['30°C'] = 'N/A'
s13.solub['40°C'] = 'N/A'
s13.solub['50°C'] = 'N/A'
s13.solub['60°C'] = 'dec'
s13.solub['70°C'] = 'N/A'
s13.solub['80°C'] = 'N/A'
s13.solub['90°C'] = 'N/A'
s13.solub['100°C'] = 'N/A'
sublist.append(s13)

s14 = substance('Ammonium chlorate', 'NH4ClO3')
s14.solub['0°C'] = 'N/A'
s14.solub['10°C'] = 'N/A'
s14.solub['15°C'] = 'N/A'
s14.solub['20°C'] = '28.7'
s14.solub['30°C'] = 'N/A'
s14.solub['40°C'] = 'N/A'
s14.solub['50°C'] = 'N/A'
s14.solub['60°C'] = 'N/A'
s14.solub['70°C'] = 'N/A'
s14.solub['80°C'] = 'N/A'
s14.solub['90°C'] = 'N/A'
s14.solub['100°C'] = 'N/A'
sublist.append(s14)

s15 = substance('Ammonium chloride', 'NH4Cl')
s15.solub['0°C'] = '29.4'
s15.solub['10°C'] = '33.2'
s15.solub['15°C'] = 'N/A'
s15.solub['20°C'] = '37.2'
s15.solub['30°C'] = '41.4'
s15.solub['40°C'] = '45.8'
s15.solub['50°C'] = '50.4'
s15.solub['60°C'] = '55.3'
s15.solub['70°C'] = '60.2'
s15.solub['80°C'] = '65.6'
s15.solub['90°C'] = '71.2'
s15.solub['100°C'] = '77.3'
sublist.append(s15)

s16 = substance('Ammonium hexachloroplatinate', '(NH4)2PtCl6')
s16.solub['0°C'] = '0.289'
s16.solub['10°C'] = '0.374'
s16.solub['15°C'] = 'N/A'
s16.solub['20°C'] = '0.499'
s16.solub['30°C'] = '0.637'
s16.solub['40°C'] = '0.815'
s16.solub['50°C'] = 'N/A'
s16.solub['60°C'] = '1.44'
s16.solub['70°C'] = 'N/A'
s16.solub['80°C'] = '2.16'
s16.solub['90°C'] = '2.61'
s16.solub['100°C'] = '3.36'
sublist.append(s16)

s17 = substance('Ammonium chromate', '(NH4)2CrO4')
s17.solub['0°C'] = '25'
s17.solub['10°C'] = '29.2'
s17.solub['15°C'] = 'N/A'
s17.solub['20°C'] = '34'
s17.solub['30°C'] = '39.3'
s17.solub['40°C'] = '45.3'
s17.solub['50°C'] = '51.9'
s17.solub['60°C'] = '59.0'
s17.solub['70°C'] = '71.2'
s17.solub['80°C'] = '76.1'
s17.solub['90°C'] = 'N/A'
s17.solub['100°C'] = 'N/A'
sublist.append(s17)

s18 = substance('Ammonium dichromate', '(NH4)2Cr2O7')
s18.solub['0°C'] = '18.2'
s18.solub['10°C'] = '25.5'
s18.solub['15°C'] = 'N/A'
s18.solub['20°C'] = '35.6'
s18.solub['30°C'] = '46.5'
s18.solub['40°C'] = '58.5'
s18.solub['50°C'] = '71.4'
s18.solub['60°C'] = '86.0'
s18.solub['70°C'] = 'N/A'
s18.solub['80°C'] = '115'
s18.solub['90°C'] = 'N/A'
s18.solub['100°C'] = '156'
sublist.append(s18)

s19 = substance('Ammonium dihydrogen arsenate', 'NH4H2AsO4')
s19.solub['0°C'] = '33.7'
s19.solub['10°C'] = 'N/A'
s19.solub['15°C'] = 'N/A'
s19.solub['20°C'] = '48.7'
s19.solub['30°C'] = 'N/A'
s19.solub['40°C'] = '63.8'
s19.solub['50°C'] = 'N/A'
s19.solub['60°C'] = '83'
s19.solub['70°C'] = 'N/A'
s19.solub['80°C'] = '107'
s19.solub['90°C'] = '122'
s19.solub['100°C'] = 'N/A'
sublist.append(s19)

s20 = substance('Ammonium dihydrogen phosphate', 'NH4H2PO4')
s20.solub['0°C'] = '22.7'
s20.solub['10°C'] = '39.5'
s20.solub['15°C'] = 'N/A'
s20.solub['20°C'] = '37.4'
s20.solub['30°C'] = '46.4'
s20.solub['40°C'] = '56.7'
s20.solub['50°C'] = '69.0'
s20.solub['60°C'] = '82.5'
s20.solub['70°C'] = '98.6'
s20.solub['80°C'] = '118.3'
s20.solub['90°C'] = '142.8'
s20.solub['100°C'] = '173.2'
sublist.append(s20)

s21 = substance('Ammonium fluoride', 'NH4F')
s21.solub['0°C'] = '100'
s21.solub['10°C'] = 'N/A'
s21.solub['15°C'] = 'N/A'
s21.solub['20°C'] = '85.3(25°C)'
s21.solub['30°C'] = 'N/A'
s21.solub['40°C'] = 'N/A'
s21.solub['50°C'] = 'N/A'
s21.solub['60°C'] = 'N/A'
s21.solub['70°C'] = 'N/A'
s21.solub['80°C'] = 'N/A'
s21.solub['90°C'] = 'N/A'
s21.solub['100°C'] = 'N/A'
sublist.append(s21)

s22 = substance('Ammonium fluorosilicate', '(NH4)2SiF6')
s22.solub['0°C'] = '12.28'
s22.solub['10°C'] = '16.41'
s22.solub['15°C'] = 'N/A'
s22.solub['20°C'] = '18.6'
s22.solub['30°C'] = '25.0'
s22.solub['40°C'] = '31.6'
s22.solub['50°C'] = '35.4'
s22.solub['60°C'] = '40.4'
s22.solub['70°C'] = '44.9'
s22.solub['80°C'] = '48.1(75°C)'
s22.solub['90°C'] = 'N/A'
s22.solub['100°C'] = '61.0'
sublist.append(s22)

s23 = substance('Ammonium formate', 'NH4HCO2')
s23.solub['0°C'] = '102'
s23.solub['10°C'] = 'N/A'
s23.solub['15°C'] = 'N/A'
s23.solub['20°C'] = '143'
s23.solub['30°C'] = 'N/A'
s23.solub['40°C'] = '204'
s23.solub['50°C'] = 'N/A'
s23.solub['60°C'] = '311'
s23.solub['70°C'] = 'N/A'
s23.solub['80°C'] = '533'
s23.solub['90°C'] = 'N/A'
s23.solub['100°C'] = 'N/A'
sublist.append(s23)

s24 = substance('Ammonium hydrogen phosphate', '(NH4)2HPO4')
s24.solub['0°C'] = '42.9'
s24.solub['10°C'] = '62.9'
s24.solub['15°C'] = 'N/A'
s24.solub['20°C'] = '68.9'
s24.solub['30°C'] = '75.1'
s24.solub['40°C'] = '81.8'
s24.solub['50°C'] = '89.2'
s24.solub['60°C'] = '97.2'
s24.solub['70°C'] = '106'
s24.solub['80°C'] = '110'
s24.solub['90°C'] = '112'
s24.solub['100°C'] = '121'
sublist.append(s24)

s25 = substance('Ammonium hydrogen sulfate', 'NH4HSO4')
s25.solub['0°C'] = 'N/A'
s25.solub['10°C'] = 'N/A'
s25.solub['15°C'] = 'N/A'
s25.solub['20°C'] = '100'
s25.solub['30°C'] = 'N/A'
s25.solub['40°C'] = 'N/A'
s25.solub['50°C'] = 'N/A'
s25.solub['60°C'] = 'N/A'
s25.solub['70°C'] = 'N/A'
s25.solub['80°C'] = 'N/A'
s25.solub['90°C'] = 'N/A'
s25.solub['100°C'] = 'N/A'
sublist.append(s25)

s26 = substance('Ammonium hydrogen tartrate', 'NH4HC4H4O6')
s26.solub['0°C'] = 'N/A'
s26.solub['10°C'] = '1.88'
s26.solub['15°C'] = 'N/A'
s26.solub['20°C'] = '2.7'
s26.solub['30°C'] = 'N/A'
s26.solub['40°C'] = 'N/A'
s26.solub['50°C'] = 'N/A'
s26.solub['60°C'] = 'N/A'
s26.solub['70°C'] = 'N/A'
s26.solub['80°C'] = 'N/A'
s26.solub['90°C'] = 'N/A'
s26.solub['100°C'] = 'N/A'
sublist.append(s26)

s27 = substance('Ammonium iodate', 'NH4IO3')
s27.solub['0°C'] = 'N/A'
s27.solub['10°C'] = 'N/A'
s27.solub['15°C'] = '2.6'
s27.solub['20°C'] = 'N/A'
s27.solub['30°C'] = 'N/A'
s27.solub['40°C'] = 'N/A'
s27.solub['50°C'] = 'N/A'
s27.solub['60°C'] = 'N/A'
s27.solub['70°C'] = 'N/A'
s27.solub['80°C'] = 'N/A'
s27.solub['90°C'] = 'N/A'
s27.solub['100°C'] = '14.5'
sublist.append(s27)

s28 = substance('Ammonium iodide', 'NH4I')
s28.solub['0°C'] = '155'
s28.solub['10°C'] = '163'
s28.solub['15°C'] = 'N/A'
s28.solub['20°C'] = '172'
s28.solub['30°C'] = '182'
s28.solub['40°C'] = '191'
s28.solub['50°C'] = '200'
s28.solub['60°C'] = '209'
s28.solub['70°C'] = '219'
s28.solub['80°C'] = '229'
s28.solub['90°C'] = 'N/A'
s28.solub['100°C'] = '250'
sublist.append(s28)

s29 = substance('Ammonium nitrate', 'NH4NO3')
s29.solub['0°C'] = '118'
s29.solub['10°C'] = '150'
s29.solub['15°C'] = 'N/A'
s29.solub['20°C'] = '192'
s29.solub['30°C'] = '242'
s29.solub['40°C'] = '297'
s29.solub['50°C'] = '344'
s29.solub['60°C'] = '421'
s29.solub['70°C'] = '499'
s29.solub['80°C'] = '580'
s29.solub['90°C'] = '740'
s29.solub['100°C'] = '871'
sublist.append(s29)

s30 = substance('Ammonium orthoperiodate', '(NH4)5IO6')
s30.solub['0°C'] = 'N/A'
s30.solub['10°C'] = 'N/A'
s30.solub['15°C'] = 'N/A'
s30.solub['20°C'] = '2.7'
s30.solub['30°C'] = 'N/A'
s30.solub['40°C'] = 'N/A'
s30.solub['50°C'] = 'N/A'
s30.solub['60°C'] = 'N/A'
s30.solub['70°C'] = 'N/A'
s30.solub['80°C'] = 'N/A'
s30.solub['90°C'] = 'N/A'
s30.solub['100°C'] = 'N/A'
sublist.append(s30)

s31 = substance('Ammonium oxalate', '(NH4)2C2O4')
s31.solub['0°C'] = '2.2'
s31.solub['10°C'] = '3.21'
s31.solub['15°C'] = 'N/A'
s31.solub['20°C'] = '4.45'
s31.solub['30°C'] = '6.09'
s31.solub['40°C'] = '8.18'
s31.solub['50°C'] = '10.3'
s31.solub['60°C'] = '14.0'
s31.solub['70°C'] = 'N/A'
s31.solub['80°C'] = '22.4'
s31.solub['90°C'] = '27.9'
s31.solub['100°C'] = '34.7'
sublist.append(s31)

s32 = substance('Ammonium perchlorate', 'NH4ClO4')
s32.solub['0°C'] = '11.56'
s32.solub['10°C'] = '16.4'
s32.solub['15°C'] = 'N/A'
s32.solub['20°C'] = '20.85'
s32.solub['30°C'] = 'N/A'
s32.solub['40°C'] = '30.58'
s32.solub['50°C'] = 'N/A'
s32.solub['60°C'] = '39.05'
s32.solub['70°C'] = 'N/A'
s32.solub['80°C'] = '48.19'
s32.solub['90°C'] = 'N/A'
s32.solub['100°C'] = '57.01'
sublist.append(s32)

s33 = substance('Ammonium permanganate', 'NH4MnO4')
s33.solub['0°C'] = 'N/A'
s33.solub['10°C'] = 'N/A'
s33.solub['15°C'] = '8.0'
s33.solub['20°C'] = 'N/A'
s33.solub['30°C'] = 'N/A'
s33.solub['40°C'] = 'N/A'
s33.solub['50°C'] = 'N/A'
s33.solub['60°C'] = 'dec'
s33.solub['70°C'] = 'N/A'
s33.solub['80°C'] = 'N/A'
s33.solub['90°C'] = 'N/A'
s33.solub['100°C'] = 'N/A'
sublist.append(s33)

s34 = substance('Ammonium perrhenate', 'NH4ReO4')
s34.solub['0°C'] = '2.8'
s34.solub['10°C'] = 'N/A'
s34.solub['15°C'] = 'N/A'
s34.solub['20°C'] = '6.2'
s34.solub['30°C'] = 'N/A'
s34.solub['40°C'] = '12.0'
s34.solub['50°C'] = 'N/A'
s34.solub['60°C'] = '20.7'
s34.solub['70°C'] = 'N/A'
s34.solub['80°C'] = '32.3'
s34.solub['90°C'] = '39.1'
s34.solub['100°C'] = 'N/A'
sublist.append(s34)

s35 = substance('Ammonium phosphate', '(NH4)3PO4')
s35.solub['0°C'] = '9.40'
s35.solub['10°C'] = 'N/A'
s35.solub['15°C'] = 'N/A'
s35.solub['20°C'] = '20.3'
s35.solub['30°C'] = 'N/A'
s35.solub['40°C'] = 'N/A'
s35.solub['50°C'] = '37.7'
s35.solub['60°C'] = 'N/A'
s35.solub['70°C'] = 'N/A'
s35.solub['80°C'] = 'N/A'
s35.solub['90°C'] = 'N/A'
s35.solub['100°C'] = 'N/A'
sublist.append(s35)

s36 = substance('Ammonium selenate', '(NH4)2SeO4')
s36.solub['0°C'] = '96'
s36.solub['10°C'] = '105'
s36.solub['15°C'] = 'N/A'
s36.solub['20°C'] = '115'
s36.solub['30°C'] = '126'
s36.solub['40°C'] = '143'
s36.solub['50°C'] = 'N/A'
s36.solub['60°C'] = '192'
s36.solub['70°C'] = 'N/A'
s36.solub['80°C'] = 'N/A'
s36.solub['90°C'] = 'N/A'
s36.solub['100°C'] = 'N/A'
sublist.append(s36)

s37 = substance('Ammonium sulfate', '(NH4)2SO4')
s37.solub['0°C'] = '70.6'
s37.solub['10°C'] = '73'
s37.solub['15°C'] = 'N/A'
s37.solub['20°C'] = '75.4'
s37.solub['30°C'] = '78.1'
s37.solub['40°C'] = '81.2'
s37.solub['50°C'] = '84.3'
s37.solub['60°C'] = '87.4'
s37.solub['70°C'] = 'N/A'
s37.solub['80°C'] = '94.1'
s37.solub['90°C'] = 'N/A'
s37.solub['100°C'] = '103'
sublist.append(s37)

s38 = substance('Ammonium aluminium sulfate', 'NH4Al(SO4)2.12H2O')
s38.solub['0°C'] = '2.4'
s38.solub['10°C'] = '5.0'
s38.solub['15°C'] = 'N/A'
s38.solub['20°C'] = '7.4'
s38.solub['30°C'] = '10.5'
s38.solub['40°C'] = '14.6'
s38.solub['50°C'] = '19.6'
s38.solub['60°C'] = '26.7'
s38.solub['70°C'] = '37.7'
s38.solub['80°C'] = '53.9'
s38.solub['90°C'] = '98.2'
s38.solub['100°C'] = '121'
sublist.append(s38)

s39 = substance('Ammonium sulfite', '(NH4)2SO3')
s39.solub['0°C'] = '47.9'
s39.solub['10°C'] = '54'
s39.solub['15°C'] = 'N/A'
s39.solub['20°C'] = '60.8'
s39.solub['30°C'] = '68.8'
s39.solub['40°C'] = '78.4'
s39.solub['50°C'] = 'N/A'
s39.solub['60°C'] = '104'
s39.solub['70°C'] = 'N/A'
s39.solub['80°C'] = '144'
s39.solub['90°C'] = '150'
s39.solub['100°C'] = '153'
sublist.append(s39)

s40 = substance('Ammonium tartrate', '(NH4)2C4H4O6')
s40.solub['0°C'] = '45'
s40.solub['10°C'] = '55'
s40.solub['15°C'] = 'N/A'
s40.solub['20°C'] = '63'
s40.solub['30°C'] = '70.5'
s40.solub['40°C'] = '76.5'
s40.solub['50°C'] = 'N/A'
s40.solub['60°C'] = '86.9'
s40.solub['70°C'] = 'N/A'
s40.solub['80°C'] = 'N/A'
s40.solub['90°C'] = 'N/A'
s40.solub['100°C'] = 'N/A'
sublist.append(s40)

s41 = substance('Ammonium thiocyanate', 'NH4SCN')
s41.solub['0°C'] = '120'
s41.solub['10°C'] = '144'
s41.solub['15°C'] = 'N/A'
s41.solub['20°C'] = '170'
s41.solub['30°C'] = '208'
s41.solub['40°C'] = '234'
s41.solub['50°C'] = '235'
s41.solub['60°C'] = '346'
s41.solub['70°C'] = 'N/A'
s41.solub['80°C'] = 'N/A'
s41.solub['90°C'] = 'N/A'
s41.solub['100°C'] = 'N/A'
sublist.append(s41)

s42 = substance('Ammonium thiosulfate', '(NH4)2S2O3')
s42.solub['0°C'] = 'N/A'
s42.solub['10°C'] = 'N/A'
s42.solub['15°C'] = 'N/A'
s42.solub['20°C'] = '173'
s42.solub['30°C'] = 'N/A'
s42.solub['40°C'] = '205'
s42.solub['50°C'] = 'N/A'
s42.solub['60°C'] = 'N/A'
s42.solub['70°C'] = 'N/A'
s42.solub['80°C'] = '269'
s42.solub['90°C'] = 'N/A'
s42.solub['100°C'] = 'N/A'
sublist.append(s42)

s43 = substance('Ammonium vanadate', 'NH4VO3')
s43.solub['0°C'] = 'N/A'
s43.solub['10°C'] = 'N/A'
s43.solub['15°C'] = 'N/A'
s43.solub['20°C'] = '0.48'
s43.solub['30°C'] = '0.84'
s43.solub['40°C'] = '1.32'
s43.solub['50°C'] = '1.78'
s43.solub['60°C'] = '2.42'
s43.solub['70°C'] = '3.05'
s43.solub['80°C'] = 'N/A'
s43.solub['90°C'] = 'N/A'
s43.solub['100°C'] = '7.0'
sublist.append(s43)

s44 = substance('Aniline', 'C6H7N')
s44.solub['0°C'] = 'N/A'
s44.solub['10°C'] = 'N/A'
s44.solub['15°C'] = 'N/A'
s44.solub['20°C'] = '3.6'
s44.solub['30°C'] = 'N/A'
s44.solub['40°C'] = 'N/A'
s44.solub['50°C'] = 'N/A'
s44.solub['60°C'] = 'N/A'
s44.solub['70°C'] = 'N/A'
s44.solub['80°C'] = 'N/A'
s44.solub['90°C'] = 'N/A'
s44.solub['100°C'] = 'N/A'
sublist.append(s44)

s45 = substance('Antimony trifluoride', 'SbF3')
s45.solub['0°C'] = '385'
s45.solub['10°C'] = 'N/A'
s45.solub['15°C'] = 'N/A'
s45.solub['20°C'] = '444'
s45.solub['30°C'] = '562'
s45.solub['40°C'] = 'dec'
s45.solub['50°C'] = 'N/A'
s45.solub['60°C'] = 'N/A'
s45.solub['70°C'] = 'N/A'
s45.solub['80°C'] = 'N/A'
s45.solub['90°C'] = 'N/A'
s45.solub['100°C'] = 'N/A'
sublist.append(s45)

s46 = substance('Antimony sulfide', 'Sb2S3')
s46.solub['0°C'] = 'N/A'
s46.solub['10°C'] = 'N/A'
s46.solub['15°C'] = 'N/A'
s46.solub['20°C'] = '1.8×10-4'
s46.solub['30°C'] = 'N/A'
s46.solub['40°C'] = 'N/A'
s46.solub['50°C'] = 'N/A'
s46.solub['60°C'] = 'N/A'
s46.solub['70°C'] = 'N/A'
s46.solub['80°C'] = 'N/A'
s46.solub['90°C'] = 'N/A'
s46.solub['100°C'] = 'N/A'
sublist.append(s46)

s47 = substance('Antimony trichloride', 'SbCl3')
s47.solub['0°C'] = '602'
s47.solub['10°C'] = 'N/A'
s47.solub['15°C'] = 'N/A'
s47.solub['20°C'] = '910'
s47.solub['30°C'] = '1090'
s47.solub['40°C'] = '1370'
s47.solub['50°C'] = '1917'
s47.solub['60°C'] = '4531'
s47.solub['70°C'] = 'dec'
s47.solub['80°C'] = 'N/A'
s47.solub['90°C'] = 'N/A'
s47.solub['100°C'] = 'N/A'
sublist.append(s47)

s48 = substance('Argon', 'Ar')
s48.solub['0°C'] = '0.056'
s48.solub['10°C'] = '0.0405'
s48.solub['15°C'] = 'N/A'
s48.solub['20°C'] = '0.0336'
s48.solub['30°C'] = '0.0288'
s48.solub['40°C'] = '0.0252'
s48.solub['50°C'] = '0.0223'
s48.solub['60°C'] = 'N/A'
s48.solub['70°C'] = 'N/A'
s48.solub['80°C'] = 'N/A'
s48.solub['90°C'] = 'N/A'
s48.solub['100°C'] = 'N/A'
sublist.append(s48)

s49 = substance('Arsenic pentasulfide', 'As2S5')
s49.solub['0°C'] = '0.0014'
s49.solub['10°C'] = 'N/A'
s49.solub['15°C'] = 'N/A'
s49.solub['20°C'] = 'N/A'
s49.solub['30°C'] = 'N/A'
s49.solub['40°C'] = 'N/A'
s49.solub['50°C'] = 'N/A'
s49.solub['60°C'] = 'N/A'
s49.solub['70°C'] = 'N/A'
s49.solub['80°C'] = 'N/A'
s49.solub['90°C'] = 'N/A'
s49.solub['100°C'] = 'N/A'
sublist.append(s49)

s50 = substance('Arsenic pentoxide', 'As2O5')
s50.solub['0°C'] = '59.5'
s50.solub['10°C'] = '62.1'
s50.solub['15°C'] = 'N/A'
s50.solub['20°C'] = '65.8'
s50.solub['30°C'] = '70.6'
s50.solub['40°C'] = '71.2'
s50.solub['50°C'] = 'N/A'
s50.solub['60°C'] = '73.0'
s50.solub['70°C'] = 'N/A'
s50.solub['80°C'] = '75.1'
s50.solub['90°C'] = 'N/A'
s50.solub['100°C'] = '76.7'
sublist.append(s50)

s51 = substance('Arsenious sulfide', 'As2S3')
s51.solub['0°C'] = 'N/A'
s51.solub['10°C'] = 'N/A'
s51.solub['15°C'] = 'N/A'
s51.solub['20°C'] = '0.0004'
s51.solub['30°C'] = 'N/A'
s51.solub['40°C'] = 'N/A'
s51.solub['50°C'] = 'N/A'
s51.solub['60°C'] = 'N/A'
s51.solub['70°C'] = 'N/A'
s51.solub['80°C'] = 'N/A'
s51.solub['90°C'] = 'N/A'
s51.solub['100°C'] = 'N/A'
sublist.append(s51)

s52 = substance('Arsenic trioxide', 'As2O3')
s52.solub['0°C'] = '1.21'
s52.solub['10°C'] = '1.58'
s52.solub['15°C'] = 'N/A'
s52.solub['20°C'] = '1.80'
s52.solub['30°C'] = 'N/A'
s52.solub['40°C'] = '2.93'
s52.solub['50°C'] = '3.43'
s52.solub['60°C'] = '4.44'
s52.solub['70°C'] = '5.37'
s52.solub['80°C'] = '5.89'
s52.solub['90°C'] = '6.55'
s52.solub['100°C'] = '9'
sublist.append(s52)

s53 = substance('Arsine', 'AsH3')
s53.solub['0°C'] = 'N/A'
s53.solub['10°C'] = 'N/A'
s53.solub['15°C'] = 'N/A'
s53.solub['20°C'] = '0.2'
s53.solub['30°C'] = 'N/A'
s53.solub['40°C'] = 'N/A'
s53.solub['50°C'] = 'N/A'
s53.solub['60°C'] = 'N/A'
s53.solub['70°C'] = 'N/A'
s53.solub['80°C'] = 'N/A'
s53.solub['90°C'] = 'N/A'
s53.solub['100°C'] = 'N/A'
sublist.append(s53)

s54 = substance('Barium acetate', 'Ba(C2H3O2)2')
s54.solub['0°C'] = '58.8'
s54.solub['10°C'] = '62'
s54.solub['20°C'] = '72'
s54.solub['30°C'] = '75'
s54.solub['40°C'] = '78.5'
s54.solub['50°C'] = '77'
s54.solub['60°C'] = '75'
s54.solub['70°C'] = '74'
s54.solub['80°C'] = '74'
s54.solub['90°C'] = 'N/A'
s54.solub['100°C'] = 'N/A'
sublist.append(s54)

s55 = substance('Barium arsenate', 'Ba3(AsO4)2')
s55.solub['0°C'] = 'N/A'
s55.solub['10°C'] = 'N/A'
s55.solub['20°C'] = '2.586×10-9'
s55.solub['30°C'] = 'N/A'
s55.solub['40°C'] = 'N/A'
s55.solub['50°C'] = 'N/A'
s55.solub['60°C'] = 'N/A'
s55.solub['70°C'] = 'N/A'
s55.solub['80°C'] = 'N/A'
s55.solub['90°C'] = 'N/A'
s55.solub['100°C'] = 'N/A'
sublist.append(s55)

s56 = substance('Barium azide', 'Ba(N3)2')
s56.solub['0°C'] = '12.5'
s56.solub['10°C'] = '16.1'
s56.solub['20°C'] = '17.4'
s56.solub['30°C'] = 'N/A'
s56.solub['40°C'] = 'N/A'
s56.solub['50°C'] = 'N/A'
s56.solub['60°C'] = 'N/A'
s56.solub['70°C'] = '24.75'
s56.solub['80°C'] = 'N/A'
s56.solub['90°C'] = 'N/A'
s56.solub['100°C'] = 'N/A'
sublist.append(s56)

s57 = substance('Barium bromate monohydrate', 'Ba(BrO3)2.H2O')
s57.solub['0°C'] = '0.29'
s57.solub['10°C'] = '0.44'
s57.solub['20°C'] = '0.65'
s57.solub['30°C'] = '0.95'
s57.solub['40°C'] = '1.31'
s57.solub['50°C'] = '1.75'
s57.solub['60°C'] = '2.27'
s57.solub['70°C'] = '3.01'
s57.solub['80°C'] = '3.65'
s57.solub['90°C'] = '4.45'
s57.solub['100°C'] = '5.71'
sublist.append(s57)

s58 = substance('Barium bromide', 'BaBr2')
s58.solub['0°C'] = '98'
s58.solub['10°C'] = '101'
s58.solub['20°C'] = '104'
s58.solub['30°C'] = '109'
s58.solub['40°C'] = '114'
s58.solub['50°C'] = 'N/A'
s58.solub['60°C'] = '123'
s58.solub['70°C'] = 'N/A'
s58.solub['80°C'] = '135'
s58.solub['90°C'] = 'N/A'
s58.solub['100°C'] = '149'
sublist.append(s58)

s59 = substance('Barium carbonate', 'BaCO3')
s59.solub['0°C'] = 'N/A'
s59.solub['10°C'] = 'N/A'
s59.solub['20°C'] = '2.4×10-3'
s59.solub['30°C'] = 'N/A'
s59.solub['40°C'] = 'N/A'
s59.solub['50°C'] = 'N/A'
s59.solub['60°C'] = 'N/A'
s59.solub['70°C'] = 'N/A'
s59.solub['80°C'] = 'N/A'
s59.solub['90°C'] = 'N/A'
s59.solub['100°C'] = 'N/A'
sublist.append(s59)

s60 = substance('Barium chlorate', 'Ba(ClO3)2')
s60.solub['0°C'] = '20.3'
s60.solub['10°C'] = '26.9'
s60.solub['20°C'] = '33.9'
s60.solub['30°C'] = '41.6'
s60.solub['40°C'] = '49.7'
s60.solub['50°C'] = 'N/A'
s60.solub['60°C'] = '66.7'
s60.solub['70°C'] = 'N/A'
s60.solub['80°C'] = '84.8'
s60.solub['90°C'] = 'N/A'
s60.solub['100°C'] = '105'
sublist.append(s60)

s61 = substance('Barium chloride', 'BaCl2')
s61.solub['0°C'] = '31.2'
s61.solub['10°C'] = '33.5'
s61.solub['20°C'] = '35.8'
s61.solub['30°C'] = '38.1'
s61.solub['40°C'] = '40.8'
s61.solub['50°C'] = 'N/A'
s61.solub['60°C'] = '46.2'
s61.solub['70°C'] = 'N/A'
s61.solub['80°C'] = '52.5'
s61.solub['90°C'] = '55.8'
s61.solub['100°C'] = '59.4'
sublist.append(s61)

s62 = substance('Barium chlorite', 'Ba(ClO2)2')
s62.solub['0°C'] = '43.9'
s62.solub['10°C'] = '44.6'
s62.solub['20°C'] = '45.4'
s62.solub['30°C'] = 'N/A'
s62.solub['40°C'] = '47.9'
s62.solub['50°C'] = 'N/A'
s62.solub['60°C'] = '53.8'
s62.solub['70°C'] = 'N/A'
s62.solub['80°C'] = '66.6'
s62.solub['90°C'] = 'N/A'
s62.solub['100°C'] = '80.8'
sublist.append(s62)

s63 = substance('Barium chromate', 'BaCrO4')
s63.solub['0°C'] = 'N/A'
s63.solub['10°C'] = 'N/A'
s63.solub['20°C'] = '2.775×10-4'
s63.solub['30°C'] = 'N/A'
s63.solub['40°C'] = 'N/A'
s63.solub['50°C'] = 'N/A'
s63.solub['60°C'] = 'N/A'
s63.solub['70°C'] = 'N/A'
s63.solub['80°C'] = 'N/A'
s63.solub['90°C'] = 'N/A'
s63.solub['100°C'] = 'N/A'
sublist.append(s63)

s64 = substance('Barium cyanide', 'Ba(CN)2')
s64.solub['0°C'] = 'N/A'
s64.solub['10°C'] = 'N/A'
s64.solub['20°C'] = '80'
s64.solub['30°C'] = 'N/A'
s64.solub['40°C'] = 'N/A'
s64.solub['50°C'] = 'N/A'
s64.solub['60°C'] = 'N/A'
s64.solub['70°C'] = 'N/A'
s64.solub['80°C'] = 'N/A'
s64.solub['90°C'] = 'N/A'
s64.solub['100°C'] = 'N/A'
sublist.append(s64)

s65 = substance('Barium ferrocyanide', 'Ba2Fe(CN)6')
s65.solub['0°C'] = 'N/A'
s65.solub['10°C'] = 'N/A'
s65.solub['20°C'] = '0.009732'
s65.solub['30°C'] = 'N/A'
s65.solub['40°C'] = 'N/A'
s65.solub['50°C'] = 'N/A'
s65.solub['60°C'] = 'N/A'
s65.solub['70°C'] = 'N/A'
s65.solub['80°C'] = 'N/A'
s65.solub['90°C'] = 'N/A'
s65.solub['100°C'] = 'N/A'
sublist.append(s65)

s66 = substance('Barium fluoride', 'BaF2')
s66.solub['0°C'] = 'N/A'
s66.solub['10°C'] = '0.159'
s66.solub['20°C'] = '0.16'
s66.solub['30°C'] = '0.161'
s66.solub['40°C'] = 'N/A'
s66.solub['50°C'] = 'N/A'
s66.solub['60°C'] = 'N/A'
s66.solub['70°C'] = 'N/A'
s66.solub['80°C'] = 'N/A'
s66.solub['90°C'] = 'N/A'
s66.solub['100°C'] = 'N/A'
sublist.append(s66)

s67 = substance('Barium fluorosilicate', 'BaSiF6')
s67.solub['0°C'] = 'N/A'
s67.solub['10°C'] = 'N/A'
s67.solub['20°C'] = '0.028'
s67.solub['30°C'] = 'N/A'
s67.solub['40°C'] = 'N/A'
s67.solub['50°C'] = 'N/A'
s67.solub['60°C'] = 'N/A'
s67.solub['70°C'] = 'N/A'
s67.solub['80°C'] = 'N/A'
s67.solub['90°C'] = 'N/A'
s67.solub['100°C'] = 'N/A'
sublist.append(s67)

s68 = substance('Barium formate', 'Ba(HCO2)2')
s68.solub['0°C'] = '26.2'
s68.solub['10°C'] = '28'
s68.solub['20°C'] = '31.9'
s68.solub['30°C'] = '34'
s68.solub['40°C'] = 'N/A'
s68.solub['50°C'] = '38.6'
s68.solub['60°C'] = 'N/A'
s68.solub['70°C'] = '44.2'
s68.solub['80°C'] = '47.6'
s68.solub['90°C'] = '51.3'
s68.solub['100°C'] = 'N/A'
sublist.append(s68)

s69 = substance('Barium hydrogen phosphate', 'BaHPO4')
s69.solub['0°C'] = 'N/A'
s69.solub['10°C'] = 'N/A'
s69.solub['20°C'] = '0.013'
s69.solub['30°C'] = 'N/A'
s69.solub['40°C'] = 'N/A'
s69.solub['50°C'] = 'N/A'
s69.solub['60°C'] = 'N/A'
s69.solub['70°C'] = 'N/A'
s69.solub['80°C'] = 'N/A'
s69.solub['90°C'] = 'N/A'
s69.solub['100°C'] = 'N/A'
sublist.append(s69)

s70 = substance('Barium hydrogen phosphite', 'BaHPO3')
s70.solub['0°C'] = 'N/A'
s70.solub['10°C'] = 'N/A'
s70.solub['20°C'] = '0.687'
s70.solub['30°C'] = 'N/A'
s70.solub['40°C'] = 'N/A'
s70.solub['50°C'] = 'N/A'
s70.solub['60°C'] = 'N/A'
s70.solub['70°C'] = 'N/A'
s70.solub['80°C'] = 'N/A'
s70.solub['90°C'] = 'N/A'
s70.solub['100°C'] = 'N/A'
sublist.append(s70)

s71 = substance('Barium hydroxide', 'Ba(OH)2.8H2O')
s71.solub['0°C'] = '1.67'
s71.solub['10°C'] = '2.48'
s71.solub['20°C'] = '3.89'
s71.solub['30°C'] = '5.59'
s71.solub['40°C'] = '8.22'
s71.solub['50°C'] = '11.7'
s71.solub['60°C'] = '20.9'
s71.solub['70°C'] = 'N/A'
s71.solub['80°C'] = '101'
s71.solub['90°C'] = 'N/A'
s71.solub['100°C'] = 'N/A'
sublist.append(s71)

s72 = substance('Barium iodate', 'Ba(IO3)2')
s72.solub['0°C'] = 'N/A'
s72.solub['10°C'] = 'N/A'
s72.solub['20°C'] = '0.035'
s72.solub['30°C'] = '0.046'
s72.solub['40°C'] = '0.057'
s72.solub['50°C'] = 'N/A'
s72.solub['60°C'] = 'N/A'
s72.solub['70°C'] = 'N/A'
s72.solub['80°C'] = 'N/A'
s72.solub['90°C'] = 'N/A'
s72.solub['100°C'] = '0.2'
sublist.append(s72)

s73 = substance('Barium iodide', 'BaI2')
s73.solub['0°C'] = '182'
s73.solub['10°C'] = '201'
s73.solub['20°C'] = '223'
s73.solub['30°C'] = '250'
s73.solub['40°C'] = 'N/A'
s73.solub['50°C'] = 'N/A'
s73.solub['60°C'] = '264'
s73.solub['70°C'] = 'N/A'
s73.solub['80°C'] = 'N/A'
s73.solub['90°C'] = '291'
s73.solub['100°C'] = '301'
sublist.append(s73)

s74 = substance('Barium molybdate', 'BaMoO4')
s74.solub['0°C'] = 'N/A'
s74.solub['10°C'] = 'N/A'
s74.solub['20°C'] = '0.006'
s74.solub['30°C'] = 'N/A'
s74.solub['40°C'] = 'N/A'
s74.solub['50°C'] = 'N/A'
s74.solub['60°C'] = 'N/A'
s74.solub['70°C'] = 'N/A'
s74.solub['80°C'] = 'N/A'
s74.solub['90°C'] = 'N/A'
s74.solub['100°C'] = 'N/A'
sublist.append(s74)

s75 = substance('Barium nitrate', 'Ba(NO3)2')
s75.solub['0°C'] = '4.95'
s75.solub['10°C'] = '6.77'
s75.solub['20°C'] = '9.02'
s75.solub['30°C'] = '11.5'
s75.solub['40°C'] = '14.1'
s75.solub['50°C'] = 'N/A'
s75.solub['60°C'] = '20.4'
s75.solub['70°C'] = 'N/A'
s75.solub['80°C'] = '27.2'
s75.solub['90°C'] = 'N/A'
s75.solub['100°C'] = '34.4'
sublist.append(s75)

s76 = substance('Barium nitrite', 'Ba(NO2)2')
s76.solub['0°C'] = '50.3'
s76.solub['10°C'] = '60'
s76.solub['20°C'] = '72.8'
s76.solub['30°C'] = 'N/A'
s76.solub['40°C'] = '102'
s76.solub['50°C'] = 'N/A'
s76.solub['60°C'] = '151'
s76.solub['70°C'] = 'N/A'
s76.solub['80°C'] = '222'
s76.solub['90°C'] = '261'
s76.solub['100°C'] = '325'
sublist.append(s76)

s77 = substance('Barium oxalate', 'BaC2O4.2H2O')
s77.solub['0°C'] = 'N/A'
s77.solub['10°C'] = 'N/A'
s77.solub['20°C'] = '0.003'
s77.solub['30°C'] = 'N/A'
s77.solub['40°C'] = 'N/A'
s77.solub['50°C'] = 'N/A'
s77.solub['60°C'] = 'N/A'
s77.solub['70°C'] = 'N/A'
s77.solub['80°C'] = 'N/A'
s77.solub['90°C'] = 'N/A'
s77.solub['100°C'] = 'N/A'
sublist.append(s77)

s78 = substance('Barium oxide', 'BaO')
s78.solub['0°C'] = 'N/A'
s78.solub['10°C'] = 'N/A'
s78.solub['20°C'] = '3.48'
s78.solub['30°C'] = 'N/A'
s78.solub['40°C'] = 'N/A'
s78.solub['50°C'] = 'N/A'
s78.solub['60°C'] = 'N/A'
s78.solub['70°C'] = 'N/A'
s78.solub['80°C'] = 'N/A'
s78.solub['90°C'] = '90.8'
s78.solub['100°C'] = 'N/A'
sublist.append(s78)

s79 = substance('Barium perchlorate', 'Ba(ClO4)2')
s79.solub['0°C'] = '239'
s79.solub['10°C'] = 'N/A'
s79.solub['20°C'] = '336'
s79.solub['30°C'] = 'N/A'
s79.solub['40°C'] = '416'
s79.solub['50°C'] = 'N/A'
s79.solub['60°C'] = '495'
s79.solub['70°C'] = 'N/A'
s79.solub['80°C'] = '575'
s79.solub['90°C'] = 'N/A'
s79.solub['100°C'] = '653'
sublist.append(s79)

s80 = substance('Barium permanganate', 'Ba(MnO4)2')
s80.solub['0°C'] = 'N/A'
s80.solub['10°C'] = '62.5'
s80.solub['20°C'] = 'N/A'
s80.solub['30°C'] = 'N/A'
s80.solub['40°C'] = 'N/A'
s80.solub['50°C'] = 'N/A'
s80.solub['60°C'] = 'N/A'
s80.solub['70°C'] = 'N/A'
s80.solub['80°C'] = 'N/A'
s80.solub['90°C'] = 'N/A'
s80.solub['100°C'] = 'N/A'
sublist.append(s80)

s81 = substance('Barium manganate', 'BaMnO4')
s81.solub['0°C'] = 'N/A'
s81.solub['10°C'] = 'N/A'
s81.solub['20°C'] = '0.0036'
s81.solub['30°C'] = 'N/A'
s81.solub['40°C'] = 'N/A'
s81.solub['50°C'] = 'N/A'
s81.solub['60°C'] = 'N/A'
s81.solub['70°C'] = 'N/A'
s81.solub['80°C'] = 'N/A'
s81.solub['90°C'] = 'N/A'
s81.solub['100°C'] = 'N/A'
sublist.append(s81)

s82 = substance('Barium pyrophosphate', 'Ba2P2O7')
s82.solub['0°C'] = 'N/A'
s82.solub['10°C'] = 'N/A'
s82.solub['20°C'] = '0.009'
s82.solub['30°C'] = 'N/A'
s82.solub['40°C'] = 'N/A'
s82.solub['50°C'] = 'N/A'
s82.solub['60°C'] = 'N/A'
s82.solub['70°C'] = 'N/A'
s82.solub['80°C'] = 'N/A'
s82.solub['90°C'] = 'N/A'
s82.solub['100°C'] = 'N/A'
sublist.append(s82)

s83 = substance('Barium selenate', 'BaSeO4')
s83.solub['0°C'] = 'N/A'
s83.solub['10°C'] = 'N/A'
s83.solub['20°C'] = '0.005'
s83.solub['30°C'] = 'N/A'
s83.solub['40°C'] = 'N/A'
s83.solub['50°C'] = 'N/A'
s83.solub['60°C'] = 'N/A'
s83.solub['70°C'] = 'N/A'
s83.solub['80°C'] = 'N/A'
s83.solub['90°C'] = 'N/A'
s83.solub['100°C'] = 'N/A'
sublist.append(s83)

s84 = substance('Barium sulfate', 'BaSO4')
s84.solub['0°C'] = 'N/A'
s84.solub['10°C'] = 'N/A'
s84.solub['20°C'] = '2.448×10-4'
s84.solub['30°C'] = '2.85×10-4'
s84.solub['40°C'] = 'N/A'
s84.solub['50°C'] = 'N/A'
s84.solub['60°C'] = 'N/A'
s84.solub['70°C'] = 'N/A'
s84.solub['80°C'] = 'N/A'
s84.solub['90°C'] = 'N/A'
s84.solub['100°C'] = 'N/A'
sublist.append(s84)

s85 = substance('Barium sulfide', 'BaS')
s85.solub['0°C'] = '2.88'
s85.solub['10°C'] = '4.89'
s85.solub['20°C'] = '7.86'
s85.solub['30°C'] = '10.4'
s85.solub['40°C'] = '14.9'
s85.solub['50°C'] = 'N/A'
s85.solub['60°C'] = '27.7'
s85.solub['70°C'] = 'N/A'
s85.solub['80°C'] = '49.9'
s85.solub['90°C'] = '67.3'
s85.solub['100°C'] = '60.3'
sublist.append(s85)

s86 = substance('Beryllium carbonate', 'BeCO3')
s86.solub['0°C'] = 'N/A'
s86.solub['10°C'] = 'N/A'
s86.solub['20°C'] = '0.218'
s86.solub['30°C'] = 'N/A'
s86.solub['40°C'] = 'N/A'
s86.solub['50°C'] = 'N/A'
s86.solub['60°C'] = 'N/A'
s86.solub['70°C'] = 'N/A'
s86.solub['80°C'] = 'N/A'
s86.solub['90°C'] = 'N/A'
s86.solub['100°C'] = 'N/A'
sublist.append(s86)

s87 = substance('Beryllium chloride', 'BeCl2')
s87.solub['0°C'] = 'N/A'
s87.solub['10°C'] = '42'
s87.solub['20°C'] = '42'
s87.solub['30°C'] = 'N/A'
s87.solub['40°C'] = 'N/A'
s87.solub['50°C'] = 'N/A'
s87.solub['60°C'] = 'N/A'
s87.solub['70°C'] = 'N/A'
s87.solub['80°C'] = 'N/A'
s87.solub['90°C'] = 'N/A'
s87.solub['100°C'] = 'N/A'
sublist.append(s87)

s88 = substance('Beryllium molybdate', 'BeMoO4')
s88.solub['0°C'] = 'N/A'
s88.solub['10°C'] = 'N/A'
s88.solub['20°C'] = '3.02'
s88.solub['30°C'] = 'N/A'
s88.solub['40°C'] = 'N/A'
s88.solub['50°C'] = 'N/A'
s88.solub['60°C'] = 'N/A'
s88.solub['70°C'] = 'N/A'
s88.solub['80°C'] = 'N/A'
s88.solub['90°C'] = 'N/A'
s88.solub['100°C'] = 'N/A'
sublist.append(s88)

s89 = substance('Beryllium nitrate', 'Be(NO3)2')
s89.solub['0°C'] = '97'
s89.solub['10°C'] = '102'
s89.solub['20°C'] = '108'
s89.solub['30°C'] = '113'
s89.solub['40°C'] = '125'
s89.solub['50°C'] = 'N/A'
s89.solub['60°C'] = '178'
s89.solub['70°C'] = 'N/A'
s89.solub['80°C'] = 'N/A'
s89.solub['90°C'] = 'N/A'
s89.solub['100°C'] = 'N/A'
sublist.append(s89)

s90 = substance('Beryllium oxalate', 'BeC2O4.3H2O')
s90.solub['0°C'] = 'N/A'
s90.solub['10°C'] = 'N/A'
s90.solub['20°C'] = '63.5'
s90.solub['30°C'] = 'N/A'
s90.solub['40°C'] = 'N/A'
s90.solub['50°C'] = 'N/A'
s90.solub['60°C'] = 'N/A'
s90.solub['70°C'] = 'N/A'
s90.solub['80°C'] = 'N/A'
s90.solub['90°C'] = 'N/A'
s90.solub['100°C'] = 'N/A'
sublist.append(s90)

s91 = substance('Beryllium perchlorate', 'Be(ClO4)2')
s91.solub['0°C'] = 'N/A'
s91.solub['10°C'] = 'N/A'
s91.solub['20°C'] = '147'
s91.solub['30°C'] = 'N/A'
s91.solub['40°C'] = 'N/A'
s91.solub['50°C'] = 'N/A'
s91.solub['60°C'] = 'N/A'
s91.solub['70°C'] = 'N/A'
s91.solub['80°C'] = 'N/A'
s91.solub['90°C'] = 'N/A'
s91.solub['100°C'] = 'N/A'
sublist.append(s91)

s92 = substance('Beryllium selenate', 'BeSeO4.4H2O')
s92.solub['0°C'] = 'N/A'
s92.solub['10°C'] = 'N/A'
s92.solub['20°C'] = '49'
s92.solub['30°C'] = 'N/A'
s92.solub['40°C'] = 'N/A'
s92.solub['50°C'] = 'N/A'
s92.solub['60°C'] = 'N/A'
s92.solub['70°C'] = 'N/A'
s92.solub['80°C'] = 'N/A'
s92.solub['90°C'] = 'N/A'
s92.solub['100°C'] = 'N/A'
sublist.append(s92)

s93 = substance('Beryllium sulfate', 'BeSO4.4H2O')
s93.solub['0°C'] = '37'
s93.solub['10°C'] = '37.6'
s93.solub['20°C'] = '39.1'
s93.solub['30°C'] = '41.4'
s93.solub['40°C'] = '45.8'
s93.solub['50°C'] = 'N/A'
s93.solub['60°C'] = '53.1'
s93.solub['70°C'] = 'N/A'
s93.solub['80°C'] = '67.2'
s93.solub['90°C'] = 'N/A'
s93.solub['100°C'] = '82.8'
sublist.append(s93)

s94 = substance('Bismuth arsenate', 'BiAsO4')
s94.solub['0°C'] = 'N/A'
s94.solub['10°C'] = 'N/A'
s94.solub['20°C'] = '7.298×10-4'
s94.solub['30°C'] = 'N/A'
s94.solub['40°C'] = 'N/A'
s94.solub['50°C'] = 'N/A'
s94.solub['60°C'] = 'N/A'
s94.solub['70°C'] = 'N/A'
s94.solub['80°C'] = 'N/A'
s94.solub['90°C'] = 'N/A'
s94.solub['100°C'] = 'N/A'
sublist.append(s94)

s95 = substance('Bismuth hydroxide', 'Bi(OH)3')
s95.solub['0°C'] = 'N/A'
s95.solub['10°C'] = 'N/A'
s95.solub['20°C'] = '2.868×10-7'
s95.solub['30°C'] = 'N/A'
s95.solub['40°C'] = 'N/A'
s95.solub['50°C'] = 'N/A'
s95.solub['60°C'] = 'N/A'
s95.solub['70°C'] = 'N/A'
s95.solub['80°C'] = 'N/A'
s95.solub['90°C'] = 'N/A'
s95.solub['100°C'] = 'N/A'
sublist.append(s95)

s96 = substance('Bismuth iodide', 'BiI3')
s96.solub['0°C'] = 'N/A'
s96.solub['10°C'] = 'N/A'
s96.solub['20°C'] = '7.761×10-4'
s96.solub['30°C'] = 'N/A'
s96.solub['40°C'] = 'N/A'
s96.solub['50°C'] = 'N/A'
s96.solub['60°C'] = 'N/A'
s96.solub['70°C'] = 'N/A'
s96.solub['80°C'] = 'N/A'
s96.solub['90°C'] = 'N/A'
s96.solub['100°C'] = 'N/A'
sublist.append(s96)

s97 = substance('Bismuth phosphate', 'BiPO4')
s97.solub['0°C'] = 'N/A'
s97.solub['10°C'] = 'N/A'
s97.solub['20°C'] = '1.096×10-10'
s97.solub['30°C'] = 'N/A'
s97.solub['40°C'] = 'N/A'
s97.solub['50°C'] = 'N/A'
s97.solub['60°C'] = 'N/A'
s97.solub['70°C'] = 'N/A'
s97.solub['80°C'] = 'N/A'
s97.solub['90°C'] = 'N/A'
s97.solub['100°C'] = 'N/A'
sublist.append(s97)

s98 = substance('Bismuth sulfide', 'Bi2S3')
s98.solub['0°C'] = 'N/A'
s98.solub['10°C'] = 'N/A'
s98.solub['20°C'] = '1.561×10-20'
s98.solub['30°C'] = 'N/A'
s98.solub['40°C'] = 'N/A'
s98.solub['50°C'] = 'N/A'
s98.solub['60°C'] = 'N/A'
s98.solub['70°C'] = 'N/A'
s98.solub['80°C'] = 'N/A'
s98.solub['90°C'] = 'N/A'
s98.solub['100°C'] = 'N/A'
sublist.append(s98)

s99 = substance('Boric acid', 'H3BO3')
s99.solub['0°C'] = '2.52'
s99.solub['10°C'] = '3.49'
s99.solub['20°C'] = '4.72'
s99.solub['30°C'] = '6.23'
s99.solub['40°C'] = '8.08'
s99.solub['50°C'] = '10.27'
s99.solub['60°C'] = '12.97'
s99.solub['70°C'] = '15.75'
s99.solub['80°C'] = '19.10'
s99.solub['90°C'] = '23.27'
s99.solub['100°C'] = '27.53'
sublist.append(s99)

s100 = substance('Boron trioxide', 'B2O3')
s100.solub['0°C'] = 'N/A'
s100.solub['10°C'] = 'N/A'
s100.solub['20°C'] = '2.2'
s100.solub['30°C'] = 'N/A'
s100.solub['40°C'] = 'N/A'
s100.solub['50°C'] = 'N/A'
s100.solub['60°C'] = 'N/A'
s100.solub['70°C'] = 'N/A'
s100.solub['80°C'] = 'N/A'
s100.solub['90°C'] = 'N/A'
s100.solub['100°C'] = 'N/A'
sublist.append(s100)

s101 = substance('Bromine monochloride', 'BrCl')
s101.solub['0°C'] = 'N/A'
s101.solub['10°C'] = 'N/A'
s101.solub['20°C'] = '1.5'
s101.solub['30°C'] = 'N/A'
s101.solub['40°C'] = 'N/A'
s101.solub['50°C'] = 'N/A'
s101.solub['60°C'] = 'N/A'
s101.solub['70°C'] = 'N/A'
s101.solub['80°C'] = 'N/A'
s101.solub['90°C'] = 'N/A'
s101.solub['100°C'] = 'N/A'
sublist.append(s101)

s102 = substance('Cadmium arsenate', 'Cd3(AsO4)2')
s102.solub['0°C'] = 'N/A'
s102.solub['10°C'] = 'N/A'
s102.solub['20°C'] = '7.091×10-6'
s102.solub['30°C'] = 'N/A'
s102.solub['40°C'] = 'N/A'
s102.solub['50°C'] = 'N/A'
s102.solub['60°C'] = 'N/A'
s102.solub['70°C'] = 'N/A'
s102.solub['80°C'] = 'N/A'
s102.solub['90°C'] = 'N/A'
s102.solub['100°C'] = 'N/A'
sublist.append(s102)

s103 = substance('Cadmium benzoate', 'Cd(C7H5O2)2')
s103.solub['0°C'] = 'N/A'
s103.solub['10°C'] = 'N/A'
s103.solub['20°C'] = '2.81'
s103.solub['30°C'] = 'N/A'
s103.solub['40°C'] = 'N/A'
s103.solub['50°C'] = 'N/A'
s103.solub['60°C'] = 'N/A'
s103.solub['70°C'] = 'N/A'
s103.solub['80°C'] = 'N/A'
s103.solub['90°C'] = 'N/A'
s103.solub['100°C'] = 'N/A'
sublist.append(s103)

s104 = substance('Cadmium bromate', 'Cd(BrO3)2')
s104.solub['0°C'] = 'N/A'
s104.solub['10°C'] = 'N/A'
s104.solub['20°C'] = '125'
s104.solub['30°C'] = 'N/A'
s104.solub['40°C'] = 'N/A'
s104.solub['50°C'] = 'N/A'
s104.solub['60°C'] = 'N/A'
s104.solub['70°C'] = 'N/A'
s104.solub['80°C'] = 'N/A'
s104.solub['90°C'] = 'N/A'
s104.solub['100°C'] = 'N/A'
sublist.append(s104)

s105 = substance('Cadmium bromide', 'CdBr2')
s105.solub['0°C'] = '56.3'
s105.solub['10°C'] = '75.4'
s105.solub['20°C'] = '98.8'
s105.solub['30°C'] = '129'
s105.solub['40°C'] = '152'
s105.solub['50°C'] = 'N/A'
s105.solub['60°C'] = '153'
s105.solub['70°C'] = 'N/A'
s105.solub['80°C'] = '156'
s105.solub['90°C'] = 'N/A'
s105.solub['100°C'] = '160'
sublist.append(s105)

s106 = substance('Cadmium carbonate', 'CdCO3')
s106.solub['0°C'] = 'N/A'
s106.solub['10°C'] = 'N/A'
s106.solub['20°C'] = '3.932×10-5'
s106.solub['30°C'] = 'N/A'
s106.solub['40°C'] = 'N/A'
s106.solub['50°C'] = 'N/A'
s106.solub['60°C'] = 'N/A'
s106.solub['70°C'] = 'N/A'
s106.solub['80°C'] = 'N/A'
s106.solub['90°C'] = 'N/A'
s106.solub['100°C'] = 'N/A'
sublist.append(s106)

s107 = substance('Cadmium chlorate', 'Cd(ClO3)2')
s107.solub['0°C'] = '299'
s107.solub['10°C'] = '308'
s107.solub['20°C'] = '322'
s107.solub['30°C'] = '348'
s107.solub['40°C'] = '376'
s107.solub['50°C'] = 'N/A'
s107.solub['60°C'] = '455'
s107.solub['70°C'] = 'N/A'
s107.solub['80°C'] = 'N/A'
s107.solub['90°C'] = 'N/A'
s107.solub['100°C'] = 'N/A'
sublist.append(s107)

s108 = substance('Cadmium chloride', 'CdCl2')
s108.solub['0°C'] = '100'
s108.solub['10°C'] = '135'
s108.solub['20°C'] = '135'
s108.solub['30°C'] = '135'
s108.solub['40°C'] = '135'
s108.solub['50°C'] = 'N/A'
s108.solub['60°C'] = '136'
s108.solub['70°C'] = 'N/A'
s108.solub['80°C'] = '140'
s108.solub['90°C'] = 'N/A'
s108.solub['100°C'] = '147'
sublist.append(s108)

s109 = substance('Cadmium cyanide', 'Cd(CN)2')
s109.solub['0°C'] = 'N/A'
s109.solub['10°C'] = 'N/A'
s109.solub['20°C'] = '0.022'
s109.solub['30°C'] = 'N/A'
s109.solub['40°C'] = 'N/A'
s109.solub['50°C'] = 'N/A'
s109.solub['60°C'] = 'N/A'
s109.solub['70°C'] = 'N/A'
s109.solub['80°C'] = 'N/A'
s109.solub['90°C'] = 'N/A'
s109.solub['100°C'] = 'N/A'
sublist.append(s109)

s110 = substance('Cadmium ferrocyanide', 'Cd2Fe(CN)6')
s110.solub['0°C'] = 'N/A'
s110.solub['10°C'] = 'N/A'
s110.solub['20°C'] = '8.736×10-5'
s110.solub['30°C'] = 'N/A'
s110.solub['40°C'] = 'N/A'
s110.solub['50°C'] = 'N/A'
s110.solub['60°C'] = 'N/A'
s110.solub['70°C'] = 'N/A'
s110.solub['80°C'] = 'N/A'
s110.solub['90°C'] = 'N/A'
s110.solub['100°C'] = 'N/A'
sublist.append(s110)

s111 = substance('Cadmium fluoride', 'CdF2')
s111.solub['0°C'] = 'N/A'
s111.solub['10°C'] = 'N/A'
s111.solub['20°C'] = '4'
s111.solub['30°C'] = 'N/A'
s111.solub['40°C'] = 'N/A'
s111.solub['50°C'] = 'N/A'
s111.solub['60°C'] = 'N/A'
s111.solub['70°C'] = 'N/A'
s111.solub['80°C'] = 'N/A'
s111.solub['90°C'] = 'N/A'
s111.solub['100°C'] = 'N/A'
sublist.append(s111)

s112 = substance('Cadmium formate', 'Cd(HCO2)2')
s112.solub['0°C'] = '8.3'
s112.solub['10°C'] = '11.1'
s112.solub['20°C'] = '14.4'
s112.solub['30°C'] = '18.6'
s112.solub['40°C'] = '25.3'
s112.solub['50°C'] = 'N/A'
s112.solub['60°C'] = '59.5'
s112.solub['70°C'] = 'N/A'
s112.solub['80°C'] = '80.5'
s112.solub['90°C'] = '85.2'
s112.solub['100°C'] = '94.6'
sublist.append(s112)

s113 = substance('Cadmium hydroxide', 'Cd(OH)2')
s113.solub['0°C'] = 'N/A'
s113.solub['10°C'] = 'N/A'
s113.solub['20°C'] = '2.697×10-4'
s113.solub['30°C'] = 'N/A'
s113.solub['40°C'] = 'N/A'
s113.solub['50°C'] = 'N/A'
s113.solub['60°C'] = 'N/A'
s113.solub['70°C'] = 'N/A'
s113.solub['80°C'] = 'N/A'
s113.solub['90°C'] = 'N/A'
s113.solub['100°C'] = 'N/A'
sublist.append(s113)

s114 = substance('Cadmium iodate', 'Cd(IO3)2')
s114.solub['0°C'] = 'N/A'
s114.solub['10°C'] = 'N/A'
s114.solub['20°C'] = '0.097'
s114.solub['30°C'] = 'N/A'
s114.solub['40°C'] = 'N/A'
s114.solub['50°C'] = 'N/A'
s114.solub['60°C'] = 'N/A'
s114.solub['70°C'] = 'N/A'
s114.solub['80°C'] = 'N/A'
s114.solub['90°C'] = 'N/A'
s114.solub['100°C'] = 'N/A'
sublist.append(s114)

s115 = substance('Cadmium iodide', 'CdI2')
s115.solub['0°C'] = '78.7'
s115.solub['10°C'] = 'N/A'
s115.solub['20°C'] = '84.7'
s115.solub['30°C'] = '87.9'
s115.solub['40°C'] = '92.1'
s115.solub['50°C'] = 'N/A'
s115.solub['60°C'] = '100'
s115.solub['70°C'] = 'N/A'
s115.solub['80°C'] = '111'
s115.solub['90°C'] = 'N/A'
s115.solub['100°C'] = '125'
sublist.append(s115)

s116 = substance('Cadmium nitrate', 'Cd(NO3)2')
s116.solub['0°C'] = '122'
s116.solub['10°C'] = 'N/A'
s116.solub['20°C'] = '136'
s116.solub['30°C'] = '150'
s116.solub['40°C'] = '194'
s116.solub['50°C'] = 'N/A'
s116.solub['60°C'] = '310'
s116.solub['70°C'] = 'N/A'
s116.solub['80°C'] = '713'
s116.solub['90°C'] = 'N/A'
s116.solub['100°C'] = 'N/A'
sublist.append(s116)

s117 = substance('Cadmium oxalate', 'CdC2O4.3H2O')
s117.solub['0°C'] = 'N/A'
s117.solub['10°C'] = 'N/A'
s117.solub['20°C'] = '0.006046'
s117.solub['30°C'] = 'N/A'
s117.solub['40°C'] = 'N/A'
s117.solub['50°C'] = 'N/A'
s117.solub['60°C'] = 'N/A'
s117.solub['70°C'] = 'N/A'
s117.solub['80°C'] = 'N/A'
s117.solub['90°C'] = 'N/A'
s117.solub['100°C'] = 'N/A'
sublist.append(s117)

s118 = substance('Cadmium perchlorate', 'Cd(ClO4)2')
s118.solub['0°C'] = 'N/A'
s118.solub['10°C'] = '180'
s118.solub['20°C'] = '188'
s118.solub['30°C'] = '195'
s118.solub['40°C'] = '203'
s118.solub['50°C'] = 'N/A'
s118.solub['60°C'] = '221'
s118.solub['70°C'] = 'N/A'
s118.solub['80°C'] = '243'
s118.solub['90°C'] = 'N/A'
s118.solub['100°C'] = '272'
sublist.append(s118)

s119 = substance('Cadmium phosphate', 'Cd3(PO4)2')
s119.solub['0°C'] = 'N/A'
s119.solub['10°C'] = 'N/A'
s119.solub['20°C'] = '6.235×10-6'
s119.solub['30°C'] = 'N/A'
s119.solub['40°C'] = 'N/A'
s119.solub['50°C'] = 'N/A'
s119.solub['60°C'] = 'N/A'
s119.solub['70°C'] = 'N/A'
s119.solub['80°C'] = 'N/A'
s119.solub['90°C'] = 'N/A'
s119.solub['100°C'] = 'N/A'
sublist.append(s119)

s120 = substance('Cadmium selenate', 'CdSeO4')
s120.solub['0°C'] = '72.5'
s120.solub['10°C'] = '68.4'
s120.solub['20°C'] = '64'
s120.solub['30°C'] = '58.9'
s120.solub['40°C'] = '55'
s120.solub['50°C'] = 'N/A'
s120.solub['60°C'] = '44.2'
s120.solub['70°C'] = 'N/A'
s120.solub['80°C'] = '32.5'
s120.solub['90°C'] = '27.2'
s120.solub['100°C'] = '22'
sublist.append(s120)

s121 = substance('Cadmium sulfate', 'CdSO4')
s121.solub['0°C'] = '75.4'
s121.solub['10°C'] = '76'
s121.solub['20°C'] = '76.6'
s121.solub['30°C'] = 'N/A'
s121.solub['40°C'] = '78.5'
s121.solub['50°C'] = 'N/A'
s121.solub['60°C'] = '81.8'
s121.solub['70°C'] = 'N/A'
s121.solub['80°C'] = '66.7'
s121.solub['90°C'] = '63.1'
s121.solub['100°C'] = '60.8'
sublist.append(s121)

s122 = substance('Cadmium sulfide', 'CdS')
s122.solub['0°C'] = 'N/A'
s122.solub['10°C'] = 'N/A'
s122.solub['20°C'] = '1.292×10-12'
s122.solub['30°C'] = 'N/A'
s122.solub['40°C'] = 'N/A'
s122.solub['50°C'] = 'N/A'
s122.solub['60°C'] = 'N/A'
s122.solub['70°C'] = 'N/A'
s122.solub['80°C'] = 'N/A'
s122.solub['90°C'] = 'N/A'
s122.solub['100°C'] = 'N/A'
sublist.append(s122)

s123 = substance('Cadmium tungstate', 'CdWO4')
s123.solub['0°C'] = 'N/A'
s123.solub['10°C'] = 'N/A'
s123.solub['20°C'] = '0.04642'
s123.solub['30°C'] = 'N/A'
s123.solub['40°C'] = 'N/A'
s123.solub['50°C'] = 'N/A'
s123.solub['60°C'] = 'N/A'
s123.solub['70°C'] = 'N/A'
s123.solub['80°C'] = 'N/A'
s123.solub['90°C'] = 'N/A'
s123.solub['100°C'] = 'N/A'
sublist.append(s123)

s124 = substance('Caesium acetate', 'CsC2H3O2')
s124.solub['0°C'] = 'N/A'
s124.solub['10°C'] = 'N/A'
s124.solub['20°C'] = '1010'
s124.solub['30°C'] = 'N/A'
s124.solub['40°C'] = 'N/A'
s124.solub['50°C'] = 'N/A'
s124.solub['60°C'] = 'N/A'
s124.solub['70°C'] = 'N/A'
s124.solub['80°C'] = 'N/A'
s124.solub['90°C'] = 'N/A'
s124.solub['100°C'] = 'N/A'
sublist.append(s124)

s125 = substance('Caesium azide', 'CsN3')
s125.solub['0°C'] = 'N/A'
s125.solub['10°C'] = 'N/A'
s125.solub['20°C'] = '307'
s125.solub['30°C'] = 'N/A'
s125.solub['40°C'] = 'N/A'
s125.solub['50°C'] = 'N/A'
s125.solub['60°C'] = 'N/A'
s125.solub['70°C'] = 'N/A'
s125.solub['80°C'] = 'N/A'
s125.solub['90°C'] = 'N/A'
s125.solub['100°C'] = 'N/A'
sublist.append(s125)

s126 = substance('Caesium bromate', 'CsBrO3')
s126.solub['0°C'] = '2.10'
s126.solub['10°C'] = 'N/A'
s126.solub['20°C'] = '3.66'
s126.solub['30°C'] = '4.53'
s126.solub['40°C'] = '5.3'
s126.solub['50°C'] = 'N/A'
s126.solub['60°C'] = 'N/A'
s126.solub['70°C'] = 'N/A'
s126.solub['80°C'] = 'N/A'
s126.solub['90°C'] = 'N/A'
s126.solub['100°C'] = 'N/A'
sublist.append(s126)

s127 = substance('Caesium bromide', 'CsBr')
s127.solub['0°C'] = 'N/A'
s127.solub['10°C'] = 'N/A'
s127.solub['20°C'] = '108'
s127.solub['30°C'] = 'N/A'
s127.solub['40°C'] = 'N/A'
s127.solub['50°C'] = 'N/A'
s127.solub['60°C'] = 'N/A'
s127.solub['70°C'] = 'N/A'
s127.solub['80°C'] = 'N/A'
s127.solub['90°C'] = 'N/A'
s127.solub['100°C'] = 'N/A'
sublist.append(s127)

s128 = substance('Caesium chlorate', 'CsClO3')
s128.solub['0°C'] = 'N/A'
s128.solub['10°C'] = '3.8'
s128.solub['20°C'] = '6.2'
s128.solub['30°C'] = '9.5'
s128.solub['40°C'] = '13.8'
s128.solub['50°C'] = 'N/A'
s128.solub['60°C'] = '26.2'
s128.solub['70°C'] = 'N/A'
s128.solub['80°C'] = '45'
s128.solub['90°C'] = '58'
s128.solub['100°C'] = '79'
sublist.append(s128)

s129 = substance('Caesium chloride', 'CsCl')
s129.solub['0°C'] = '146'
s129.solub['10°C'] = '175'
s129.solub['20°C'] = '187'
s129.solub['30°C'] = '197'
s129.solub['40°C'] = '208'
s129.solub['50°C'] = 'N/A'
s129.solub['60°C'] = '230'
s129.solub['70°C'] = 'N/A'
s129.solub['80°C'] = '250'
s129.solub['90°C'] = '260'
s129.solub['100°C'] = '271'
sublist.append(s129)

s130 = substance('Caesium chromate', 'Cs2CrO4')
s130.solub['0°C'] = 'N/A'
s130.solub['10°C'] = '71.4'
s130.solub['20°C'] = 'N/A'
s130.solub['30°C'] = 'N/A'
s130.solub['40°C'] = 'N/A'
s130.solub['50°C'] = 'N/A'
s130.solub['60°C'] = 'N/A'
s130.solub['70°C'] = 'N/A'
s130.solub['80°C'] = 'N/A'
s130.solub['90°C'] = 'N/A'
s130.solub['100°C'] = 'N/A'
sublist.append(s130)

s131 = substance('Caesium fluoride', 'CsF')
s131.solub['0°C'] = 'N/A'
s131.solub['10°C'] = 'N/A'
s131.solub['20°C'] = '322'
s131.solub['30°C'] = 'N/A'
s131.solub['40°C'] = 'N/A'
s131.solub['50°C'] = 'N/A'
s131.solub['60°C'] = 'N/A'
s131.solub['70°C'] = 'N/A'
s131.solub['80°C'] = 'N/A'
s131.solub['90°C'] = 'N/A'
s131.solub['100°C'] = 'N/A'
sublist.append(s131)

s132 = substance('Caesium fluoroborate', 'CsBF4')
s132.solub['0°C'] = 'N/A'
s132.solub['10°C'] = 'N/A'
s132.solub['20°C'] = '0.818'
s132.solub['30°C'] = 'N/A'
s132.solub['40°C'] = 'N/A'
s132.solub['50°C'] = 'N/A'
s132.solub['60°C'] = 'N/A'
s132.solub['70°C'] = 'N/A'
s132.solub['80°C'] = 'N/A'
s132.solub['90°C'] = 'N/A'
s132.solub['100°C'] = 'N/A'
sublist.append(s132)

s133 = substance('Caesium formate', 'CsHCO2')
s133.solub['0°C'] = '335'
s133.solub['10°C'] = '381'
s133.solub['20°C'] = '450'
s133.solub['30°C'] = '694'
s133.solub['40°C'] = 'N/A'
s133.solub['50°C'] = 'N/A'
s133.solub['60°C'] = 'N/A'
s133.solub['70°C'] = 'N/A'
s133.solub['80°C'] = 'N/A'
s133.solub['90°C'] = 'N/A'
s133.solub['100°C'] = 'N/A'
sublist.append(s133)

s134 = substance('Caesium iodate', 'CsIO3')
s134.solub['0°C'] = 'N/A'
s134.solub['10°C'] = 'N/A'
s134.solub['20°C'] = '2.6'
s134.solub['30°C'] = 'N/A'
s134.solub['40°C'] = 'N/A'
s134.solub['50°C'] = 'N/A'
s134.solub['60°C'] = 'N/A'
s134.solub['70°C'] = 'N/A'
s134.solub['80°C'] = 'N/A'
s134.solub['90°C'] = 'N/A'
s134.solub['100°C'] = 'N/A'
sublist.append(s134)

s135 = substance('Caesium iodide', 'CsI')
s135.solub['0°C'] = '44.1'
s135.solub['10°C'] = '58.5'
s135.solub['20°C'] = '76.5'
s135.solub['30°C'] = '96'
s135.solub['40°C'] = '124'
s135.solub['50°C'] = 'N/A'
s135.solub['60°C'] = '150'
s135.solub['70°C'] = 'N/A'
s135.solub['80°C'] = '190'
s135.solub['90°C'] = '205'
s135.solub['100°C'] = 'N/A'
sublist.append(s135)

s136 = substance('Caesium nitrate', 'CsNO3')
s136.solub['0°C'] = '9.33'
s136.solub['10°C'] = '14.9'
s136.solub['20°C'] = '23'
s136.solub['30°C'] = '33.9'
s136.solub['40°C'] = '47.2'
s136.solub['50°C'] = 'N/A'
s136.solub['60°C'] = '83.8'
s136.solub['70°C'] = 'N/A'
s136.solub['80°C'] = '134'
s136.solub['90°C'] = '163'
s136.solub['100°C'] = '197'
sublist.append(s136)

s137 = substance('Caesium oxalate', 'Cs2C2O4')
s137.solub['0°C'] = 'N/A'
s137.solub['10°C'] = 'N/A'
s137.solub['20°C'] = '313'
s137.solub['30°C'] = 'N/A'
s137.solub['40°C'] = 'N/A'
s137.solub['50°C'] = 'N/A'
s137.solub['60°C'] = 'N/A'
s137.solub['70°C'] = 'N/A'
s137.solub['80°C'] = 'N/A'
s137.solub['90°C'] = 'N/A'
s137.solub['100°C'] = 'N/A'
sublist.append(s137)

s138 = substance('Caesium perchlorate', 'CsClO4')
s138.solub['0°C'] = '0.8'
s138.solub['10°C'] = '1'
s138.solub['20°C'] = '1.6'
s138.solub['30°C'] = '2.6'
s138.solub['40°C'] = '4'
s138.solub['50°C'] = 'N/A'
s138.solub['60°C'] = '7.3'
s138.solub['70°C'] = 'N/A'
s138.solub['80°C'] = '14.4'
s138.solub['90°C'] = '20.5'
s138.solub['100°C'] = '30'
sublist.append(s138)

s139 = substance('Caesium permanganate', 'CsMnO4')
s139.solub['0°C'] = 'N/A'
s139.solub['10°C'] = 'N/A'
s139.solub['20°C'] = '0.228'
s139.solub['30°C'] = 'N/A'
s139.solub['40°C'] = 'N/A'
s139.solub['50°C'] = 'N/A'
s139.solub['60°C'] = 'N/A'
s139.solub['70°C'] = 'N/A'
s139.solub['80°C'] = 'N/A'
s139.solub['90°C'] = 'N/A'
s139.solub['100°C'] = 'N/A'
sublist.append(s139)

s140 = substance('Caesium selenate', 'Cs2SeO4')
s140.solub['0°C'] = 'N/A'
s140.solub['10°C'] = '244'
s140.solub['20°C'] = 'N/A'
s140.solub['30°C'] = 'N/A'
s140.solub['40°C'] = 'N/A'
s140.solub['50°C'] = 'N/A'
s140.solub['60°C'] = 'N/A'
s140.solub['70°C'] = 'N/A'
s140.solub['80°C'] = 'N/A'
s140.solub['90°C'] = 'N/A'
s140.solub['100°C'] = 'N/A'
sublist.append(s140)

s141 = substance('Caesium sulfate', 'Cs2SO4')
s141.solub['0°C'] = '167'
s141.solub['10°C'] = '173'
s141.solub['20°C'] = '179'
s141.solub['30°C'] = '184'
s141.solub['40°C'] = '190'
s141.solub['50°C'] = 'N/A'
s141.solub['60°C'] = '200'
s141.solub['70°C'] = 'N/A'
s141.solub['80°C'] = '210'
s141.solub['90°C'] = '215'
s141.solub['100°C'] = '200'
sublist.append(s141)

s142 = substance('Calcium acetate', 'Ca(C2H3O2)2')
s142.solub['0°C'] = '37.4'
s142.solub['10°C'] = '36'
s142.solub['20°C'] = '34.7'
s142.solub['30°C'] = '33.8'
s142.solub['40°C'] = '33.2'
s142.solub['50°C'] = 'N/A'
s142.solub['60°C'] = '32.7'
s142.solub['70°C'] = 'N/A'
s142.solub['80°C'] = '33.5'
s142.solub['90°C'] = '31.1'
s142.solub['100°C'] = '29.7'
sublist.append(s142)

s143 = substance('Calcium arsenate', 'Ca3(AsO4)2')
s143.solub['0°C'] = 'N/A'
s143.solub['10°C'] = 'N/A'
s143.solub['20°C'] = '0.003629'
s143.solub['30°C'] = 'N/A'
s143.solub['40°C'] = 'N/A'
s143.solub['50°C'] = 'N/A'
s143.solub['60°C'] = 'N/A'
s143.solub['70°C'] = 'N/A'
s143.solub['80°C'] = 'N/A'
s143.solub['90°C'] = 'N/A'
s143.solub['100°C'] = 'N/A'
sublist.append(s143)

s144 = substance('Calcium azide', 'Ca(N3)2')
s144.solub['0°C'] = 'N/A'
s144.solub['10°C'] = 'N/A'
s144.solub['20°C'] = '45'
s144.solub['30°C'] = 'N/A'
s144.solub['40°C'] = 'N/A'
s144.solub['50°C'] = 'N/A'
s144.solub['60°C'] = 'N/A'
s144.solub['70°C'] = 'N/A'
s144.solub['80°C'] = 'N/A'
s144.solub['90°C'] = 'N/A'
s144.solub['100°C'] = 'N/A'
sublist.append(s144)

s145 = substance('Calcium benzoate', 'Ca(C7H5O2)2.3H2O')
s145.solub['0°C'] = '2.32'
s145.solub['10°C'] = '2.45'
s145.solub['20°C'] = '2.72'
s145.solub['30°C'] = '3.02'
s145.solub['40°C'] = '3.42'
s145.solub['50°C'] = 'N/A'
s145.solub['60°C'] = '4.71'
s145.solub['70°C'] = 'N/A'
s145.solub['80°C'] = '6.87'
s145.solub['90°C'] = '8.55'
s145.solub['100°C'] = '8.7'
sublist.append(s145)

s146 = substance('Calcium bicarbonate', 'Ca(HCO3)2')
s146.solub['0°C'] = '16.1'
s146.solub['10°C'] = 'N/A'
s146.solub['20°C'] = '16.6'
s146.solub['30°C'] = 'N/A'
s146.solub['40°C'] = '17.1'
s146.solub['50°C'] = 'N/A'
s146.solub['60°C'] = '17.5'
s146.solub['70°C'] = 'N/A'
s146.solub['80°C'] = '17.9'
s146.solub['90°C'] = 'N/A'
s146.solub['100°C'] = '18.4'
sublist.append(s146)

s147 = substance('Calcium bromate', 'Ca(BrO3)2')
s147.solub['0°C'] = 'N/A'
s147.solub['10°C'] = 'N/A'
s147.solub['20°C'] = '230'
s147.solub['30°C'] = 'N/A'
s147.solub['40°C'] = 'N/A'
s147.solub['50°C'] = 'N/A'
s147.solub['60°C'] = 'N/A'
s147.solub['70°C'] = 'N/A'
s147.solub['80°C'] = 'N/A'
s147.solub['90°C'] = 'N/A'
s147.solub['100°C'] = 'N/A'
sublist.append(s147)

s148 = substance('Calcium bromide', 'CaBr2')
s148.solub['0°C'] = '125'
s148.solub['10°C'] = '132'
s148.solub['20°C'] = '143'
s148.solub['30°C'] = 'N/A'
s148.solub['40°C'] = '213'
s148.solub['50°C'] = 'N/A'
s148.solub['60°C'] = '278'
s148.solub['70°C'] = 'N/A'
s148.solub['80°C'] = '295'
s148.solub['90°C'] = 'N/A'
s148.solub['100°C'] = '312'
sublist.append(s148)

s149 = substance('Calcium carbonate (Aragonite)', 'CaCO3-Aragonite')
s149.solub['0°C'] = 'N/A'
s149.solub['10°C'] = 'N/A'
s149.solub['20°C'] = '7.753×10-4'
s149.solub['30°C'] = 'N/A'
s149.solub['40°C'] = 'N/A'
s149.solub['50°C'] = 'N/A'
s149.solub['60°C'] = 'N/A'
s149.solub['70°C'] = 'N/A'
s149.solub['80°C'] = 'N/A'
s149.solub['90°C'] = 'N/A'
s149.solub['100°C'] = 'N/A'
sublist.append(s149)

s150 = substance('Calcium carbonate (Calcite)', 'CaCO3-Calcite')
s150.solub['0°C'] = 'N/A'
s150.solub['10°C'] = 'N/A'
s150.solub['20°C'] = '6.17×10-4'
s150.solub['30°C'] = 'N/A'
s150.solub['40°C'] = 'N/A'
s150.solub['50°C'] = 'N/A'
s150.solub['60°C'] = 'N/A'
s150.solub['70°C'] = 'N/A'
s150.solub['80°C'] = 'N/A'
s150.solub['90°C'] = 'N/A'
s150.solub['100°C'] = 'N/A'
sublist.append(s150)

s151 = substance('Calcium chlorate', 'Ca(ClO3)2')
s151.solub['0°C'] = 'N/A'
s151.solub['10°C'] = 'N/A'
s151.solub['20°C'] = '209'
s151.solub['30°C'] = 'N/A'
s151.solub['40°C'] = 'N/A'
s151.solub['50°C'] = 'N/A'
s151.solub['60°C'] = 'N/A'
s151.solub['70°C'] = 'N/A'
s151.solub['80°C'] = 'N/A'
s151.solub['90°C'] = 'N/A'
s151.solub['100°C'] = 'N/A'
sublist.append(s151)

s152 = substance('Calcium chloride', 'CaCl2')
s152.solub['0°C'] = '59.5'
s152.solub['10°C'] = '64.7'
s152.solub['20°C'] = '74.5'
s152.solub['30°C'] = '100'
s152.solub['40°C'] = '128'
s152.solub['50°C'] = 'N/A'
s152.solub['60°C'] = '137'
s152.solub['70°C'] = 'N/A'
s152.solub['80°C'] = '147'
s152.solub['90°C'] = '154'
s152.solub['100°C'] = '159'
sublist.append(s152)

s153 = substance('Calcium chromate', 'CaCrO4')
s153.solub['0°C'] = '4.5'
s153.solub['10°C'] = 'N/A'
s153.solub['20°C'] = '2.25'
s153.solub['30°C'] = '1.83'
s153.solub['40°C'] = '1.49'
s153.solub['50°C'] = 'N/A'
s153.solub['60°C'] = '0.83'
s153.solub['70°C'] = 'N/A'
s153.solub['80°C'] = 'N/A'
s153.solub['90°C'] = 'N/A'
s153.solub['100°C'] = 'N/A'
sublist.append(s153)

s154 = substance('Calcium citrate', 'Ca3(C6H5O7)2')
s154.solub['0°C'] = 'N/A'
s154.solub['10°C'] = 'N/A'
s154.solub['20°C'] = '0.095(25°C)'
s154.solub['30°C'] = 'N/A'
s154.solub['40°C'] = 'N/A'
s154.solub['50°C'] = 'N/A'
s154.solub['60°C'] = 'N/A'
s154.solub['70°C'] = 'N/A'
s154.solub['80°C'] = 'N/A'
s154.solub['90°C'] = 'N/A'
s154.solub['100°C'] = 'N/A'
sublist.append(s154)

s155 = substance('Monocalcium phosphate', 'Ca(H2PO4)2')
s155.solub['0°C'] = 'N/A'
s155.solub['10°C'] = 'N/A'
s155.solub['20°C'] = '1.8'
s155.solub['30°C'] = 'N/A'
s155.solub['40°C'] = 'N/A'
s155.solub['50°C'] = 'N/A'
s155.solub['60°C'] = 'N/A'
s155.solub['70°C'] = 'N/A'
s155.solub['80°C'] = 'N/A'
s155.solub['90°C'] = 'N/A'
s155.solub['100°C'] = 'N/A'
sublist.append(s155)

s156 = substance('Calcium fluoride', 'CaF2')
s156.solub['0°C'] = '0.008575'
s156.solub['10°C'] = 'N/A'
s156.solub['20°C'] = 'N/A'
s156.solub['30°C'] = 'N/A'
s156.solub['40°C'] = 'N/A'
s156.solub['50°C'] = 'N/A'
s156.solub['60°C'] = 'N/A'
s156.solub['70°C'] = 'N/A'
s156.solub['80°C'] = 'N/A'
s156.solub['90°C'] = 'N/A'
s156.solub['100°C'] = 'N/A'
sublist.append(s156)

s157 = substance('Calcium fluorosilicate', 'CaSiF6')
s157.solub['0°C'] = 'N/A'
s157.solub['10°C'] = 'N/A'
s157.solub['20°C'] = '0.518'
s157.solub['30°C'] = 'N/A'
s157.solub['40°C'] = 'N/A'
s157.solub['50°C'] = 'N/A'
s157.solub['60°C'] = 'N/A'
s157.solub['70°C'] = 'N/A'
s157.solub['80°C'] = 'N/A'
s157.solub['90°C'] = 'N/A'
s157.solub['100°C'] = 'N/A'
sublist.append(s157)

s158 = substance('Calcium formate', 'Ca(HCO2)2')
s158.solub['0°C'] = '16.1'
s158.solub['10°C'] = 'N/A'
s158.solub['20°C'] = '16.6'
s158.solub['30°C'] = 'N/A'
s158.solub['40°C'] = '17.1'
s158.solub['50°C'] = 'N/A'
s158.solub['60°C'] = '17.5'
s158.solub['70°C'] = 'N/A'
s158.solub['80°C'] = '17.9'
s158.solub['90°C'] = 'N/A'
s158.solub['100°C'] = '18.4'
sublist.append(s158)

s159 = substance('Dicalcium phosphate', 'CaHPO4')
s159.solub['0°C'] = 'N/A'
s159.solub['10°C'] = 'N/A'
s159.solub['20°C'] = '0.004303'
s159.solub['30°C'] = 'N/A'
s159.solub['40°C'] = 'N/A'
s159.solub['50°C'] = 'N/A'
s159.solub['60°C'] = 'N/A'
s159.solub['70°C'] = 'N/A'
s159.solub['80°C'] = 'N/A'
s159.solub['90°C'] = 'N/A'
s159.solub['100°C'] = 'N/A'
sublist.append(s159)

s160 = substance('Calcium hydroxide', 'Ca(OH)2')
s160.solub['0°C'] = '0.189'
s160.solub['10°C'] = '0.182'
s160.solub['20°C'] = '0.173'
s160.solub['30°C'] = '0.16'
s160.solub['40°C'] = '0.141'
s160.solub['50°C'] = 'N/A'
s160.solub['60°C'] = '0.121'
s160.solub['70°C'] = 'N/A'
s160.solub['80°C'] = '0.086'
s160.solub['90°C'] = '0.076'
s160.solub['100°C'] = 'N/A'
sublist.append(s160)

s161 = substance('Calcium iodate', 'Ca(IO3)2')
s161.solub['0°C'] = '0.09'
s161.solub['10°C'] = 'N/A'
s161.solub['20°C'] = '0.24'
s161.solub['30°C'] = '0.38'
s161.solub['40°C'] = '0.52'
s161.solub['50°C'] = 'N/A'
s161.solub['60°C'] = '0.65'
s161.solub['70°C'] = 'N/A'
s161.solub['80°C'] = '0.66'
s161.solub['90°C'] = '0.67'
s161.solub['100°C'] = '0.67'
sublist.append(s161)

s162 = substance('Calcium iodide', 'CaI2')
s162.solub['0°C'] = '64.6'
s162.solub['10°C'] = 'N/A'
s162.solub['20°C'] = '66'
s162.solub['30°C'] = '67.6'
s162.solub['40°C'] = '70.8'
s162.solub['50°C'] = 'N/A'
s162.solub['60°C'] = '74'
s162.solub['70°C'] = 'N/A'
s162.solub['80°C'] = '78'
s162.solub['90°C'] = 'N/A'
s162.solub['100°C'] = '81'
sublist.append(s162)

s163 = substance('Calcium molybdate', 'CaMoO4')
s163.solub['0°C'] = 'N/A'
s163.solub['10°C'] = 'N/A'
s163.solub['20°C'] = '0.004099'
s163.solub['30°C'] = 'N/A'
s163.solub['40°C'] = 'N/A'
s163.solub['50°C'] = 'N/A'
s163.solub['60°C'] = 'N/A'
s163.solub['70°C'] = 'N/A'
s163.solub['80°C'] = 'N/A'
s163.solub['90°C'] = 'N/A'
s163.solub['100°C'] = 'N/A'
sublist.append(s163)

s164 = substance('Calcium nitrate', 'Ca(NO3)2')
s164.solub['0°C'] = 'N/A'
s164.solub['10°C'] = 'N/A'
s164.solub['20°C'] = '121.2'
s164.solub['30°C'] = 'N/A'
s164.solub['40°C'] = 'N/A'
s164.solub['50°C'] = 'N/A'
s164.solub['60°C'] = 'N/A'
s164.solub['70°C'] = 'N/A'
s164.solub['80°C'] = 'N/A'
s164.solub['90°C'] = 'N/A'
s164.solub['100°C'] = 'N/A'
sublist.append(s164)

s165 = substance('Calcium nitrate tetrahydrate', 'Ca(NO3)2.4H2O')
s165.solub['0°C'] = '102'
s165.solub['10°C'] = '115'
s165.solub['20°C'] = '129'
s165.solub['30°C'] = '152'
s165.solub['40°C'] = '191'
s165.solub['50°C'] = 'N/A'
s165.solub['60°C'] = 'N/A'
s165.solub['70°C'] = 'N/A'
s165.solub['80°C'] = '358'
s165.solub['90°C'] = 'N/A'
s165.solub['100°C'] = '363'
sublist.append(s165)

s166 = substance('Calcium nitrite', 'Ca(NO2)2.4H2O')
s166.solub['0°C'] = '63.9'
s166.solub['10°C'] = 'N/A'
s166.solub['20°C'] = '84.5'
s166.solub['30°C'] = '104'
s166.solub['40°C'] = 'N/A'
s166.solub['50°C'] = 'N/A'
s166.solub['60°C'] = '134'
s166.solub['70°C'] = 'N/A'
s166.solub['80°C'] = '151'
s166.solub['90°C'] = '166'
s166.solub['100°C'] = '178'
sublist.append(s166)

s167 = substance('Calcium oxalate', 'CaC2O4')
s167.solub['0°C'] = 'N/A'
s167.solub['10°C'] = 'N/A'
s167.solub['20°C'] = '6.7×10-4'
s167.solub['30°C'] = 'N/A'
s167.solub['40°C'] = 'N/A'
s167.solub['50°C'] = 'N/A'
s167.solub['60°C'] = 'N/A'
s167.solub['70°C'] = 'N/A'
s167.solub['80°C'] = 'N/A'
s167.solub['90°C'] = '0.0014'
s167.solub['100°C'] = 'N/A'
sublist.append(s167)

s168 = substance('Calcium oxide', 'CaO')
s168.solub['0°C'] = 'N/A'
s168.solub['10°C'] = 'N/A'
s168.solub['20°C'] = 'N/A'
s168.solub['30°C'] = 'N/A'
s168.solub['40°C'] = 'N/A'
s168.solub['50°C'] = 'N/A'
s168.solub['60°C'] = 'N/A'
s168.solub['70°C'] = 'N/A'
s168.solub['80°C'] = 'N/A'
s168.solub['90°C'] = 'N/A'
s168.solub['100°C'] = '5.7'
sublist.append(s168)

s169 = substance('Calcium perchlorate', 'Ca(ClO4)2')
s169.solub['0°C'] = 'N/A'
s169.solub['10°C'] = 'N/A'
s169.solub['20°C'] = '188'
s169.solub['30°C'] = 'N/A'
s169.solub['40°C'] = 'N/A'
s169.solub['50°C'] = 'N/A'
s169.solub['60°C'] = 'N/A'
s169.solub['70°C'] = 'N/A'
s169.solub['80°C'] = 'N/A'
s169.solub['90°C'] = 'N/A'
s169.solub['100°C'] = 'N/A'
sublist.append(s169)

s170 = substance('Calcium permanganate', 'Ca(MnO4)2')
s170.solub['0°C'] = 'N/A'
s170.solub['10°C'] = 'N/A'
s170.solub['20°C'] = '338'
s170.solub['30°C'] = 'N/A'
s170.solub['40°C'] = 'N/A'
s170.solub['50°C'] = 'N/A'
s170.solub['60°C'] = 'N/A'
s170.solub['70°C'] = 'N/A'
s170.solub['80°C'] = 'N/A'
s170.solub['90°C'] = 'N/A'
s170.solub['100°C'] = 'N/A'
sublist.append(s170)

s171 = substance('Calcium phosphate', 'Ca3(PO4)2')
s171.solub['0°C'] = 'N/A'
s171.solub['10°C'] = 'N/A'
s171.solub['20°C'] = '0.002'
s171.solub['30°C'] = 'N/A'
s171.solub['40°C'] = 'N/A'
s171.solub['50°C'] = 'N/A'
s171.solub['60°C'] = 'N/A'
s171.solub['70°C'] = 'N/A'
s171.solub['80°C'] = 'N/A'
s171.solub['90°C'] = 'N/A'
s171.solub['100°C'] = 'N/A'
sublist.append(s171)

s172 = substance('Calcium selenate', 'CaSeO4.2H2O')
s172.solub['0°C'] = '9.73'
s172.solub['10°C'] = '9.77'
s172.solub['20°C'] = '9.22'
s172.solub['30°C'] = '8.79'
s172.solub['40°C'] = '7.14'
s172.solub['50°C'] = 'N/A'
s172.solub['60°C'] = 'N/A'
s172.solub['70°C'] = 'N/A'
s172.solub['80°C'] = 'N/A'
s172.solub['90°C'] = 'N/A'
s172.solub['100°C'] = 'N/A'
sublist.append(s172)

s173 = substance('Calcium sulfate', 'CaSO4.2H2O')
s173.solub['0°C'] = '0.223'
s173.solub['10°C'] = '0.244'
s173.solub['20°C'] = '0.255'
s173.solub['30°C'] = '0.264'
s173.solub['40°C'] = '0.265'
s173.solub['50°C'] = 'N/A'
s173.solub['60°C'] = '0.244'
s173.solub['70°C'] = 'N/A'
s173.solub['80°C'] = '0.234'
s173.solub['90°C'] = 'N/A'
s173.solub['100°C'] = '0.205'
sublist.append(s173)

s174 = substance('Calcium tungstate', 'CaWO4')
s174.solub['0°C'] = 'N/A'
s174.solub['10°C'] = 'N/A'
s174.solub['20°C'] = '0.002387'
s174.solub['30°C'] = 'N/A'
s174.solub['40°C'] = 'N/A'
s174.solub['50°C'] = 'N/A'
s174.solub['60°C'] = 'N/A'
s174.solub['70°C'] = 'N/A'
s174.solub['80°C'] = 'N/A'
s174.solub['90°C'] = 'N/A'
s174.solub['100°C'] = 'N/A'
sublist.append(s174)

s175 = substance('Carbon dioxide', 'CO2')
s175.solub['0°C'] = 'N/A'
s175.solub['10°C'] = 'N/A'
s175.solub['20°C'] = '0.1782'
s175.solub['30°C'] = 'N/A'
s175.solub['40°C'] = 'N/A'
s175.solub['50°C'] = 'N/A'
s175.solub['60°C'] = 'N/A'
s175.solub['70°C'] = 'N/A'
s175.solub['80°C'] = 'N/A'
s175.solub['90°C'] = 'N/A'
s175.solub['100°C'] = 'N/A'
sublist.append(s175)

s176 = substance('Carbon monoxide', 'CO')
s176.solub['0°C'] = 'N/A'
s176.solub['10°C'] = 'N/A'
s176.solub['20°C'] = '0.0026'
s176.solub['30°C'] = 'N/A'
s176.solub['40°C'] = 'N/A'
s176.solub['50°C'] = 'N/A'
s176.solub['60°C'] = 'N/A'
s176.solub['70°C'] = 'N/A'
s176.solub['80°C'] = 'N/A'
s176.solub['90°C'] = 'N/A'
s176.solub['100°C'] = 'N/A'
sublist.append(s176)

s177 = substance('Cerium(III) acetate', 'Ce(C2H3O2)3')
s177.solub['0°C'] = 'N/A'
s177.solub['10°C'] = 'N/A'
s177.solub['20°C'] = '0.35'
s177.solub['30°C'] = 'N/A'
s177.solub['40°C'] = 'N/A'
s177.solub['50°C'] = 'N/A'
s177.solub['60°C'] = 'N/A'
s177.solub['70°C'] = 'N/A'
s177.solub['80°C'] = 'N/A'
s177.solub['90°C'] = 'N/A'
s177.solub['100°C'] = 'N/A'
sublist.append(s177)

s178 = substance('Cerium(III) chloride', 'CeCl3')
s178.solub['0°C'] = 'N/A'
s178.solub['10°C'] = 'N/A'
s178.solub['20°C'] = '100'
s178.solub['30°C'] = 'N/A'
s178.solub['40°C'] = 'N/A'
s178.solub['50°C'] = 'N/A'
s178.solub['60°C'] = 'N/A'
s178.solub['70°C'] = 'N/A'
s178.solub['80°C'] = 'N/A'
s178.solub['90°C'] = 'N/A'
s178.solub['100°C'] = 'N/A'
sublist.append(s178)

s179 = substance('Cerium(III) hydroxide', 'Ce(OH)3')
s179.solub['0°C'] = 'N/A'
s179.solub['10°C'] = 'N/A'
s179.solub['20°C'] = '9.43×10-5'
s179.solub['30°C'] = 'N/A'
s179.solub['40°C'] = 'N/A'
s179.solub['50°C'] = 'N/A'
s179.solub['60°C'] = 'N/A'
s179.solub['70°C'] = 'N/A'
s179.solub['80°C'] = 'N/A'
s179.solub['90°C'] = 'N/A'
s179.solub['100°C'] = 'N/A'
sublist.append(s179)

s180 = substance('Cerium(III) iodate', 'Ce(IO3)3')
s180.solub['0°C'] = 'N/A'
s180.solub['10°C'] = 'N/A'
s180.solub['20°C'] = '0.123'
s180.solub['30°C'] = 'N/A'
s180.solub['40°C'] = 'N/A'
s180.solub['50°C'] = 'N/A'
s180.solub['60°C'] = 'N/A'
s180.solub['70°C'] = 'N/A'
s180.solub['80°C'] = 'N/A'
s180.solub['90°C'] = 'N/A'
s180.solub['100°C'] = 'N/A'
sublist.append(s180)

s181 = substance('Cerium(III) nitrate', 'Ce(NO3)3')
s181.solub['0°C'] = 'N/A'
s181.solub['10°C'] = 'N/A'
s181.solub['20°C'] = '234'
s181.solub['30°C'] = 'N/A'
s181.solub['40°C'] = 'N/A'
s181.solub['50°C'] = 'N/A'
s181.solub['60°C'] = 'N/A'
s181.solub['70°C'] = 'N/A'
s181.solub['80°C'] = 'N/A'
s181.solub['90°C'] = 'N/A'
s181.solub['100°C'] = 'N/A'
sublist.append(s181)

s182 = substance('Cerium(III) phosphate', 'CePO4')
s182.solub['0°C'] = 'N/A'
s182.solub['10°C'] = 'N/A'
s182.solub['20°C'] = '7.434×10-11'
s182.solub['30°C'] = 'N/A'
s182.solub['40°C'] = 'N/A'
s182.solub['50°C'] = 'N/A'
s182.solub['60°C'] = 'N/A'
s182.solub['70°C'] = 'N/A'
s182.solub['80°C'] = 'N/A'
s182.solub['90°C'] = 'N/A'
s182.solub['100°C'] = 'N/A'
sublist.append(s182)

s183 = substance('Cerium(III) selenate', 'Ce2(SeO4)3')
s183.solub['0°C'] = '39.5'
s183.solub['10°C'] = '37.2'
s183.solub['20°C'] = '35.2'
s183.solub['30°C'] = '33.2'
s183.solub['40°C'] = '32.6'
s183.solub['50°C'] = 'N/A'
s183.solub['60°C'] = '13.7'
s183.solub['70°C'] = 'N/A'
s183.solub['80°C'] = '4.6'
s183.solub['90°C'] = 'N/A'
s183.solub['100°C'] = 'N/A'
sublist.append(s183)

s184 = substance('Cerium(III) sulfate', 'Ce2(SO4)3.2H2O')
s184.solub['0°C'] = '21.4'
s184.solub['10°C'] = 'N/A'
s184.solub['20°C'] = '9.84'
s184.solub['30°C'] = '7.24'
s184.solub['40°C'] = '5.63'
s184.solub['50°C'] = 'N/A'
s184.solub['60°C'] = '3.87'
s184.solub['70°C'] = 'N/A'
s184.solub['80°C'] = 'N/A'
s184.solub['90°C'] = 'N/A'
s184.solub['100°C'] = 'N/A'
sublist.append(s184)

s185 = substance('Cerium(IV) hydroxide', 'Ce(OH)4')
s185.solub['0°C'] = 'N/A'
s185.solub['10°C'] = 'N/A'
s185.solub['20°C'] = '1.981×10-5'
s185.solub['30°C'] = 'N/A'
s185.solub['40°C'] = 'N/A'
s185.solub['50°C'] = 'N/A'
s185.solub['60°C'] = 'N/A'
s185.solub['70°C'] = 'N/A'
s185.solub['80°C'] = 'N/A'
s185.solub['90°C'] = 'N/A'
s185.solub['100°C'] = 'N/A'
sublist.append(s185)

s186 = substance('Chromium(III) nitrate', 'Cr(NO3)3')
s186.solub['0°C'] = '108'
s186.solub['10°C'] = '124'
s186.solub['20°C'] = '130'
s186.solub['30°C'] = '152'
s186.solub['40°C'] = 'N/A'
s186.solub['50°C'] = 'N/A'
s186.solub['60°C'] = 'N/A'
s186.solub['70°C'] = 'N/A'
s186.solub['80°C'] = 'N/A'
s186.solub['90°C'] = 'N/A'
s186.solub['100°C'] = 'N/A'
sublist.append(s186)

s187 = substance('Chromium(III) perchlorate', 'Cr(ClO4)3')
s187.solub['0°C'] = '104'
s187.solub['10°C'] = '123'
s187.solub['20°C'] = '130'
s187.solub['30°C'] = 'N/A'
s187.solub['40°C'] = 'N/A'
s187.solub['50°C'] = 'N/A'
s187.solub['60°C'] = 'N/A'
s187.solub['70°C'] = 'N/A'
s187.solub['80°C'] = 'N/A'
s187.solub['90°C'] = 'N/A'
s187.solub['100°C'] = 'N/A'
sublist.append(s187)

s188 = substance('Chromium(III) sulfate', 'Cr2(SO4)3.18H2O')
s188.solub['0°C'] = 'N/A'
s188.solub['10°C'] = 'N/A'
s188.solub['20°C'] = '220'
s188.solub['30°C'] = 'N/A'
s188.solub['40°C'] = 'N/A'
s188.solub['50°C'] = 'N/A'
s188.solub['60°C'] = 'N/A'
s188.solub['70°C'] = 'N/A'
s188.solub['80°C'] = 'N/A'
s188.solub['90°C'] = 'N/A'
s188.solub['100°C'] = 'N/A'
sublist.append(s188)

s189 = substance('Chromium(VI) oxide', 'CrO3')
s189.solub['0°C'] = '61.7'
s189.solub['10°C'] = 'N/A'
s189.solub['20°C'] = '63'
s189.solub['30°C'] = 'N/A'
s189.solub['40°C'] = 'N/A'
s189.solub['50°C'] = 'N/A'
s189.solub['60°C'] = 'N/A'
s189.solub['70°C'] = 'N/A'
s189.solub['80°C'] = 'N/A'
s189.solub['90°C'] = '67'
s189.solub['100°C'] = 'N/A'
sublist.append(s189)

s190 = substance('Cobalt(II) bromate', 'Co(BrO3)2.6H2O')
s190.solub['0°C'] = 'N/A'
s190.solub['10°C'] = 'N/A'
s190.solub['20°C'] = '45.5'
s190.solub['30°C'] = 'N/A'
s190.solub['40°C'] = 'N/A'
s190.solub['50°C'] = 'N/A'
s190.solub['60°C'] = 'N/A'
s190.solub['70°C'] = 'N/A'
s190.solub['80°C'] = 'N/A'
s190.solub['90°C'] = 'N/A'
s190.solub['100°C'] = 'N/A'
sublist.append(s190)

s191 = substance('Cobalt(II) bromide', 'CoBr2')
s191.solub['0°C'] = '91.9'
s191.solub['10°C'] = 'N/A'
s191.solub['20°C'] = '112'
s191.solub['30°C'] = '128'
s191.solub['40°C'] = '163'
s191.solub['50°C'] = 'N/A'
s191.solub['60°C'] = '227'
s191.solub['70°C'] = 'N/A'
s191.solub['80°C'] = '241'
s191.solub['90°C'] = 'N/A'
s191.solub['100°C'] = '257'
sublist.append(s191)

s192 = substance('Cobalt(II) chlorate', 'Co(ClO3)2')
s192.solub['0°C'] = '135'
s192.solub['10°C'] = '162'
s192.solub['20°C'] = '180'
s192.solub['30°C'] = '195'
s192.solub['40°C'] = '214'
s192.solub['50°C'] = 'N/A'
s192.solub['60°C'] = '316'
s192.solub['70°C'] = 'N/A'
s192.solub['80°C'] = 'N/A'
s192.solub['90°C'] = 'N/A'
s192.solub['100°C'] = 'N/A'
sublist.append(s192)

s193 = substance('Cobalt(II) chloride', 'CoCl2')
s193.solub['0°C'] = '43.5'
s193.solub['10°C'] = '47.7'
s193.solub['20°C'] = '52.9'
s193.solub['30°C'] = '59.7'
s193.solub['40°C'] = '69.5'
s193.solub['50°C'] = 'N/A'
s193.solub['60°C'] = '93.8'
s193.solub['70°C'] = 'N/A'
s193.solub['80°C'] = '97.6'
s193.solub['90°C'] = '101'
s193.solub['100°C'] = '106'
sublist.append(s193)

s194 = substance('Cobalt(II) fluoride', 'CoF2')
s194.solub['0°C'] = 'N/A'
s194.solub['10°C'] = 'N/A'
s194.solub['20°C'] = '1.36'
s194.solub['30°C'] = 'N/A'
s194.solub['40°C'] = 'N/A'
s194.solub['50°C'] = 'N/A'
s194.solub['60°C'] = 'N/A'
s194.solub['70°C'] = 'N/A'
s194.solub['80°C'] = 'N/A'
s194.solub['90°C'] = 'N/A'
s194.solub['100°C'] = 'N/A'
sublist.append(s194)

s195 = substance('Cobalt(II) fluorosilicate', 'CoSiF6.6H2')
s195.solub['0°C'] = 'N/A'
s195.solub['10°C'] = 'N/A'
s195.solub['20°C'] = '118'
s195.solub['30°C'] = 'N/A'
s195.solub['40°C'] = 'N/A'
s195.solub['50°C'] = 'N/A'
s195.solub['60°C'] = 'N/A'
s195.solub['70°C'] = 'N/A'
s195.solub['80°C'] = 'N/A'
s195.solub['90°C'] = 'N/A'
s195.solub['100°C'] = 'N/A'
sublist.append(s195)

s196 = substance('Cobalt(II) iodate', 'Co(IO3)2.2H2O')
s196.solub['0°C'] = 'N/A'
s196.solub['10°C'] = 'N/A'
s196.solub['20°C'] = '1.02'
s196.solub['30°C'] = '0.9'
s196.solub['40°C'] = '0.88'
s196.solub['50°C'] = 'N/A'
s196.solub['60°C'] = '0.82'
s196.solub['70°C'] = 'N/A'
s196.solub['80°C'] = '0.73'
s196.solub['90°C'] = 'N/A'
s196.solub['100°C'] = '0.7'
sublist.append(s196)

s197 = substance('Cobalt(II) iodide', 'CoI2')
s197.solub['0°C'] = 'N/A'
s197.solub['10°C'] = 'N/A'
s197.solub['20°C'] = '203'
s197.solub['30°C'] = 'N/A'
s197.solub['40°C'] = 'N/A'
s197.solub['50°C'] = 'N/A'
s197.solub['60°C'] = 'N/A'
s197.solub['70°C'] = 'N/A'
s197.solub['80°C'] = 'N/A'
s197.solub['90°C'] = 'N/A'
s197.solub['100°C'] = 'N/A'
sublist.append(s197)

s198 = substance('Cobalt(II) nitrate', 'Co(NO3)2')
s198.solub['0°C'] = '84'
s198.solub['10°C'] = '89.6'
s198.solub['20°C'] = '97.4'
s198.solub['30°C'] = '111'
s198.solub['40°C'] = '125'
s198.solub['50°C'] = 'N/A'
s198.solub['60°C'] = '174'
s198.solub['70°C'] = 'N/A'
s198.solub['80°C'] = '204'
s198.solub['90°C'] = '300'
s198.solub['100°C'] = 'N/A'
sublist.append(s198)

s199 = substance('Cobalt(II) nitrite', 'Co(NO2)2')
s199.solub['0°C'] = '0.076'
s199.solub['10°C'] = '0.24'
s199.solub['20°C'] = '0.4'
s199.solub['30°C'] = '0.61'
s199.solub['40°C'] = '0.85'
s199.solub['50°C'] = 'N/A'
s199.solub['60°C'] = 'N/A'
s199.solub['70°C'] = 'N/A'
s199.solub['80°C'] = 'N/A'
s199.solub['90°C'] = 'N/A'
s199.solub['100°C'] = 'N/A'
sublist.append(s199)

s200 = substance('Cobalt oxalate', 'CoC2O4.2H2O')
s200.solub['0°C'] = 'N/A'
s200.solub['10°C'] = 'N/A'
s200.solub['20°C'] = '2.6972×10-9'
s200.solub['30°C'] = 'N/A'
s200.solub['40°C'] = 'N/A'
s200.solub['50°C'] = 'N/A'
s200.solub['60°C'] = 'N/A'
s200.solub['70°C'] = 'N/A'
s200.solub['80°C'] = 'N/A'
s200.solub['90°C'] = 'N/A'
s200.solub['100°C'] = 'N/A'
sublist.append(s200)

s201 = substance('Cobalt(II) perchlorate', 'Co(ClO4)2')
s201.solub['0°C'] = 'N/A'
s201.solub['10°C'] = 'N/A'
s201.solub['20°C'] = '104'
s201.solub['30°C'] = 'N/A'
s201.solub['40°C'] = 'N/A'
s201.solub['50°C'] = 'N/A'
s201.solub['60°C'] = 'N/A'
s201.solub['70°C'] = 'N/A'
s201.solub['80°C'] = 'N/A'
s201.solub['90°C'] = 'N/A'
s201.solub['100°C'] = 'N/A'
sublist.append(s201)

s202 = substance('Cobalt(II) sulfate', 'CoSO4')
s202.solub['0°C'] = '25.5'
s202.solub['10°C'] = '30.5'
s202.solub['20°C'] = '36.1'
s202.solub['30°C'] = '42'
s202.solub['40°C'] = '48.8'
s202.solub['50°C'] = 'N/A'
s202.solub['60°C'] = '55'
s202.solub['70°C'] = 'N/A'
s202.solub['80°C'] = '53.8'
s202.solub['90°C'] = '45.3'
s202.solub['100°C'] = '38.9'
sublist.append(s202)

s203 = substance('Copper(I) chloride', 'CuCl')
s203.solub['0°C'] = 'N/A'
s203.solub['10°C'] = 'N/A'
s203.solub['20°C'] = '0.0099'
s203.solub['30°C'] = 'N/A'
s203.solub['40°C'] = 'N/A'
s203.solub['50°C'] = 'N/A'
s203.solub['60°C'] = 'N/A'
s203.solub['70°C'] = 'N/A'
s203.solub['80°C'] = 'N/A'
s203.solub['90°C'] = 'N/A'
s203.solub['100°C'] = 'N/A'
sublist.append(s203)

s204 = substance('Copper(I) cyanide', 'CuCN')
s204.solub['0°C'] = 'N/A'
s204.solub['10°C'] = 'N/A'
s204.solub['20°C'] = '1.602×10-9'
s204.solub['30°C'] = 'N/A'
s204.solub['40°C'] = 'N/A'
s204.solub['50°C'] = 'N/A'
s204.solub['60°C'] = 'N/A'
s204.solub['70°C'] = 'N/A'
s204.solub['80°C'] = 'N/A'
s204.solub['90°C'] = 'N/A'
s204.solub['100°C'] = 'N/A'
sublist.append(s204)

s205 = substance('Copper(I) hydroxide', 'CuOH')
s205.solub['0°C'] = 'N/A'
s205.solub['10°C'] = 'N/A'
s205.solub['20°C'] = '8.055×10-7'
s205.solub['30°C'] = 'N/A'
s205.solub['40°C'] = 'N/A'
s205.solub['50°C'] = 'N/A'
s205.solub['60°C'] = 'N/A'
s205.solub['70°C'] = 'N/A'
s205.solub['80°C'] = 'N/A'
s205.solub['90°C'] = 'N/A'
s205.solub['100°C'] = 'N/A'
sublist.append(s205)

s206 = substance('Copper(I) iodide', 'CuI')
s206.solub['0°C'] = 'N/A'
s206.solub['10°C'] = 'N/A'
s206.solub['20°C'] = '1.997×10-5'
s206.solub['30°C'] = 'N/A'
s206.solub['40°C'] = 'N/A'
s206.solub['50°C'] = 'N/A'
s206.solub['60°C'] = 'N/A'
s206.solub['70°C'] = 'N/A'
s206.solub['80°C'] = 'N/A'
s206.solub['90°C'] = 'N/A'
s206.solub['100°C'] = 'N/A'
sublist.append(s206)

s207 = substance('Copper(I) sulfide', 'Cu2S')
s207.solub['0°C'] = 'N/A'
s207.solub['10°C'] = 'N/A'
s207.solub['20°C'] = '1.361×10-15'
s207.solub['30°C'] = 'N/A'
s207.solub['40°C'] = 'N/A'
s207.solub['50°C'] = 'N/A'
s207.solub['60°C'] = 'N/A'
s207.solub['70°C'] = 'N/A'
s207.solub['80°C'] = 'N/A'
s207.solub['90°C'] = 'N/A'
s207.solub['100°C'] = 'N/A'
sublist.append(s207)

s208 = substance('Copper(I) thiocyanate', 'CuSCN')
s208.solub['0°C'] = 'N/A'
s208.solub['10°C'] = 'N/A'
s208.solub['20°C'] = '8.427×10-7'
s208.solub['30°C'] = 'N/A'
s208.solub['40°C'] = 'N/A'
s208.solub['50°C'] = 'N/A'
s208.solub['60°C'] = 'N/A'
s208.solub['70°C'] = 'N/A'
s208.solub['80°C'] = 'N/A'
s208.solub['90°C'] = 'N/A'
s208.solub['100°C'] = 'N/A'
sublist.append(s208)

s209 = substance('Copper(II) bromide', 'CuBr2')
s209.solub['0°C'] = '107'
s209.solub['10°C'] = '116'
s209.solub['20°C'] = '126'
s209.solub['30°C'] = '128'
s209.solub['40°C'] = '131'
s209.solub['50°C'] = 'N/A'
s209.solub['60°C'] = 'N/A'
s209.solub['70°C'] = 'N/A'
s209.solub['80°C'] = 'N/A'
s209.solub['90°C'] = 'N/A'
s209.solub['100°C'] = 'N/A'
sublist.append(s209)

s210 = substance('Copper(II) carbonate', 'CuCO3')
s210.solub['0°C'] = 'N/A'
s210.solub['10°C'] = 'N/A'
s210.solub['20°C'] = '1.462×10-4'
s210.solub['30°C'] = 'N/A'
s210.solub['40°C'] = 'N/A'
s210.solub['50°C'] = 'N/A'
s210.solub['60°C'] = 'N/A'
s210.solub['70°C'] = 'N/A'
s210.solub['80°C'] = 'N/A'
s210.solub['90°C'] = 'N/A'
s210.solub['100°C'] = 'N/A'
sublist.append(s210)

s211 = substance('Copper(II) chlorate', 'Cu(ClO3)2')
s211.solub['0°C'] = 'N/A'
s211.solub['10°C'] = 'N/A'
s211.solub['20°C'] = '242'
s211.solub['30°C'] = 'N/A'
s211.solub['40°C'] = 'N/A'
s211.solub['50°C'] = 'N/A'
s211.solub['60°C'] = 'N/A'
s211.solub['70°C'] = 'N/A'
s211.solub['80°C'] = 'N/A'
s211.solub['90°C'] = 'N/A'
s211.solub['100°C'] = 'N/A'
sublist.append(s211)

s212 = substance('Copper(II) chloride', 'CuCl2')
s212.solub['0°C'] = '68.6'
s212.solub['10°C'] = '70.9'
s212.solub['20°C'] = '73'
s212.solub['30°C'] = '77.3'
s212.solub['40°C'] = '87.6'
s212.solub['50°C'] = 'N/A'
s212.solub['60°C'] = '96.5'
s212.solub['70°C'] = 'N/A'
s212.solub['80°C'] = '104'
s212.solub['90°C'] = '108'
s212.solub['100°C'] = '120'
sublist.append(s212)

s213 = substance('Copper(II) chromate', 'CuCrO4')
s213.solub['0°C'] = 'N/A'
s213.solub['10°C'] = 'N/A'
s213.solub['20°C'] = '0.03407'
s213.solub['30°C'] = 'N/A'
s213.solub['40°C'] = 'N/A'
s213.solub['50°C'] = 'N/A'
s213.solub['60°C'] = 'N/A'
s213.solub['70°C'] = 'N/A'
s213.solub['80°C'] = 'N/A'
s213.solub['90°C'] = 'N/A'
s213.solub['100°C'] = 'N/A'
sublist.append(s213)

s214 = substance('Copper(II) fluoride', 'CuF2')
s214.solub['0°C'] = 'N/A'
s214.solub['10°C'] = 'N/A'
s214.solub['20°C'] = '0.075'
s214.solub['30°C'] = 'N/A'
s214.solub['40°C'] = 'N/A'
s214.solub['50°C'] = 'N/A'
s214.solub['60°C'] = 'N/A'
s214.solub['70°C'] = 'N/A'
s214.solub['80°C'] = 'N/A'
s214.solub['90°C'] = 'N/A'
s214.solub['100°C'] = 'N/A'
sublist.append(s214)

s215 = substance('Copper(II) fluorosilicate', 'CuSiF6')
s215.solub['0°C'] = '73.5'
s215.solub['10°C'] = '76.5'
s215.solub['20°C'] = '81.6'
s215.solub['30°C'] = '84.1'
s215.solub['40°C'] = '91.2'
s215.solub['50°C'] = 'N/A'
s215.solub['60°C'] = 'N/A'
s215.solub['70°C'] = 'N/A'
s215.solub['80°C'] = '93.2'
s215.solub['90°C'] = 'N/A'
s215.solub['100°C'] = 'N/A'
sublist.append(s215)

s216 = substance('Copper(II) formate', 'Cu(HCO2)2')
s216.solub['0°C'] = 'N/A'
s216.solub['10°C'] = 'N/A'
s216.solub['20°C'] = '12.5'
s216.solub['30°C'] = 'N/A'
s216.solub['40°C'] = 'N/A'
s216.solub['50°C'] = 'N/A'
s216.solub['60°C'] = 'N/A'
s216.solub['70°C'] = 'N/A'
s216.solub['80°C'] = 'N/A'
s216.solub['90°C'] = 'N/A'
s216.solub['100°C'] = 'N/A'
sublist.append(s216)

s217 = substance('Copper(II) hydroxide', 'Cu(OH)2')
s217.solub['0°C'] = 'N/A'
s217.solub['10°C'] = 'N/A'
s217.solub['20°C'] = '1.722×10-6'
s217.solub['30°C'] = 'N/A'
s217.solub['40°C'] = 'N/A'
s217.solub['50°C'] = 'N/A'
s217.solub['60°C'] = 'N/A'
s217.solub['70°C'] = 'N/A'
s217.solub['80°C'] = 'N/A'
s217.solub['90°C'] = 'N/A'
s217.solub['100°C'] = 'N/A'
sublist.append(s217)

s218 = substance('Copper(II) iodate', 'Cu(IO3)2.2H2O')
s218.solub['0°C'] = 'N/A'
s218.solub['10°C'] = 'N/A'
s218.solub['20°C'] = '0.109'
s218.solub['30°C'] = 'N/A'
s218.solub['40°C'] = 'N/A'
s218.solub['50°C'] = 'N/A'
s218.solub['60°C'] = 'N/A'
s218.solub['70°C'] = 'N/A'
s218.solub['80°C'] = 'N/A'
s218.solub['90°C'] = 'N/A'
s218.solub['100°C'] = 'N/A'
sublist.append(s218)

s219 = substance('Copper(II) nitrate', 'Cu(NO3)2')
s219.solub['0°C'] = '83.5'
s219.solub['10°C'] = '100'
s219.solub['20°C'] = '125'
s219.solub['30°C'] = '156'
s219.solub['40°C'] = '163'
s219.solub['50°C'] = 'N/A'
s219.solub['60°C'] = '182'
s219.solub['70°C'] = 'N/A'
s219.solub['80°C'] = '208'
s219.solub['90°C'] = '222'
s219.solub['100°C'] = '247'
sublist.append(s219)

s220 = substance('Copper oxalate', 'CuC2O4.2H2O')
s220.solub['0°C'] = 'N/A'
s220.solub['10°C'] = 'N/A'
s220.solub['20°C'] = '2.1627×10-10'
s220.solub['30°C'] = 'N/A'
s220.solub['40°C'] = 'N/A'
s220.solub['50°C'] = 'N/A'
s220.solub['60°C'] = 'N/A'
s220.solub['70°C'] = 'N/A'
s220.solub['80°C'] = 'N/A'
s220.solub['90°C'] = 'N/A'
s220.solub['100°C'] = 'N/A'
sublist.append(s220)

s221 = substance('Copper(II) perchlorate', 'Cu(ClO4)2')
s221.solub['0°C'] = 'N/A'
s221.solub['10°C'] = 'N/A'
s221.solub['20°C'] = 'N/A'
s221.solub['30°C'] = '146'
s221.solub['40°C'] = 'N/A'
s221.solub['50°C'] = 'N/A'
s221.solub['60°C'] = 'N/A'
s221.solub['70°C'] = 'N/A'
s221.solub['80°C'] = 'N/A'
s221.solub['90°C'] = 'N/A'
s221.solub['100°C'] = 'N/A'
sublist.append(s221)

s222 = substance('Copper(II) selenate', 'CuSeO4')
s222.solub['0°C'] = '12'
s222.solub['10°C'] = '14.5'
s222.solub['20°C'] = '17.5'
s222.solub['30°C'] = '21'
s222.solub['40°C'] = '25.2'
s222.solub['50°C'] = 'N/A'
s222.solub['60°C'] = '36.5'
s222.solub['70°C'] = 'N/A'
s222.solub['80°C'] = '53.7'
s222.solub['90°C'] = 'N/A'
s222.solub['100°C'] = 'N/A'
sublist.append(s222)

s223 = substance('Copper(II) selenite', 'CuSeO3')
s223.solub['0°C'] = 'N/A'
s223.solub['10°C'] = 'N/A'
s223.solub['20°C'] = '0.002761'
s223.solub['30°C'] = 'N/A'
s223.solub['40°C'] = 'N/A'
s223.solub['50°C'] = 'N/A'
s223.solub['60°C'] = 'N/A'
s223.solub['70°C'] = 'N/A'
s223.solub['80°C'] = 'N/A'
s223.solub['90°C'] = 'N/A'
s223.solub['100°C'] = 'N/A'
sublist.append(s223)

s224 = substance('Copper(II) sulfate', 'CuSO4.5H2O')
s224.solub['0°C'] = '23.1'
s224.solub['10°C'] = '27.5'
s224.solub['20°C'] = '32'
s224.solub['30°C'] = '37.8'
s224.solub['40°C'] = '44.6'
s224.solub['50°C'] = 'N/A'
s224.solub['60°C'] = '61.8'
s224.solub['70°C'] = 'N/A'
s224.solub['80°C'] = '83.8'
s224.solub['90°C'] = 'N/A'
s224.solub['100°C'] = '114'
sublist.append(s224)

s225 = substance('Copper(II) sulfide', 'CuS')
s225.solub['0°C'] = 'N/A'
s225.solub['10°C'] = 'N/A'
s225.solub['20°C'] = '2.41×10-17'
s225.solub['30°C'] = 'N/A'
s225.solub['40°C'] = 'N/A'
s225.solub['50°C'] = 'N/A'
s225.solub['60°C'] = 'N/A'
s225.solub['70°C'] = 'N/A'
s225.solub['80°C'] = 'N/A'
s225.solub['90°C'] = 'N/A'
s225.solub['100°C'] = 'N/A'
sublist.append(s225)

s226 = substance('Dysprosium(III) chromate', 'Dy2(CrO4)3.10H2O')
s226.solub['0°C'] = 'N/A'
s226.solub['10°C'] = 'N/A'
s226.solub['20°C'] = '0.663'
s226.solub['30°C'] = 'N/A'
s226.solub['40°C'] = 'N/A'
s226.solub['50°C'] = 'N/A'
s226.solub['60°C'] = 'N/A'
s226.solub['70°C'] = 'N/A'
s226.solub['80°C'] = 'N/A'
s226.solub['90°C'] = 'N/A'
s226.solub['100°C'] = 'N/A'
sublist.append(s226)

s227 = substance('Dysprosium(III) sulfate', 'Dy2(SO4)3.8H2O')
s227.solub['0°C'] = 'N/A'
s227.solub['10°C'] = 'N/A'
s227.solub['20°C'] = '4.83'
s227.solub['30°C'] = 'N/A'
s227.solub['40°C'] = 'N/A'
s227.solub['50°C'] = 'N/A'
s227.solub['60°C'] = 'N/A'
s227.solub['70°C'] = 'N/A'
s227.solub['80°C'] = 'N/A'
s227.solub['90°C'] = 'N/A'
s227.solub['100°C'] = 'N/A'
sublist.append(s227)

s228 = substance('Erbium(III) hydroxide', 'Er(OH)3')
s228.solub['0°C'] = 'N/A'
s228.solub['10°C'] = 'N/A'
s228.solub['20°C'] = '1.363×10-5'
s228.solub['30°C'] = 'N/A'
s228.solub['40°C'] = 'N/A'
s228.solub['50°C'] = 'N/A'
s228.solub['60°C'] = 'N/A'
s228.solub['70°C'] = 'N/A'
s228.solub['80°C'] = 'N/A'
s228.solub['90°C'] = 'N/A'
s228.solub['100°C'] = 'N/A'
sublist.append(s228)

s229 = substance('Erbium(III) sulfate', 'Er2(SO4)3')
s229.solub['0°C'] = 'N/A'
s229.solub['10°C'] = 'N/A'
s229.solub['20°C'] = '13.79'
s229.solub['30°C'] = 'N/A'
s229.solub['40°C'] = 'N/A'
s229.solub['50°C'] = 'N/A'
s229.solub['60°C'] = 'N/A'
s229.solub['70°C'] = 'N/A'
s229.solub['80°C'] = 'N/A'
s229.solub['90°C'] = 'N/A'
s229.solub['100°C'] = 'N/A'
sublist.append(s229)

s230 = substance('Erbium(III) sulfate octahydrate', 'Er2(SO4)3.8H2O')
s230.solub['0°C'] = 'N/A'
s230.solub['10°C'] = 'N/A'
s230.solub['20°C'] = '16.00'
s230.solub['30°C'] = 'N/A'
s230.solub['40°C'] = '6.53'
s230.solub['50°C'] = 'N/A'
s230.solub['60°C'] = 'N/A'
s230.solub['70°C'] = 'N/A'
s230.solub['80°C'] = 'N/A'
s230.solub['90°C'] = 'N/A'
s230.solub['100°C'] = 'N/A'
sublist.append(s230)

s231 = substance('Europium(III) hydroxide', 'Eu(OH)3')
s231.solub['0°C'] = 'N/A'
s231.solub['10°C'] = 'N/A'
s231.solub['20°C'] = '1.538×10-5'
s231.solub['30°C'] = 'N/A'
s231.solub['40°C'] = 'N/A'
s231.solub['50°C'] = 'N/A'
s231.solub['60°C'] = 'N/A'
s231.solub['70°C'] = 'N/A'
s231.solub['80°C'] = 'N/A'
s231.solub['90°C'] = 'N/A'
s231.solub['100°C'] = 'N/A'
sublist.append(s231)

s232 = substance('Europium(III) sulfate', 'Eu2(SO4)3.8H2O')
s232.solub['0°C'] = 'N/A'
s232.solub['10°C'] = 'N/A'
s232.solub['20°C'] = '2.56'
s232.solub['30°C'] = 'N/A'
s232.solub['40°C'] = 'N/A'
s232.solub['50°C'] = 'N/A'
s232.solub['60°C'] = 'N/A'
s232.solub['70°C'] = 'N/A'
s232.solub['80°C'] = 'N/A'
s232.solub['90°C'] = 'N/A'
s232.solub['100°C'] = 'N/A'
sublist.append(s232)

s233 = substance('Ferrous ammonium sulfate', '(NH4)2Fe(SO4)2.6H2O')
s233.solub['0°C'] = 'N/A'
s233.solub['10°C'] = 'N/A'
s233.solub['20°C'] = '26.9'
s233.solub['30°C'] = 'N/A'
s233.solub['40°C'] = 'N/A'
s233.solub['50°C'] = 'N/A'
s233.solub['60°C'] = 'N/A'
s233.solub['70°C'] = 'N/A'
s233.solub['80°C'] = '73'
s233.solub['90°C'] = 'N/A'
s233.solub['100°C'] = 'N/A'
sublist.append(s233)

s234 = substance('Fructose', 'C6H12O6')
s234.solub['0°C'] = 'N/A'
s234.solub['10°C'] = 'N/A'
s234.solub['20°C'] = '375.0'
s234.solub['30°C'] = 'N/A'
s234.solub['40°C'] = '538.0'
s234.solub['50°C'] = 'N/A'
s234.solub['60°C'] = 'N/A'
s234.solub['70°C'] = 'N/A'
s234.solub['80°C'] = 'N/A'
s234.solub['90°C'] = 'N/A'
s234.solub['100°C'] = 'N/A'
sublist.append(s234)

s235 = substance('Gadolinium(III) acetate', 'Gd(C2H3O2)3.4H2O')
s235.solub['0°C'] = 'N/A'
s235.solub['10°C'] = 'N/A'
s235.solub['20°C'] = '11.6'
s235.solub['30°C'] = 'N/A'
s235.solub['40°C'] = 'N/A'
s235.solub['50°C'] = 'N/A'
s235.solub['60°C'] = 'N/A'
s235.solub['70°C'] = 'N/A'
s235.solub['80°C'] = 'N/A'
s235.solub['90°C'] = 'N/A'
s235.solub['100°C'] = 'N/A'
sublist.append(s235)

s236 = substance('Gadolinium(III) bicarbonate', 'Gd(HCO3)3')
s236.solub['0°C'] = 'N/A'
s236.solub['10°C'] = 'N/A'
s236.solub['20°C'] = '5.61'
s236.solub['30°C'] = 'N/A'
s236.solub['40°C'] = 'N/A'
s236.solub['50°C'] = 'N/A'
s236.solub['60°C'] = 'N/A'
s236.solub['70°C'] = 'N/A'
s236.solub['80°C'] = 'N/A'
s236.solub['90°C'] = 'N/A'
s236.solub['100°C'] = 'N/A'
sublist.append(s236)

s237 = substance('Gadolinium(III) bromate', 'Gd(BrO3)3.9H2O')
s237.solub['0°C'] = '50.2'
s237.solub['10°C'] = '70.1'
s237.solub['20°C'] = '95.6'
s237.solub['30°C'] = '126'
s237.solub['40°C'] = '166'
s237.solub['50°C'] = 'N/A'
s237.solub['60°C'] = 'N/A'
s237.solub['70°C'] = 'N/A'
s237.solub['80°C'] = 'N/A'
s237.solub['90°C'] = 'N/A'
s237.solub['100°C'] = 'N/A'
sublist.append(s237)

s238 = substance('Gadolinium(III) hydroxide', 'Gd(OH)3')
s238.solub['0°C'] = 'N/A'
s238.solub['10°C'] = 'N/A'
s238.solub['20°C'] = '1.882×10-5'
s238.solub['30°C'] = 'N/A'
s238.solub['40°C'] = 'N/A'
s238.solub['50°C'] = 'N/A'
s238.solub['60°C'] = 'N/A'
s238.solub['70°C'] = 'N/A'
s238.solub['80°C'] = 'N/A'
s238.solub['90°C'] = 'N/A'
s238.solub['100°C'] = 'N/A'
sublist.append(s238)

s239 = substance('Gadolinium(III) sulfate', 'Gd2(SO4)3')
s239.solub['0°C'] = '3.98'
s239.solub['10°C'] = '3.3'
s239.solub['20°C'] = '2.6'
s239.solub['30°C'] = '2.32'
s239.solub['40°C'] = 'N/A'
s239.solub['50°C'] = 'N/A'
s239.solub['60°C'] = 'N/A'
s239.solub['70°C'] = 'N/A'
s239.solub['80°C'] = 'N/A'
s239.solub['90°C'] = 'N/A'
s239.solub['100°C'] = 'N/A'
sublist.append(s239)

s240 = substance('D-Galactose', 'C6H12O6')
s240.solub['0°C'] = 'N/A'
s240.solub['10°C'] = 'N/A'
s240.solub['20°C'] = '10.3'
s240.solub['30°C'] = 'N/A'
s240.solub['40°C'] = 'N/A'
s240.solub['50°C'] = 'N/A'
s240.solub['60°C'] = 'N/A'
s240.solub['70°C'] = 'N/A'
s240.solub['80°C'] = 'N/A'
s240.solub['90°C'] = 'N/A'
s240.solub['100°C'] = '68.3'
sublist.append(s240)

s241 = substance('Gallium hydroxide', 'Ga(OH)3')
s241.solub['0°C'] = 'N/A'
s241.solub['10°C'] = 'N/A'
s241.solub['20°C'] = '8.616×10-9'
s241.solub['30°C'] = 'N/A'
s241.solub['40°C'] = 'N/A'
s241.solub['50°C'] = 'N/A'
s241.solub['60°C'] = 'N/A'
s241.solub['70°C'] = 'N/A'
s241.solub['80°C'] = 'N/A'
s241.solub['90°C'] = 'N/A'
s241.solub['100°C'] = 'N/A'
sublist.append(s241)

s242 = substance('Gallium oxalate', 'Ga2(C2O4)3.42O')
s242.solub['0°C'] = 'N/A'
s242.solub['10°C'] = 'N/A'
s242.solub['20°C'] = '0.4'
s242.solub['30°C'] = 'N/A'
s242.solub['40°C'] = 'N/A'
s242.solub['50°C'] = 'N/A'
s242.solub['60°C'] = 'N/A'
s242.solub['70°C'] = 'N/A'
s242.solub['80°C'] = 'N/A'
s242.solub['90°C'] = 'N/A'
s242.solub['100°C'] = 'N/A'
sublist.append(s242)

s243 = substance('Gallium selenate', 'Ga2(SeO4)3.16H2O')
s243.solub['0°C'] = 'N/A'
s243.solub['10°C'] = 'N/A'
s243.solub['20°C'] = '18.1'
s243.solub['30°C'] = 'N/A'
s243.solub['40°C'] = 'N/A'
s243.solub['50°C'] = 'N/A'
s243.solub['60°C'] = 'N/A'
s243.solub['70°C'] = 'N/A'
s243.solub['80°C'] = 'N/A'
s243.solub['90°C'] = 'N/A'
s243.solub['100°C'] = 'N/A'
sublist.append(s243)

s244 = substance('D-Glucose', 'C6H12O6')
s244.solub['0°C'] = 'N/A'
s244.solub['10°C'] = 'N/A'
s244.solub['20°C'] = '90'
s244.solub['30°C'] = 'N/A'
s244.solub['40°C'] = 'N/A'
s244.solub['50°C'] = 'N/A'
s244.solub['60°C'] = 'N/A'
s244.solub['70°C'] = 'N/A'
s244.solub['80°C'] = 'N/A'
s244.solub['90°C'] = 'N/A'
s244.solub['100°C'] = 'N/A'
sublist.append(s244)

s245 = substance('Gold(III) chloride', 'AuCl3')
s245.solub['0°C'] = 'N/A'
s245.solub['10°C'] = 'N/A'
s245.solub['20°C'] = '68'
s245.solub['30°C'] = 'N/A'
s245.solub['40°C'] = 'N/A'
s245.solub['50°C'] = 'N/A'
s245.solub['60°C'] = 'N/A'
s245.solub['70°C'] = 'N/A'
s245.solub['80°C'] = 'N/A'
s245.solub['90°C'] = 'N/A'
s245.solub['100°C'] = 'N/A'
sublist.append(s245)

s246 = substance('Gold(V) oxalate', 'Au2(C2O4)5')
s246.solub['0°C'] = 'N/A'
s246.solub['10°C'] = 'N/A'
s246.solub['20°C'] = '0.258'
s246.solub['30°C'] = 'N/A'
s246.solub['40°C'] = 'N/A'
s246.solub['50°C'] = 'N/A'
s246.solub['60°C'] = 'N/A'
s246.solub['70°C'] = 'N/A'
s246.solub['80°C'] = 'N/A'
s246.solub['90°C'] = 'N/A'
s246.solub['100°C'] = 'N/A'
sublist.append(s246)

s247 = substance('Hafnium(III) hydroxide', 'Hf(OH)3')
s247.solub['0°C'] = 'N/A'
s247.solub['10°C'] = 'N/A'
s247.solub['20°C'] = '4.503×10-4'
s247.solub['30°C'] = 'N/A'
s247.solub['40°C'] = 'N/A'
s247.solub['50°C'] = 'N/A'
s247.solub['60°C'] = 'N/A'
s247.solub['70°C'] = 'N/A'
s247.solub['80°C'] = 'N/A'
s247.solub['90°C'] = 'N/A'
s247.solub['100°C'] = 'N/A'
sublist.append(s247)

s248 = substance('Hafnium(IV) hydroxide', 'Hf(OH)4')
s248.solub['0°C'] = 'N/A'
s248.solub['10°C'] = 'N/A'
s248.solub['20°C'] = '4.503×10-6'
s248.solub['30°C'] = 'N/A'
s248.solub['40°C'] = 'N/A'
s248.solub['50°C'] = 'N/A'
s248.solub['60°C'] = 'N/A'
s248.solub['70°C'] = 'N/A'
s248.solub['80°C'] = 'N/A'
s248.solub['90°C'] = 'N/A'
s248.solub['100°C'] = 'N/A'
sublist.append(s248)

s249 = substance('Helium', 'He')
s249.solub['0°C'] = 'N/A'
s249.solub['10°C'] = 'N/A'
s249.solub['20°C'] = '0.6'
s249.solub['30°C'] = 'N/A'
s249.solub['40°C'] = 'N/A'
s249.solub['50°C'] = 'N/A'
s249.solub['60°C'] = 'N/A'
s249.solub['70°C'] = 'N/A'
s249.solub['80°C'] = 'N/A'
s249.solub['90°C'] = 'N/A'
s249.solub['100°C'] = 'N/A'
sublist.append(s249)

s250 = substance('Holmium(III) hydroxide', 'Ho(OH)3')
s250.solub['0°C'] = 'N/A'
s250.solub['10°C'] = 'N/A'
s250.solub['20°C'] = '2.519×10-5'
s250.solub['30°C'] = 'N/A'
s250.solub['40°C'] = 'N/A'
s250.solub['50°C'] = 'N/A'
s250.solub['60°C'] = 'N/A'
s250.solub['70°C'] = 'N/A'
s250.solub['80°C'] = 'N/A'
s250.solub['90°C'] = 'N/A'
s250.solub['100°C'] = 'N/A'
sublist.append(s250)

s251 = substance('Holmium(III) sulfate', 'Ho2(SO4)3.8H2O')
s251.solub['0°C'] = 'N/A'
s251.solub['10°C'] = 'N/A'
s251.solub['20°C'] = '8.18'
s251.solub['30°C'] = '6.1'
s251.solub['40°C'] = '4.52'
s251.solub['50°C'] = 'N/A'
s251.solub['60°C'] = 'N/A'
s251.solub['70°C'] = 'N/A'
s251.solub['80°C'] = 'N/A'
s251.solub['90°C'] = 'N/A'
s251.solub['100°C'] = 'N/A'
sublist.append(s251)

s252 = substance('Hydrogen chloride', 'HCl')
s252.solub['0°C'] = '81'
s252.solub['10°C'] = '75'
s252.solub['20°C'] = '70'
s252.solub['30°C'] = '65.5'
s252.solub['40°C'] = '61'
s252.solub['50°C'] = '57.5'
s252.solub['60°C'] = '53'
s252.solub['70°C'] = '50'
s252.solub['80°C'] = '47'
s252.solub['90°C'] = '43'
s252.solub['100°C'] = '40'
sublist.append(s252)

s253 = substance('Hydrogen sulfide', 'H2S')
s253.solub['0°C'] = 'N/A'
s253.solub['10°C'] = 'N/A'
s253.solub['20°C'] = '0.33'
s253.solub['30°C'] = 'N/A'
s253.solub['40°C'] = 'N/A'
s253.solub['50°C'] = 'N/A'
s253.solub['60°C'] = 'N/A'
s253.solub['70°C'] = 'N/A'
s253.solub['80°C'] = 'N/A'
s253.solub['90°C'] = 'N/A'
s253.solub['100°C'] = 'N/A'
sublist.append(s253)

s254 = substance('Indium(III) bromide', 'InBr3')
s254.solub['0°C'] = 'N/A'
s254.solub['10°C'] = 'N/A'
s254.solub['20°C'] = '571'
s254.solub['30°C'] = 'N/A'
s254.solub['40°C'] = 'N/A'
s254.solub['50°C'] = 'N/A'
s254.solub['60°C'] = 'N/A'
s254.solub['70°C'] = 'N/A'
s254.solub['80°C'] = 'N/A'
s254.solub['90°C'] = 'N/A'
s254.solub['100°C'] = 'N/A'
sublist.append(s254)

s255 = substance('Indium(III) chloride', 'InCl3')
s255.solub['0°C'] = 'N/A'
s255.solub['10°C'] = '210'
s255.solub['20°C'] = '212'
s255.solub['30°C'] = 'N/A'
s255.solub['40°C'] = 'N/A'
s255.solub['50°C'] = 'N/A'
s255.solub['60°C'] = 'N/A'
s255.solub['70°C'] = 'N/A'
s255.solub['80°C'] = 'N/A'
s255.solub['90°C'] = 'N/A'
s255.solub['100°C'] = 'N/A'
sublist.append(s255)

s256 = substance('Indium(III) fluoride', 'InF3')
s256.solub['0°C'] = 'N/A'
s256.solub['10°C'] = 'N/A'
s256.solub['20°C'] = '11.2'
s256.solub['30°C'] = 'N/A'
s256.solub['40°C'] = 'N/A'
s256.solub['50°C'] = 'N/A'
s256.solub['60°C'] = 'N/A'
s256.solub['70°C'] = 'N/A'
s256.solub['80°C'] = 'N/A'
s256.solub['90°C'] = 'N/A'
s256.solub['100°C'] = 'N/A'
sublist.append(s256)

s257 = substance('Indium(III) hydroxide', 'In(OH)3')
s257.solub['0°C'] = 'N/A'
s257.solub['10°C'] = 'N/A'
s257.solub['20°C'] = '3.645×10-8'
s257.solub['30°C'] = 'N/A'
s257.solub['40°C'] = 'N/A'
s257.solub['50°C'] = 'N/A'
s257.solub['60°C'] = 'N/A'
s257.solub['70°C'] = 'N/A'
s257.solub['80°C'] = 'N/A'
s257.solub['90°C'] = 'N/A'
s257.solub['100°C'] = 'N/A'
sublist.append(s257)

s258 = substance('Indium(III) iodate', 'In(IO3)3')
s258.solub['0°C'] = 'N/A'
s258.solub['10°C'] = 'N/A'
s258.solub['20°C'] = '0.067'
s258.solub['30°C'] = 'N/A'
s258.solub['40°C'] = 'N/A'
s258.solub['50°C'] = 'N/A'
s258.solub['60°C'] = 'N/A'
s258.solub['70°C'] = 'N/A'
s258.solub['80°C'] = 'N/A'
s258.solub['90°C'] = 'N/A'
s258.solub['100°C'] = 'N/A'
sublist.append(s258)

s259 = substance('Indium(III) sulfide', 'In2S3')
s259.solub['0°C'] = 'N/A'
s259.solub['10°C'] = 'N/A'
s259.solub['20°C'] = '2.867×10-14'
s259.solub['30°C'] = 'N/A'
s259.solub['40°C'] = 'N/A'
s259.solub['50°C'] = 'N/A'
s259.solub['60°C'] = 'N/A'
s259.solub['70°C'] = 'N/A'
s259.solub['80°C'] = 'N/A'
s259.solub['90°C'] = 'N/A'
s259.solub['100°C'] = 'N/A'
sublist.append(s259)

s260 = substance('Iron(II) bromide', 'FeBr2')
s260.solub['0°C'] = '101'
s260.solub['10°C'] = '109'
s260.solub['20°C'] = '117'
s260.solub['30°C'] = '124'
s260.solub['40°C'] = '133'
s260.solub['50°C'] = 'N/A'
s260.solub['60°C'] = '144'
s260.solub['70°C'] = 'N/A'
s260.solub['80°C'] = '168'
s260.solub['90°C'] = '176'
s260.solub['100°C'] = '184'
sublist.append(s260)

s261 = substance('Iron(II) carbonate', 'FeCO3')
s261.solub['0°C'] = 'N/A'
s261.solub['10°C'] = 'N/A'
s261.solub['20°C'] = '6.554×10-5'
s261.solub['30°C'] = 'N/A'
s261.solub['40°C'] = 'N/A'
s261.solub['50°C'] = 'N/A'
s261.solub['60°C'] = 'N/A'
s261.solub['70°C'] = 'N/A'
s261.solub['80°C'] = 'N/A'
s261.solub['90°C'] = 'N/A'
s261.solub['100°C'] = 'N/A'
sublist.append(s261)

s262 = substance('Iron(II) chloride', 'FeCl2')
s262.solub['0°C'] = '49.7'
s262.solub['10°C'] = '59'
s262.solub['20°C'] = '62.5'
s262.solub['30°C'] = '66.7'
s262.solub['40°C'] = '70'
s262.solub['50°C'] = 'N/A'
s262.solub['60°C'] = '78.3'
s262.solub['70°C'] = 'N/A'
s262.solub['80°C'] = '88.7'
s262.solub['90°C'] = '92.3'
s262.solub['100°C'] = '94.9'
sublist.append(s262)

s263 = substance('Iron(II) fluorosilicate', 'FeSiF6.6H2O')
s263.solub['0°C'] = '72.1'
s263.solub['10°C'] = '74.4'
s263.solub['20°C'] = 'N/A'
s263.solub['30°C'] = '77'
s263.solub['40°C'] = 'N/A'
s263.solub['50°C'] = 'N/A'
s263.solub['60°C'] = '84'
s263.solub['70°C'] = 'N/A'
s263.solub['80°C'] = '88'
s263.solub['90°C'] = 'N/A'
s263.solub['100°C'] = '100'
sublist.append(s263)

s264 = substance('Iron(II) hydroxide', 'Fe(OH)2')
s264.solub['0°C'] = 'N/A'
s264.solub['10°C'] = 'N/A'
s264.solub['20°C'] = '5.255×10-5'
s264.solub['30°C'] = 'N/A'
s264.solub['40°C'] = 'N/A'
s264.solub['50°C'] = 'N/A'
s264.solub['60°C'] = 'N/A'
s264.solub['70°C'] = 'N/A'
s264.solub['80°C'] = 'N/A'
s264.solub['90°C'] = 'N/A'
s264.solub['100°C'] = 'N/A'
sublist.append(s264)

s265 = substance('Iron(II) nitrate', 'Fe(NO3)2.6H2O')
s265.solub['0°C'] = '113'
s265.solub['10°C'] = '134'
s265.solub['20°C'] = 'N/A'
s265.solub['30°C'] = 'N/A'
s265.solub['40°C'] = 'N/A'
s265.solub['50°C'] = 'N/A'
s265.solub['60°C'] = 'N/A'
s265.solub['70°C'] = 'N/A'
s265.solub['80°C'] = 'N/A'
s265.solub['90°C'] = 'N/A'
s265.solub['100°C'] = 'N/A'
sublist.append(s265)

s266 = substance('Iron(II) oxalate', 'FeC2O4.2H2O')
s266.solub['0°C'] = 'N/A'
s266.solub['10°C'] = 'N/A'
s266.solub['20°C'] = '0.008'
s266.solub['30°C'] = 'N/A'
s266.solub['40°C'] = 'N/A'
s266.solub['50°C'] = 'N/A'
s266.solub['60°C'] = 'N/A'
s266.solub['70°C'] = 'N/A'
s266.solub['80°C'] = 'N/A'
s266.solub['90°C'] = 'N/A'
s266.solub['100°C'] = 'N/A'
sublist.append(s266)

s267 = substance('Iron(II) perchlorate', 'Fe(ClO4)2.6H2O')
s267.solub['0°C'] = 'N/A'
s267.solub['10°C'] = 'N/A'
s267.solub['20°C'] = '299'
s267.solub['30°C'] = 'N/A'
s267.solub['40°C'] = 'N/A'
s267.solub['50°C'] = 'N/A'
s267.solub['60°C'] = 'N/A'
s267.solub['70°C'] = 'N/A'
s267.solub['80°C'] = 'N/A'
s267.solub['90°C'] = 'N/A'
s267.solub['100°C'] = 'N/A'
sublist.append(s267)

s268 = substance('Iron(II) sulfate', 'FeSO4')
s268.solub['0°C'] = 'N/A'
s268.solub['10°C'] = 'N/A'
s268.solub['20°C'] = '28.8'
s268.solub['30°C'] = 'N/A'
s268.solub['40°C'] = '40'
s268.solub['50°C'] = '48'
s268.solub['60°C'] = '60'
s268.solub['70°C'] = '73.3'
s268.solub['80°C'] = 'N/A'
s268.solub['90°C'] = '101'
s268.solub['100°C'] = '79.9'
sublist.append(s268)

s269 = substance('Iron(III) arsenate', 'FeAsO4')
s269.solub['0°C'] = 'N/A'
s269.solub['10°C'] = 'N/A'
s269.solub['20°C'] = '1.47×10-9'
s269.solub['30°C'] = 'N/A'
s269.solub['40°C'] = 'N/A'
s269.solub['50°C'] = 'N/A'
s269.solub['60°C'] = 'N/A'
s269.solub['70°C'] = 'N/A'
s269.solub['80°C'] = 'N/A'
s269.solub['90°C'] = 'N/A'
s269.solub['100°C'] = 'N/A'
sublist.append(s269)

s270 = substance('Iron(III) chloride', 'FeCl3.6H2O')
s270.solub['0°C'] = '74.4'
s270.solub['10°C'] = 'N/A'
s270.solub['20°C'] = '91.8'
s270.solub['30°C'] = '107'
s270.solub['40°C'] = 'N/A'
s270.solub['50°C'] = 'N/A'
s270.solub['60°C'] = 'N/A'
s270.solub['70°C'] = 'N/A'
s270.solub['80°C'] = 'N/A'
s270.solub['90°C'] = 'N/A'
s270.solub['100°C'] = 'N/A'
sublist.append(s270)

s271 = substance('Iron(III) fluoride', 'FeF3')
s271.solub['0°C'] = 'N/A'
s271.solub['10°C'] = 'N/A'
s271.solub['20°C'] = '0.091'
s271.solub['30°C'] = 'N/A'
s271.solub['40°C'] = 'N/A'
s271.solub['50°C'] = 'N/A'
s271.solub['60°C'] = 'N/A'
s271.solub['70°C'] = 'N/A'
s271.solub['80°C'] = 'N/A'
s271.solub['90°C'] = 'N/A'
s271.solub['100°C'] = 'N/A'
sublist.append(s271)

s272 = substance('Iron(III) hydroxide', 'Fe(OH)3')
s272.solub['0°C'] = 'N/A'
s272.solub['10°C'] = 'N/A'
s272.solub['20°C'] = '2.097×10-9'
s272.solub['30°C'] = 'N/A'
s272.solub['40°C'] = 'N/A'
s272.solub['50°C'] = 'N/A'
s272.solub['60°C'] = 'N/A'
s272.solub['70°C'] = 'N/A'
s272.solub['80°C'] = 'N/A'
s272.solub['90°C'] = 'N/A'
s272.solub['100°C'] = 'N/A'
sublist.append(s272)

s273 = substance('Iron(III) iodate', 'Fe(IO3)3')
s273.solub['0°C'] = 'N/A'
s273.solub['10°C'] = 'N/A'
s273.solub['20°C'] = '0.36'
s273.solub['30°C'] = 'N/A'
s273.solub['40°C'] = 'N/A'
s273.solub['50°C'] = 'N/A'
s273.solub['60°C'] = 'N/A'
s273.solub['70°C'] = 'N/A'
s273.solub['80°C'] = 'N/A'
s273.solub['90°C'] = 'N/A'
s273.solub['100°C'] = 'N/A'
sublist.append(s273)

s274 = substance('Iron(III) nitrate', 'Fe(NO3)3.9H2O')
s274.solub['0°C'] = '112'
s274.solub['10°C'] = 'N/A'
s274.solub['20°C'] = '138'
s274.solub['30°C'] = 'N/A'
s274.solub['40°C'] = '175'
s274.solub['50°C'] = 'N/A'
s274.solub['60°C'] = 'N/A'
s274.solub['70°C'] = 'N/A'
s274.solub['80°C'] = 'N/A'
s274.solub['90°C'] = 'N/A'
s274.solub['100°C'] = 'N/A'
sublist.append(s274)

s275 = substance('Iron(III) perchlorate', 'Fe(ClO4)3')
s275.solub['0°C'] = '289'
s275.solub['10°C'] = 'N/A'
s275.solub['20°C'] = '368'
s275.solub['30°C'] = '422'
s275.solub['40°C'] = '478'
s275.solub['50°C'] = 'N/A'
s275.solub['60°C'] = '772'
s275.solub['70°C'] = 'N/A'
s275.solub['80°C'] = 'N/A'
s275.solub['90°C'] = 'N/A'
s275.solub['100°C'] = 'N/A'
sublist.append(s275)

s276 = substance('Iron(III) sulfate', 'Fe2(SO4)3.9H2O')
s276.solub['0°C'] = 'N/A'
s276.solub['10°C'] = 'N/A'
s276.solub['20°C'] = 'N/A'
s276.solub['30°C'] = 'N/A'
s276.solub['40°C'] = 'N/A'
s276.solub['50°C'] = 'N/A'
s276.solub['60°C'] = 'N/A'
s276.solub['70°C'] = 'N/A'
s276.solub['80°C'] = 'N/A'
s276.solub['90°C'] = 'N/A'
s276.solub['100°C'] = 'N/A'
sublist.append(s276)

s277 = substance('Lactose', 'C12H22O11')
s277.solub['0°C'] = 'N/A'
s277.solub['10°C'] = 'N/A'
s277.solub['20°C'] = '8'
s277.solub['30°C'] = 'N/A'
s277.solub['40°C'] = 'N/A'
s277.solub['50°C'] = 'N/A'
s277.solub['60°C'] = 'N/A'
s277.solub['70°C'] = 'N/A'
s277.solub['80°C'] = 'N/A'
s277.solub['90°C'] = 'N/A'
s277.solub['100°C'] = 'N/A'
sublist.append(s277)

s278 = substance('Lanthanum(III) acetate', 'La(C2H3O2)3.H2O')
s278.solub['0°C'] = 'N/A'
s278.solub['10°C'] = 'N/A'
s278.solub['20°C'] = '16.9'
s278.solub['30°C'] = 'N/A'
s278.solub['40°C'] = 'N/A'
s278.solub['50°C'] = 'N/A'
s278.solub['60°C'] = 'N/A'
s278.solub['70°C'] = 'N/A'
s278.solub['80°C'] = 'N/A'
s278.solub['90°C'] = 'N/A'
s278.solub['100°C'] = 'N/A'
sublist.append(s278)

s279 = substance('Lanthanum(III) bromate', 'La(BrO3)3')
s279.solub['0°C'] = '98'
s279.solub['10°C'] = '120'
s279.solub['20°C'] = '149'
s279.solub['30°C'] = '200'
s279.solub['40°C'] = 'N/A'
s279.solub['50°C'] = 'N/A'
s279.solub['60°C'] = 'N/A'
s279.solub['70°C'] = 'N/A'
s279.solub['80°C'] = 'N/A'
s279.solub['90°C'] = 'N/A'
s279.solub['100°C'] = 'N/A'
sublist.append(s279)

s280 = substance('Lanthanum(III) iodate', 'La(IO3)3')
s280.solub['0°C'] = 'N/A'
s280.solub['10°C'] = 'N/A'
s280.solub['20°C'] = '0.04575'
s280.solub['30°C'] = 'N/A'
s280.solub['40°C'] = 'N/A'
s280.solub['50°C'] = 'N/A'
s280.solub['60°C'] = 'N/A'
s280.solub['70°C'] = 'N/A'
s280.solub['80°C'] = 'N/A'
s280.solub['90°C'] = 'N/A'
s280.solub['100°C'] = 'N/A'
sublist.append(s280)

s281 = substance('Lanthanum(III) molybdate', 'La2(MoO4)3')
s281.solub['0°C'] = 'N/A'
s281.solub['10°C'] = 'N/A'
s281.solub['20°C'] = '0.002473'
s281.solub['30°C'] = 'N/A'
s281.solub['40°C'] = 'N/A'
s281.solub['50°C'] = 'N/A'
s281.solub['60°C'] = 'N/A'
s281.solub['70°C'] = 'N/A'
s281.solub['80°C'] = 'N/A'
s281.solub['90°C'] = 'N/A'
s281.solub['100°C'] = 'N/A'
sublist.append(s281)

s282 = substance('Lanthanum(III) nitrate', 'La(NO3)3')
s282.solub['0°C'] = '100'
s282.solub['10°C'] = 'N/A'
s282.solub['20°C'] = '136'
s282.solub['30°C'] = 'N/A'
s282.solub['40°C'] = '168'
s282.solub['50°C'] = 'N/A'
s282.solub['60°C'] = '247'
s282.solub['70°C'] = 'N/A'
s282.solub['80°C'] = 'N/A'
s282.solub['90°C'] = 'N/A'
s282.solub['100°C'] = 'N/A'
sublist.append(s282)

s283 = substance('Lanthanum(III) selenate', 'La2(SeO4)3')
s283.solub['0°C'] = '50.5'
s283.solub['10°C'] = '45'
s283.solub['20°C'] = '45'
s283.solub['30°C'] = '45'
s283.solub['40°C'] = '45'
s283.solub['50°C'] = 'N/A'
s283.solub['60°C'] = '18.5'
s283.solub['70°C'] = 'N/A'
s283.solub['80°C'] = '5.4'
s283.solub['90°C'] = '2.2'
s283.solub['100°C'] = 'N/A'
sublist.append(s283)

s284 = substance('Lanthanum(III) sulfate', 'La2(SO4)3')
s284.solub['0°C'] = '3'
s284.solub['10°C'] = '2.72'
s284.solub['20°C'] = '2.33'
s284.solub['30°C'] = '1.9'
s284.solub['40°C'] = '1.67'
s284.solub['50°C'] = 'N/A'
s284.solub['60°C'] = '1.26'
s284.solub['70°C'] = 'N/A'
s284.solub['80°C'] = '0.91'
s284.solub['90°C'] = '0.79'
s284.solub['100°C'] = '0.68'
sublist.append(s284)

s285 = substance('Lanthanum(III) tungstate', 'La2(WO4)3.3H2O')
s285.solub['0°C'] = 'N/A'
s285.solub['10°C'] = 'N/A'
s285.solub['20°C'] = '6.06'
s285.solub['30°C'] = 'N/A'
s285.solub['40°C'] = 'N/A'
s285.solub['50°C'] = 'N/A'
s285.solub['60°C'] = 'N/A'
s285.solub['70°C'] = 'N/A'
s285.solub['80°C'] = 'N/A'
s285.solub['90°C'] = 'N/A'
s285.solub['100°C'] = 'N/A'
sublist.append(s285)

s286 = substance('Lead(II) acetate', 'Pb(C2H3O2)2')
s286.solub['0°C'] = '19.8'
s286.solub['10°C'] = '29.5'
s286.solub['20°C'] = '44.3'
s286.solub['30°C'] = '69.8'
s286.solub['40°C'] = '116'
s286.solub['50°C'] = 'N/A'
s286.solub['60°C'] = 'N/A'
s286.solub['70°C'] = 'N/A'
s286.solub['80°C'] = 'N/A'
s286.solub['90°C'] = 'N/A'
s286.solub['100°C'] = 'N/A'
sublist.append(s286)

s287 = substance('Lead(II) azide', 'Pb(N3)2')
s287.solub['0°C'] = 'N/A'
s287.solub['10°C'] = 'N/A'
s287.solub['20°C'] = '0.0249'
s287.solub['30°C'] = 'N/A'
s287.solub['40°C'] = 'N/A'
s287.solub['50°C'] = 'N/A'
s287.solub['60°C'] = 'N/A'
s287.solub['70°C'] = 'N/A'
s287.solub['80°C'] = 'N/A'
s287.solub['90°C'] = 'N/A'
s287.solub['100°C'] = 'N/A'
sublist.append(s287)

s288 = substance('Lead(II) bromate', 'Pb(BrO3)2')
s288.solub['0°C'] = 'N/A'
s288.solub['10°C'] = 'N/A'
s288.solub['20°C'] = '7.92'
s288.solub['30°C'] = 'N/A'
s288.solub['40°C'] = 'N/A'
s288.solub['50°C'] = 'N/A'
s288.solub['60°C'] = 'N/A'
s288.solub['70°C'] = 'N/A'
s288.solub['80°C'] = 'N/A'
s288.solub['90°C'] = 'N/A'
s288.solub['100°C'] = 'N/A'
sublist.append(s288)

s289 = substance('Lead(II) bromide', 'PbBr2')
s289.solub['0°C'] = '0.45'
s289.solub['10°C'] = '0.63'
s289.solub['20°C'] = '0.973'
s289.solub['30°C'] = '1.12'
s289.solub['40°C'] = '1.5'
s289.solub['50°C'] = 'N/A'
s289.solub['60°C'] = '2.29'
s289.solub['70°C'] = 'N/A'
s289.solub['80°C'] = '3.32'
s289.solub['90°C'] = '3.86'
s289.solub['100°C'] = '4.55'
sublist.append(s289)

s290 = substance('Lead(II) carbonate', 'PbCO3')
s290.solub['0°C'] = 'N/A'
s290.solub['10°C'] = 'N/A'
s290.solub['20°C'] = '7.269×10-5'
s290.solub['30°C'] = 'N/A'
s290.solub['40°C'] = 'N/A'
s290.solub['50°C'] = 'N/A'
s290.solub['60°C'] = 'N/A'
s290.solub['70°C'] = 'N/A'
s290.solub['80°C'] = 'N/A'
s290.solub['90°C'] = 'N/A'
s290.solub['100°C'] = 'N/A'
sublist.append(s290)

s291 = substance('Lead(II) chlorate', 'Pb(ClO3)2')
s291.solub['0°C'] = 'N/A'
s291.solub['10°C'] = 'N/A'
s291.solub['20°C'] = '144'
s291.solub['30°C'] = 'N/A'
s291.solub['40°C'] = 'N/A'
s291.solub['50°C'] = 'N/A'
s291.solub['60°C'] = 'N/A'
s291.solub['70°C'] = 'N/A'
s291.solub['80°C'] = 'N/A'
s291.solub['90°C'] = 'N/A'
s291.solub['100°C'] = 'N/A'
sublist.append(s291)

s292 = substance('Lead(II) chloride', 'PbCl2')
s292.solub['0°C'] = '0.67'
s292.solub['10°C'] = '0.82'
s292.solub['20°C'] = '1.08'
s292.solub['30°C'] = '1.2'
s292.solub['40°C'] = '1.42'
s292.solub['50°C'] = 'N/A'
s292.solub['60°C'] = '1.94'
s292.solub['70°C'] = 'N/A'
s292.solub['80°C'] = '2.54'
s292.solub['90°C'] = '2.88'
s292.solub['100°C'] = '3.2'
sublist.append(s292)

s293 = substance('Lead(II) chromate', 'PbCrO4')
s293.solub['0°C'] = 'N/A'
s293.solub['10°C'] = 'N/A'
s293.solub['20°C'] = '1.71×10-5'
s293.solub['30°C'] = 'N/A'
s293.solub['40°C'] = 'N/A'
s293.solub['50°C'] = 'N/A'
s293.solub['60°C'] = 'N/A'
s293.solub['70°C'] = 'N/A'
s293.solub['80°C'] = 'N/A'
s293.solub['90°C'] = 'N/A'
s293.solub['100°C'] = 'N/A'
sublist.append(s293)

s294 = substance('Lead(II) ferrocyanide', 'PbFe(CN)6')
s294.solub['0°C'] = 'N/A'
s294.solub['10°C'] = 'N/A'
s294.solub['20°C'] = '5.991×10-4'
s294.solub['30°C'] = 'N/A'
s294.solub['40°C'] = 'N/A'
s294.solub['50°C'] = 'N/A'
s294.solub['60°C'] = 'N/A'
s294.solub['70°C'] = 'N/A'
s294.solub['80°C'] = 'N/A'
s294.solub['90°C'] = 'N/A'
s294.solub['100°C'] = 'N/A'
sublist.append(s294)

s295 = substance('Lead(II) fluoride', 'PbF2')
s295.solub['0°C'] = 'N/A'
s295.solub['10°C'] = 'N/A'
s295.solub['20°C'] = '0.0671'
s295.solub['30°C'] = 'N/A'
s295.solub['40°C'] = 'N/A'
s295.solub['50°C'] = 'N/A'
s295.solub['60°C'] = 'N/A'
s295.solub['70°C'] = 'N/A'
s295.solub['80°C'] = 'N/A'
s295.solub['90°C'] = 'N/A'
s295.solub['100°C'] = 'N/A'
sublist.append(s295)

s296 = substance('Lead(II) fluorosilicate', 'PbSiF6')
s296.solub['0°C'] = '190'
s296.solub['10°C'] = 'N/A'
s296.solub['20°C'] = '222'
s296.solub['30°C'] = 'N/A'
s296.solub['40°C'] = 'N/A'
s296.solub['50°C'] = 'N/A'
s296.solub['60°C'] = '403'
s296.solub['70°C'] = 'N/A'
s296.solub['80°C'] = '428'
s296.solub['90°C'] = 'N/A'
s296.solub['100°C'] = '463'
sublist.append(s296)

s297 = substance('Lead(II) hydrogen phosphate', 'PbHPO4')
s297.solub['0°C'] = 'N/A'
s297.solub['10°C'] = 'N/A'
s297.solub['20°C'] = '3.457×10-4'
s297.solub['30°C'] = 'N/A'
s297.solub['40°C'] = 'N/A'
s297.solub['50°C'] = 'N/A'
s297.solub['60°C'] = 'N/A'
s297.solub['70°C'] = 'N/A'
s297.solub['80°C'] = 'N/A'
s297.solub['90°C'] = 'N/A'
s297.solub['100°C'] = 'N/A'
sublist.append(s297)

s298 = substance('Lead(II) hydrogen phosphite', 'PbHPO3')
s298.solub['0°C'] = 'N/A'
s298.solub['10°C'] = 'N/A'
s298.solub['20°C'] = '0.02187'
s298.solub['30°C'] = 'N/A'
s298.solub['40°C'] = 'N/A'
s298.solub['50°C'] = 'N/A'
s298.solub['60°C'] = 'N/A'
s298.solub['70°C'] = 'N/A'
s298.solub['80°C'] = 'N/A'
s298.solub['90°C'] = 'N/A'
s298.solub['100°C'] = 'N/A'
sublist.append(s298)

s299 = substance('Lead(II) hydroxide', 'Pb(OH)2')
s299.solub['0°C'] = 'N/A'
s299.solub['10°C'] = 'N/A'
s299.solub['20°C'] = '1.615×10-4'
s299.solub['30°C'] = 'N/A'
s299.solub['40°C'] = 'N/A'
s299.solub['50°C'] = 'N/A'
s299.solub['60°C'] = 'N/A'
s299.solub['70°C'] = 'N/A'
s299.solub['80°C'] = 'N/A'
s299.solub['90°C'] = 'N/A'
s299.solub['100°C'] = 'N/A'
sublist.append(s299)

s300 = substance('Lead(II) iodate', 'Pb(IO3)2')
s300.solub['0°C'] = 'N/A'
s300.solub['10°C'] = 'N/A'
s300.solub['20°C'] = '0.0024'
s300.solub['30°C'] = 'N/A'
s300.solub['40°C'] = 'N/A'
s300.solub['50°C'] = 'N/A'
s300.solub['60°C'] = 'N/A'
s300.solub['70°C'] = 'N/A'
s300.solub['80°C'] = 'N/A'
s300.solub['90°C'] = 'N/A'
s300.solub['100°C'] = 'N/A'
sublist.append(s300)

s301 = substance('Lead(II) iodide', 'PbI2')
s301.solub['0°C'] = '0.044'
s301.solub['10°C'] = '0.056'
s301.solub['20°C'] = '0.0756'
s301.solub['30°C'] = '0.09'
s301.solub['40°C'] = '0.124'
s301.solub['50°C'] = 'N/A'
s301.solub['60°C'] = '0.193'
s301.solub['70°C'] = 'N/A'
s301.solub['80°C'] = '0.294'
s301.solub['90°C'] = 'N/A'
s301.solub['100°C'] = '0.42'
sublist.append(s301)

s302 = substance('Lead(II) molybdate', 'PbMoO4')
s302.solub['0°C'] = 'N/A'
s302.solub['10°C'] = 'N/A'
s302.solub['20°C'] = '1.161×10-5'
s302.solub['30°C'] = 'N/A'
s302.solub['40°C'] = 'N/A'
s302.solub['50°C'] = 'N/A'
s302.solub['60°C'] = 'N/A'
s302.solub['70°C'] = 'N/A'
s302.solub['80°C'] = 'N/A'
s302.solub['90°C'] = 'N/A'
s302.solub['100°C'] = 'N/A'
sublist.append(s302)

s303 = substance('Lead(II) nitrate', 'Pb(NO3)2')
s303.solub['0°C'] = '37.5'
s303.solub['10°C'] = '46.2'
s303.solub['20°C'] = '54.3'
s303.solub['30°C'] = '63.4'
s303.solub['40°C'] = '72.1'
s303.solub['50°C'] = 'N/A'
s303.solub['60°C'] = '91.6'
s303.solub['70°C'] = 'N/A'
s303.solub['80°C'] = '111'
s303.solub['90°C'] = 'N/A'
s303.solub['100°C'] = '133'
sublist.append(s303)

s304 = substance('Lead(II) oxalate', 'PbC2O4')
s304.solub['0°C'] = 'N/A'
s304.solub['10°C'] = 'N/A'
s304.solub['20°C'] = '6.495×10-4'
s304.solub['30°C'] = 'N/A'
s304.solub['40°C'] = 'N/A'
s304.solub['50°C'] = 'N/A'
s304.solub['60°C'] = 'N/A'
s304.solub['70°C'] = 'N/A'
s304.solub['80°C'] = 'N/A'
s304.solub['90°C'] = 'N/A'
s304.solub['100°C'] = 'N/A'
sublist.append(s304)

s305 = substance('Lead(II) perchlorate', 'Pb(ClO4)2.3H2O')
s305.solub['0°C'] = 'N/A'
s305.solub['10°C'] = 'N/A'
s305.solub['20°C'] = '440'
s305.solub['30°C'] = 'N/A'
s305.solub['40°C'] = 'N/A'
s305.solub['50°C'] = 'N/A'
s305.solub['60°C'] = 'N/A'
s305.solub['70°C'] = 'N/A'
s305.solub['80°C'] = 'N/A'
s305.solub['90°C'] = 'N/A'
s305.solub['100°C'] = 'N/A'
sublist.append(s305)

s306 = substance('Lead(II) selenate', 'PbSeO4')
s306.solub['0°C'] = 'N/A'
s306.solub['10°C'] = 'N/A'
s306.solub['20°C'] = '0.0131'
s306.solub['30°C'] = 'N/A'
s306.solub['40°C'] = 'N/A'
s306.solub['50°C'] = 'N/A'
s306.solub['60°C'] = 'N/A'
s306.solub['70°C'] = 'N/A'
s306.solub['80°C'] = 'N/A'
s306.solub['90°C'] = 'N/A'
s306.solub['100°C'] = 'N/A'
sublist.append(s306)

s307 = substance('Lead(II) sulfate', 'PbSO4')
s307.solub['0°C'] = 'N/A'
s307.solub['10°C'] = 'N/A'
s307.solub['20°C'] = '0.00443'
s307.solub['30°C'] = 'N/A'
s307.solub['40°C'] = 'N/A'
s307.solub['50°C'] = 'N/A'
s307.solub['60°C'] = 'N/A'
s307.solub['70°C'] = 'N/A'
s307.solub['80°C'] = 'N/A'
s307.solub['90°C'] = 'N/A'
s307.solub['100°C'] = 'N/A'
sublist.append(s307)

s308 = substance('Lead(II) sulfide', 'PbS')
s308.solub['0°C'] = 'N/A'
s308.solub['10°C'] = 'N/A'
s308.solub['20°C'] = '6.767×10-13'
s308.solub['30°C'] = 'N/A'
s308.solub['40°C'] = 'N/A'
s308.solub['50°C'] = 'N/A'
s308.solub['60°C'] = 'N/A'
s308.solub['70°C'] = 'N/A'
s308.solub['80°C'] = 'N/A'
s308.solub['90°C'] = 'N/A'
s308.solub['100°C'] = 'N/A'
sublist.append(s308)

s309 = substance('Lead(II) tartrate', 'PbC4H4O6')
s309.solub['0°C'] = 'N/A'
s309.solub['10°C'] = 'N/A'
s309.solub['20°C'] = '0.0025'
s309.solub['30°C'] = 'N/A'
s309.solub['40°C'] = 'N/A'
s309.solub['50°C'] = 'N/A'
s309.solub['60°C'] = 'N/A'
s309.solub['70°C'] = 'N/A'
s309.solub['80°C'] = 'N/A'
s309.solub['90°C'] = 'N/A'
s309.solub['100°C'] = 'N/A'
sublist.append(s309)

s310 = substance('Lead(II) thiocyanate', 'Pb(SCN)2')
s310.solub['0°C'] = 'N/A'
s310.solub['10°C'] = 'N/A'
s310.solub['20°C'] = '0.553'
s310.solub['30°C'] = 'N/A'
s310.solub['40°C'] = 'N/A'
s310.solub['50°C'] = 'N/A'
s310.solub['60°C'] = 'N/A'
s310.solub['70°C'] = 'N/A'
s310.solub['80°C'] = 'N/A'
s310.solub['90°C'] = 'N/A'
s310.solub['100°C'] = 'N/A'
sublist.append(s310)

s311 = substance('Lead(II) thiosulfate', 'PbS2O3')
s311.solub['0°C'] = 'N/A'
s311.solub['10°C'] = 'N/A'
s311.solub['20°C'] = '0.0202'
s311.solub['30°C'] = 'N/A'
s311.solub['40°C'] = 'N/A'
s311.solub['50°C'] = 'N/A'
s311.solub['60°C'] = 'N/A'
s311.solub['70°C'] = 'N/A'
s311.solub['80°C'] = 'N/A'
s311.solub['90°C'] = 'N/A'
s311.solub['100°C'] = 'N/A'
sublist.append(s311)

s312 = substance('Lead(II) tungstate', 'PbWO4')
s312.solub['0°C'] = 'N/A'
s312.solub['10°C'] = 'N/A'
s312.solub['20°C'] = '0.02838'
s312.solub['30°C'] = 'N/A'
s312.solub['40°C'] = 'N/A'
s312.solub['50°C'] = 'N/A'
s312.solub['60°C'] = 'N/A'
s312.solub['70°C'] = 'N/A'
s312.solub['80°C'] = 'N/A'
s312.solub['90°C'] = 'N/A'
s312.solub['100°C'] = 'N/A'
sublist.append(s312)

s313 = substance('Lead(IV) hydroxide', 'Pb(OH)4')
s313.solub['0°C'] = 'N/A'
s313.solub['10°C'] = 'N/A'
s313.solub['20°C'] = '7.229×10-11'
s313.solub['30°C'] = 'N/A'
s313.solub['40°C'] = 'N/A'
s313.solub['50°C'] = 'N/A'
s313.solub['60°C'] = 'N/A'
s313.solub['70°C'] = 'N/A'
s313.solub['80°C'] = 'N/A'
s313.solub['90°C'] = 'N/A'
s313.solub['100°C'] = 'N/A'
sublist.append(s313)

s314 = substance('Lithium acetate', 'LiC2H3O2')
s314.solub['0°C'] = '31.2'
s314.solub['10°C'] = '35.1'
s314.solub['20°C'] = '40.8'
s314.solub['30°C'] = '50.6'
s314.solub['40°C'] = '68.6'
s314.solub['50°C'] = 'N/A'
s314.solub['60°C'] = 'N/A'
s314.solub['70°C'] = 'N/A'
s314.solub['80°C'] = 'N/A'
s314.solub['90°C'] = 'N/A'
s314.solub['100°C'] = 'N/A'
sublist.append(s314)

s315 = substance('Lithium azide', 'LiN3')
s315.solub['0°C'] = '61.3'
s315.solub['10°C'] = '64.2'
s315.solub['20°C'] = '67.2'
s315.solub['30°C'] = '71.2'
s315.solub['40°C'] = '75.4'
s315.solub['50°C'] = 'N/A'
s315.solub['60°C'] = '86.6'
s315.solub['70°C'] = 'N/A'
s315.solub['80°C'] = 'N/A'
s315.solub['90°C'] = 'N/A'
s315.solub['100°C'] = '100'
sublist.append(s315)

s316 = substance('Lithium benzoate', 'LiC7H5O2')
s316.solub['0°C'] = '38.9'
s316.solub['10°C'] = '41.6'
s316.solub['20°C'] = '44.7'
s316.solub['30°C'] = '53.8'
s316.solub['40°C'] = 'N/A'
s316.solub['50°C'] = 'N/A'
s316.solub['60°C'] = 'N/A'
s316.solub['70°C'] = 'N/A'
s316.solub['80°C'] = 'N/A'
s316.solub['90°C'] = 'N/A'
s316.solub['100°C'] = 'N/A'
sublist.append(s316)

s317 = substance('Lithium bicarbonate', 'LiHCO3')
s317.solub['0°C'] = 'N/A'
s317.solub['10°C'] = 'N/A'
s317.solub['20°C'] = '5.74'
s317.solub['30°C'] = 'N/A'
s317.solub['40°C'] = 'N/A'
s317.solub['50°C'] = 'N/A'
s317.solub['60°C'] = 'N/A'
s317.solub['70°C'] = 'N/A'
s317.solub['80°C'] = 'N/A'
s317.solub['90°C'] = 'N/A'
s317.solub['100°C'] = 'N/A'
sublist.append(s317)

s318 = substance('Lithium bromate', 'LiBrO3')
s318.solub['0°C'] = '154'
s318.solub['10°C'] = '166'
s318.solub['20°C'] = '179'
s318.solub['30°C'] = '198'
s318.solub['40°C'] = '221'
s318.solub['50°C'] = 'N/A'
s318.solub['60°C'] = '269'
s318.solub['70°C'] = 'N/A'
s318.solub['80°C'] = '308'
s318.solub['90°C'] = '329'
s318.solub['100°C'] = '355'
sublist.append(s318)

s319 = substance('Lithium bromide', 'LiBr')
s319.solub['0°C'] = '143'
s319.solub['10°C'] = '147'
s319.solub['20°C'] = '160'
s319.solub['30°C'] = '183'
s319.solub['40°C'] = '211'
s319.solub['50°C'] = 'N/A'
s319.solub['60°C'] = '223'
s319.solub['70°C'] = 'N/A'
s319.solub['80°C'] = '245'
s319.solub['90°C'] = 'N/A'
s319.solub['100°C'] = '266'
sublist.append(s319)

s320 = substance('Lithium carbonate', 'Li2CO3')
s320.solub['0°C'] = '1.54'
s320.solub['10°C'] = '1.43'
s320.solub['20°C'] = '1.33'
s320.solub['30°C'] = '1.26'
s320.solub['40°C'] = '1.17'
s320.solub['50°C'] = 'N/A'
s320.solub['60°C'] = '1.01'
s320.solub['70°C'] = 'N/A'
s320.solub['80°C'] = '0.85'
s320.solub['90°C'] = 'N/A'
s320.solub['100°C'] = '0.72'
sublist.append(s320)

s321 = substance('Lithium chlorate', 'LiClO3')
s321.solub['0°C'] = '241'
s321.solub['10°C'] = '283'
s321.solub['20°C'] = '372'
s321.solub['30°C'] = '488'
s321.solub['40°C'] = '604'
s321.solub['50°C'] = 'N/A'
s321.solub['60°C'] = '777'
s321.solub['70°C'] = 'N/A'
s321.solub['80°C'] = 'N/A'
s321.solub['90°C'] = 'N/A'
s321.solub['100°C'] = 'N/A'
sublist.append(s321)

s322 = substance('Lithium chloride', 'LiCl')
s322.solub['0°C'] = '69.2'
s322.solub['10°C'] = '74.5'
s322.solub['20°C'] = '83.5'
s322.solub['30°C'] = '86.2'
s322.solub['40°C'] = '89.8'
s322.solub['50°C'] = 'N/A'
s322.solub['60°C'] = '98.4'
s322.solub['70°C'] = 'N/A'
s322.solub['80°C'] = '112'
s322.solub['90°C'] = '121'
s322.solub['100°C'] = '128'
sublist.append(s322)

s323 = substance('Lithium chromate', 'Li2CrO4.2H2O')
s323.solub['0°C'] = 'N/A'
s323.solub['10°C'] = 'N/A'
s323.solub['20°C'] = '142'
s323.solub['30°C'] = 'N/A'
s323.solub['40°C'] = 'N/A'
s323.solub['50°C'] = 'N/A'
s323.solub['60°C'] = 'N/A'
s323.solub['70°C'] = 'N/A'
s323.solub['80°C'] = 'N/A'
s323.solub['90°C'] = 'N/A'
s323.solub['100°C'] = 'N/A'
sublist.append(s323)

s324 = substance('Lithium dichromate', 'Li2Cr2O7.2H2O')
s324.solub['0°C'] = 'N/A'
s324.solub['10°C'] = 'N/A'
s324.solub['20°C'] = 'N/A'
s324.solub['30°C'] = '151'
s324.solub['40°C'] = 'N/A'
s324.solub['50°C'] = 'N/A'
s324.solub['60°C'] = 'N/A'
s324.solub['70°C'] = 'N/A'
s324.solub['80°C'] = 'N/A'
s324.solub['90°C'] = 'N/A'
s324.solub['100°C'] = 'N/A'
sublist.append(s324)

s325 = substance('Lithium dihydrogen phosphate', 'LiH2PO4')
s325.solub['0°C'] = '126'
s325.solub['10°C'] = 'N/A'
s325.solub['20°C'] = 'N/A'
s325.solub['30°C'] = 'N/A'
s325.solub['40°C'] = 'N/A'
s325.solub['50°C'] = 'N/A'
s325.solub['60°C'] = 'N/A'
s325.solub['70°C'] = 'N/A'
s325.solub['80°C'] = 'N/A'
s325.solub['90°C'] = 'N/A'
s325.solub['100°C'] = 'N/A'
sublist.append(s325)

s326 = substance('Lithium fluoride', 'LiF')
s326.solub['0°C'] = 'N/A'
s326.solub['10°C'] = 'N/A'
s326.solub['20°C'] = '0.27'
s326.solub['30°C'] = '0.135'
s326.solub['40°C'] = 'N/A'
s326.solub['50°C'] = 'N/A'
s326.solub['60°C'] = 'N/A'
s326.solub['70°C'] = 'N/A'
s326.solub['80°C'] = 'N/A'
s326.solub['90°C'] = 'N/A'
s326.solub['100°C'] = 'N/A'
sublist.append(s326)

s327 = substance('Lithium fluorosilicate', 'Li2SiF6.2H2O')
s327.solub['0°C'] = 'N/A'
s327.solub['10°C'] = 'N/A'
s327.solub['20°C'] = '73'
s327.solub['30°C'] = 'N/A'
s327.solub['40°C'] = 'N/A'
s327.solub['50°C'] = 'N/A'
s327.solub['60°C'] = 'N/A'
s327.solub['70°C'] = 'N/A'
s327.solub['80°C'] = 'N/A'
s327.solub['90°C'] = 'N/A'
s327.solub['100°C'] = 'N/A'
sublist.append(s327)

s328 = substance('Lithium formate', 'LiHCO2')
s328.solub['0°C'] = '32.3'
s328.solub['10°C'] = '35.7'
s328.solub['20°C'] = '39.3'
s328.solub['30°C'] = '44.1'
s328.solub['40°C'] = '49.5'
s328.solub['50°C'] = 'N/A'
s328.solub['60°C'] = '64.7'
s328.solub['70°C'] = 'N/A'
s328.solub['80°C'] = '92.7'
s328.solub['90°C'] = '116'
s328.solub['100°C'] = '138'
sublist.append(s328)

s329 = substance('Lithium hydrogen phosphite', 'Li2HPO3')
s329.solub['0°C'] = '4.43'
s329.solub['10°C'] = 'N/A'
s329.solub['20°C'] = 'N/A'
s329.solub['30°C'] = '9.97'
s329.solub['40°C'] = '7.61'
s329.solub['50°C'] = 'N/A'
s329.solub['60°C'] = '7.11'
s329.solub['70°C'] = 'N/A'
s329.solub['80°C'] = 'N/A'
s329.solub['90°C'] = 'N/A'
s329.solub['100°C'] = '6.03'
sublist.append(s329)

s330 = substance('Lithium hydroxide', 'LiOH')
s330.solub['0°C'] = '12.7'
s330.solub['10°C'] = '12.7'
s330.solub['20°C'] = '12.8'
s330.solub['30°C'] = '12.9'
s330.solub['40°C'] = '13.0'
s330.solub['50°C'] = '13.3'
s330.solub['60°C'] = '13.8'
s330.solub['70°C'] = 'N/A'
s330.solub['80°C'] = '15.3'
s330.solub['90°C'] = 'N/A'
s330.solub['100°C'] = '17.5'
sublist.append(s330)

s331 = substance('Lithium iodide', 'LiI')
s331.solub['0°C'] = '151'
s331.solub['10°C'] = '157'
s331.solub['20°C'] = '165'
s331.solub['30°C'] = '171'
s331.solub['40°C'] = '179'
s331.solub['50°C'] = 'N/A'
s331.solub['60°C'] = '202'
s331.solub['70°C'] = 'N/A'
s331.solub['80°C'] = '435'
s331.solub['90°C'] = '440'
s331.solub['100°C'] = '481'
sublist.append(s331)

s332 = substance('Lithium molybdate', 'Li2MoO4')
s332.solub['0°C'] = '82.6'
s332.solub['10°C'] = 'N/A'
s332.solub['20°C'] = '79.5'
s332.solub['30°C'] = '79.5'
s332.solub['40°C'] = '78'
s332.solub['50°C'] = 'N/A'
s332.solub['60°C'] = 'N/A'
s332.solub['70°C'] = 'N/A'
s332.solub['80°C'] = 'N/A'
s332.solub['90°C'] = 'N/A'
s332.solub['100°C'] = '73.9'
sublist.append(s332)

s333 = substance('Lithium nitrate', 'LiNO3')
s333.solub['0°C'] = '53.4'
s333.solub['10°C'] = '60.8'
s333.solub['20°C'] = '70.1'
s333.solub['30°C'] = '138'
s333.solub['40°C'] = '152'
s333.solub['50°C'] = 'N/A'
s333.solub['60°C'] = '175'
s333.solub['70°C'] = 'N/A'
s333.solub['80°C'] = 'N/A'
s333.solub['90°C'] = 'N/A'
s333.solub['100°C'] = 'N/A'
sublist.append(s333)

s334 = substance('Lithium nitrite', 'LiNO2')
s334.solub['0°C'] = '70.9'
s334.solub['10°C'] = '82.5'
s334.solub['20°C'] = '96.8'
s334.solub['30°C'] = '114'
s334.solub['40°C'] = '133'
s334.solub['50°C'] = 'N/A'
s334.solub['60°C'] = '177'
s334.solub['70°C'] = 'N/A'
s334.solub['80°C'] = '233'
s334.solub['90°C'] = '272'
s334.solub['100°C'] = '324'
sublist.append(s334)

s335 = substance('Lithium oxalate', 'Li2C2O4')
s335.solub['0°C'] = 'N/A'
s335.solub['10°C'] = 'N/A'
s335.solub['20°C'] = '8'
s335.solub['30°C'] = 'N/A'
s335.solub['40°C'] = 'N/A'
s335.solub['50°C'] = 'N/A'
s335.solub['60°C'] = 'N/A'
s335.solub['70°C'] = 'N/A'
s335.solub['80°C'] = 'N/A'
s335.solub['90°C'] = 'N/A'
s335.solub['100°C'] = 'N/A'
sublist.append(s335)

s336 = substance('Lithium perchlorate', 'LiClO4')
s336.solub['0°C'] = '42.7'
s336.solub['10°C'] = '49'
s336.solub['20°C'] = '56.1'
s336.solub['30°C'] = '63.6'
s336.solub['40°C'] = '72.3'
s336.solub['50°C'] = 'N/A'
s336.solub['60°C'] = '92.3'
s336.solub['70°C'] = 'N/A'
s336.solub['80°C'] = '128'
s336.solub['90°C'] = '151'
s336.solub['100°C'] = 'N/A'
sublist.append(s336)

s337 = substance('Lithium permanganate', 'LiMnO4')
s337.solub['0°C'] = 'N/A'
s337.solub['10°C'] = 'N/A'
s337.solub['20°C'] = '71.4'
s337.solub['30°C'] = 'N/A'
s337.solub['40°C'] = 'N/A'
s337.solub['50°C'] = 'N/A'
s337.solub['60°C'] = 'N/A'
s337.solub['70°C'] = 'N/A'
s337.solub['80°C'] = 'N/A'
s337.solub['90°C'] = 'N/A'
s337.solub['100°C'] = 'N/A'
sublist.append(s337)

s338 = substance('Lithium phosphate', 'Li3PO4')
s338.solub['0°C'] = 'N/A'
s338.solub['10°C'] = 'N/A'
s338.solub['20°C'] = '0.039'
s338.solub['30°C'] = 'N/A'
s338.solub['40°C'] = 'N/A'
s338.solub['50°C'] = 'N/A'
s338.solub['60°C'] = 'N/A'
s338.solub['70°C'] = 'N/A'
s338.solub['80°C'] = 'N/A'
s338.solub['90°C'] = 'N/A'
s338.solub['100°C'] = 'N/A'
sublist.append(s338)

s339 = substance('Lithium selenide', 'Li2Se')
s339.solub['0°C'] = 'N/A'
s339.solub['10°C'] = 'N/A'
s339.solub['20°C'] = '57.7'
s339.solub['30°C'] = 'N/A'
s339.solub['40°C'] = 'N/A'
s339.solub['50°C'] = 'N/A'
s339.solub['60°C'] = 'N/A'
s339.solub['70°C'] = 'N/A'
s339.solub['80°C'] = 'N/A'
s339.solub['90°C'] = 'N/A'
s339.solub['100°C'] = 'N/A'
sublist.append(s339)

s340 = substance('Lithium selenite', 'Li2SeO3')
s340.solub['0°C'] = '25'
s340.solub['10°C'] = '23.3'
s340.solub['20°C'] = '21.5'
s340.solub['30°C'] = '19.6'
s340.solub['40°C'] = '17.9'
s340.solub['50°C'] = 'N/A'
s340.solub['60°C'] = '14.7'
s340.solub['70°C'] = 'N/A'
s340.solub['80°C'] = '11.9'
s340.solub['90°C'] = '11.1'
s340.solub['100°C'] = '9.9'
sublist.append(s340)

s341 = substance('Lithium sulfate', 'Li2SO4')
s341.solub['0°C'] = '36.1'
s341.solub['10°C'] = '35.5'
s341.solub['20°C'] = '34.8'
s341.solub['30°C'] = '34.2'
s341.solub['40°C'] = '33.7'
s341.solub['50°C'] = 'N/A'
s341.solub['60°C'] = '32.6'
s341.solub['70°C'] = 'N/A'
s341.solub['80°C'] = '31.4'
s341.solub['90°C'] = '30.9'
s341.solub['100°C'] = 'N/A'
sublist.append(s341)

s342 = substance('Lithium tartrate', 'Li2C4H4O6')
s342.solub['0°C'] = '42'
s342.solub['10°C'] = '31.8'
s342.solub['20°C'] = '27.1'
s342.solub['30°C'] = '26.6'
s342.solub['40°C'] = '27.2'
s342.solub['50°C'] = 'N/A'
s342.solub['60°C'] = '29.5'
s342.solub['70°C'] = 'N/A'
s342.solub['80°C'] = 'N/A'
s342.solub['90°C'] = 'N/A'
s342.solub['100°C'] = 'N/A'
sublist.append(s342)

s343 = substance('Lithium thiocyanate', 'LiSCN')
s343.solub['0°C'] = 'N/A'
s343.solub['10°C'] = 'N/A'
s343.solub['20°C'] = '114'
s343.solub['30°C'] = '131'
s343.solub['40°C'] = '153'
s343.solub['50°C'] = 'N/A'
s343.solub['60°C'] = 'N/A'
s343.solub['70°C'] = 'N/A'
s343.solub['80°C'] = 'N/A'
s343.solub['90°C'] = 'N/A'
s343.solub['100°C'] = 'N/A'
sublist.append(s343)

s344 = substance('Lithium vanadate', 'LiVO3')
s344.solub['0°C'] = '2.5'
s344.solub['10°C'] = 'N/A'
s344.solub['20°C'] = '4.82'
s344.solub['30°C'] = '6.28'
s344.solub['40°C'] = '4.38'
s344.solub['50°C'] = 'N/A'
s344.solub['60°C'] = '2.67'
s344.solub['70°C'] = 'N/A'
s344.solub['80°C'] = 'N/A'
s344.solub['90°C'] = 'N/A'
s344.solub['100°C'] = 'N/A'
sublist.append(s344)

s345 = substance('Lutetium(III) hydroxide', 'Lu(OH)3')
s345.solub['0°C'] = 'N/A'
s345.solub['10°C'] = 'N/A'
s345.solub['20°C'] = '1.164×10-5'
s345.solub['30°C'] = 'N/A'
s345.solub['40°C'] = 'N/A'
s345.solub['50°C'] = 'N/A'
s345.solub['60°C'] = 'N/A'
s345.solub['70°C'] = 'N/A'
s345.solub['80°C'] = 'N/A'
s345.solub['90°C'] = 'N/A'
s345.solub['100°C'] = 'N/A'
sublist.append(s345)

s346 = substance('Lutetium(III) sulfate', 'Lu2(SO4)3.8H2O')
s346.solub['0°C'] = 'N/A'
s346.solub['10°C'] = 'N/A'
s346.solub['20°C'] = '57.9'
s346.solub['30°C'] = 'N/A'
s346.solub['40°C'] = 'N/A'
s346.solub['50°C'] = 'N/A'
s346.solub['60°C'] = 'N/A'
s346.solub['70°C'] = 'N/A'
s346.solub['80°C'] = 'N/A'
s346.solub['90°C'] = 'N/A'
s346.solub['100°C'] = 'N/A'
sublist.append(s346)

s347 = substance('Magnesium acetate', 'Mg(C2H3O2)2')
s347.solub['0°C'] = '56.7'
s347.solub['10°C'] = '59.7'
s347.solub['20°C'] = '53.4'
s347.solub['30°C'] = '68.6'
s347.solub['40°C'] = '75.7'
s347.solub['50°C'] = 'N/A'
s347.solub['60°C'] = '118'
s347.solub['70°C'] = 'N/A'
s347.solub['80°C'] = 'N/A'
s347.solub['90°C'] = 'N/A'
s347.solub['100°C'] = 'N/A'
sublist.append(s347)

s348 = substance('Magnesium benzoate', 'Mg(C7H5O2)2.H2O')
s348.solub['0°C'] = 'N/A'
s348.solub['10°C'] = 'N/A'
s348.solub['20°C'] = 'N/A'
s348.solub['30°C'] = 'N/A'
s348.solub['40°C'] = '5'
s348.solub['50°C'] = 'N/A'
s348.solub['60°C'] = 'N/A'
s348.solub['70°C'] = 'N/A'
s348.solub['80°C'] = 'N/A'
s348.solub['90°C'] = 'N/A'
s348.solub['100°C'] = 'N/A'
sublist.append(s348)

s349 = substance('Magnesium bromate', 'Mg(BrO3)2.6H2O')
s349.solub['0°C'] = 'N/A'
s349.solub['10°C'] = 'N/A'
s349.solub['20°C'] = 'N/A'
s349.solub['30°C'] = 'N/A'
s349.solub['40°C'] = '58'
s349.solub['50°C'] = 'N/A'
s349.solub['60°C'] = 'N/A'
s349.solub['70°C'] = 'N/A'
s349.solub['80°C'] = 'N/A'
s349.solub['90°C'] = 'N/A'
s349.solub['100°C'] = 'N/A'
sublist.append(s349)

s350 = substance('Magnesium bromide', 'MgBr2')
s350.solub['0°C'] = '98'
s350.solub['10°C'] = '99'
s350.solub['20°C'] = '101'
s350.solub['30°C'] = '104'
s350.solub['40°C'] = '106'
s350.solub['50°C'] = 'N/A'
s350.solub['60°C'] = '112'
s350.solub['70°C'] = 'N/A'
s350.solub['80°C'] = 'N/A'
s350.solub['90°C'] = 'N/A'
s350.solub['100°C'] = '125'
sublist.append(s350)

s351 = substance('Magnesium carbonate', 'MgCO3')
s351.solub['0°C'] = 'N/A'
s351.solub['10°C'] = 'N/A'
s351.solub['20°C'] = '0.039'
s351.solub['30°C'] = 'N/A'
s351.solub['40°C'] = 'N/A'
s351.solub['50°C'] = 'N/A'
s351.solub['60°C'] = 'N/A'
s351.solub['70°C'] = 'N/A'
s351.solub['80°C'] = 'N/A'
s351.solub['90°C'] = 'N/A'
s351.solub['100°C'] = 'N/A'
sublist.append(s351)

s352 = substance('Magnesium chlorate', 'Mg(ClO3)2')
s352.solub['0°C'] = '114'
s352.solub['10°C'] = '123'
s352.solub['20°C'] = '135'
s352.solub['30°C'] = '155'
s352.solub['40°C'] = '178'
s352.solub['50°C'] = 'N/A'
s352.solub['60°C'] = '242'
s352.solub['70°C'] = 'N/A'
s352.solub['80°C'] = 'N/A'
s352.solub['90°C'] = '268'
s352.solub['100°C'] = 'N/A'
sublist.append(s352)

s353 = substance('Magnesium chloride', 'MgCl2')
s353.solub['0°C'] = '52.9'
s353.solub['10°C'] = '53.6'
s353.solub['20°C'] = '54.6'
s353.solub['30°C'] = '55.8'
s353.solub['40°C'] = '57.5'
s353.solub['50°C'] = 'N/A'
s353.solub['60°C'] = '61'
s353.solub['70°C'] = 'N/A'
s353.solub['80°C'] = '66.1'
s353.solub['90°C'] = '69.5'
s353.solub['100°C'] = '73.3'
sublist.append(s353)

s354 = substance('Magnesium chromate', 'MgCrO4.7H2O')
s354.solub['0°C'] = 'N/A'
s354.solub['10°C'] = 'N/A'
s354.solub['20°C'] = '137'
s354.solub['30°C'] = 'N/A'
s354.solub['40°C'] = 'N/A'
s354.solub['50°C'] = 'N/A'
s354.solub['60°C'] = 'N/A'
s354.solub['70°C'] = 'N/A'
s354.solub['80°C'] = 'N/A'
s354.solub['90°C'] = 'N/A'
s354.solub['100°C'] = 'N/A'
sublist.append(s354)

s355 = substance('Magnesium fluoride', 'MgF2')
s355.solub['0°C'] = 'N/A'
s355.solub['10°C'] = 'N/A'
s355.solub['20°C'] = '0.007325'
s355.solub['30°C'] = 'N/A'
s355.solub['40°C'] = 'N/A'
s355.solub['50°C'] = 'N/A'
s355.solub['60°C'] = 'N/A'
s355.solub['70°C'] = 'N/A'
s355.solub['80°C'] = 'N/A'
s355.solub['90°C'] = 'N/A'
s355.solub['100°C'] = 'N/A'
sublist.append(s355)

s356 = substance('Magnesium fluorosilicate', 'MgSiF6')
s356.solub['0°C'] = '26.3'
s356.solub['10°C'] = 'N/A'
s356.solub['20°C'] = '30.8'
s356.solub['30°C'] = 'N/A'
s356.solub['40°C'] = '34.9'
s356.solub['50°C'] = 'N/A'
s356.solub['60°C'] = '44.4'
s356.solub['70°C'] = 'N/A'
s356.solub['80°C'] = 'N/A'
s356.solub['90°C'] = 'N/A'
s356.solub['100°C'] = 'N/A'
sublist.append(s356)

s357 = substance('Magnesium formate', 'Mg(HCO2)2')
s357.solub['0°C'] = '14'
s357.solub['10°C'] = '14.2'
s357.solub['20°C'] = '14.4'
s357.solub['30°C'] = '14.9'
s357.solub['40°C'] = '15.9'
s357.solub['50°C'] = 'N/A'
s357.solub['60°C'] = '17.9'
s357.solub['70°C'] = 'N/A'
s357.solub['80°C'] = '20.5'
s357.solub['90°C'] = '22.2'
s357.solub['100°C'] = '22.9'
sublist.append(s357)

s358 = substance('Magnesium hydroxide', 'Mg(OH)2')
s358.solub['0°C'] = 'N/A'
s358.solub['10°C'] = 'N/A'
s358.solub['20°C'] = '9.628×10-4'
s358.solub['30°C'] = 'N/A'
s358.solub['40°C'] = 'N/A'
s358.solub['50°C'] = 'N/A'
s358.solub['60°C'] = 'N/A'
s358.solub['70°C'] = 'N/A'
s358.solub['80°C'] = 'N/A'
s358.solub['90°C'] = 'N/A'
s358.solub['100°C'] = '0.004'
sublist.append(s358)

s359 = substance('Magnesium iodate', 'Mg(IO3)2')
s359.solub['0°C'] = 'N/A'
s359.solub['10°C'] = '7.2'
s359.solub['20°C'] = '8.6'
s359.solub['30°C'] = '10'
s359.solub['40°C'] = '11.7'
s359.solub['50°C'] = 'N/A'
s359.solub['60°C'] = '15.2'
s359.solub['70°C'] = 'N/A'
s359.solub['80°C'] = '15.5'
s359.solub['90°C'] = '15.6'
s359.solub['100°C'] = 'N/A'
sublist.append(s359)

s360 = substance('Magnesium iodide', 'MgI2')
s360.solub['0°C'] = '120'
s360.solub['10°C'] = 'N/A'
s360.solub['20°C'] = '140'
s360.solub['30°C'] = 'N/A'
s360.solub['40°C'] = '173'
s360.solub['50°C'] = 'N/A'
s360.solub['60°C'] = 'N/A'
s360.solub['70°C'] = 'N/A'
s360.solub['80°C'] = '186'
s360.solub['90°C'] = 'N/A'
s360.solub['100°C'] = 'N/A'
sublist.append(s360)

s361 = substance('Magnesium molybdate', 'MgMoO4')
s361.solub['0°C'] = 'N/A'
s361.solub['10°C'] = 'N/A'
s361.solub['20°C'] = '13.7'
s361.solub['30°C'] = 'N/A'
s361.solub['40°C'] = 'N/A'
s361.solub['50°C'] = 'N/A'
s361.solub['60°C'] = 'N/A'
s361.solub['70°C'] = 'N/A'
s361.solub['80°C'] = 'N/A'
s361.solub['90°C'] = 'N/A'
s361.solub['100°C'] = 'N/A'
sublist.append(s361)

s362 = substance('Magnesium nitrate', 'Mg(NO3)2')
s362.solub['0°C'] = '62.1'
s362.solub['10°C'] = '66'
s362.solub['20°C'] = '69.5'
s362.solub['30°C'] = '73.6'
s362.solub['40°C'] = '78.9'
s362.solub['50°C'] = 'N/A'
s362.solub['60°C'] = '78.9'
s362.solub['70°C'] = 'N/A'
s362.solub['80°C'] = '91.6'
s362.solub['90°C'] = '106'
s362.solub['100°C'] = 'N/A'
sublist.append(s362)

s363 = substance('Magnesium oxalate', 'MgC2O4')
s363.solub['0°C'] = 'N/A'
s363.solub['10°C'] = 'N/A'
s363.solub['20°C'] = '0.104'
s363.solub['30°C'] = 'N/A'
s363.solub['40°C'] = 'N/A'
s363.solub['50°C'] = 'N/A'
s363.solub['60°C'] = 'N/A'
s363.solub['70°C'] = 'N/A'
s363.solub['80°C'] = 'N/A'
s363.solub['90°C'] = 'N/A'
s363.solub['100°C'] = 'N/A'
sublist.append(s363)

s364 = substance('Magnesium perchlorate', 'Mg(ClO4)2')
s364.solub['0°C'] = 'N/A'
s364.solub['10°C'] = 'N/A'
s364.solub['20°C'] = '49.6'
s364.solub['30°C'] = 'N/A'
s364.solub['40°C'] = 'N/A'
s364.solub['50°C'] = 'N/A'
s364.solub['60°C'] = 'N/A'
s364.solub['70°C'] = 'N/A'
s364.solub['80°C'] = 'N/A'
s364.solub['90°C'] = 'N/A'
s364.solub['100°C'] = 'N/A'
sublist.append(s364)

s365 = substance('Magnesium phosphate', 'Mg3(PO4)2')
s365.solub['0°C'] = 'N/A'
s365.solub['10°C'] = 'N/A'
s365.solub['20°C'] = '2.588×10-4'
s365.solub['30°C'] = 'N/A'
s365.solub['40°C'] = 'N/A'
s365.solub['50°C'] = 'N/A'
s365.solub['60°C'] = 'N/A'
s365.solub['70°C'] = 'N/A'
s365.solub['80°C'] = 'N/A'
s365.solub['90°C'] = 'N/A'
s365.solub['100°C'] = 'N/A'
sublist.append(s365)

s366 = substance('Magnesium selenate', 'MgSeO4')
s366.solub['0°C'] = '20'
s366.solub['10°C'] = '30.4'
s366.solub['20°C'] = '38.3'
s366.solub['30°C'] = '44.3'
s366.solub['40°C'] = '48.6'
s366.solub['50°C'] = 'N/A'
s366.solub['60°C'] = '55.8'
s366.solub['70°C'] = 'N/A'
s366.solub['80°C'] = 'N/A'
s366.solub['90°C'] = 'N/A'
s366.solub['100°C'] = 'N/A'
sublist.append(s366)

s367 = substance('Magnesium selenite', 'MgSeO3')
s367.solub['0°C'] = 'N/A'
s367.solub['10°C'] = 'N/A'
s367.solub['20°C'] = '0.05454'
s367.solub['30°C'] = 'N/A'
s367.solub['40°C'] = 'N/A'
s367.solub['50°C'] = 'N/A'
s367.solub['60°C'] = 'N/A'
s367.solub['70°C'] = 'N/A'
s367.solub['80°C'] = 'N/A'
s367.solub['90°C'] = 'N/A'
s367.solub['100°C'] = 'N/A'
sublist.append(s367)

s368 = substance('Magnesium sulfate', 'MgSO4')
s368.solub['0°C'] = '25.5'
s368.solub['10°C'] = '30.4'
s368.solub['20°C'] = '35.1'
s368.solub['30°C'] = '39.7'
s368.solub['40°C'] = '44.7'
s368.solub['50°C'] = '50.4'
s368.solub['60°C'] = '54.8'
s368.solub['70°C'] = '59.2'
s368.solub['80°C'] = '54.8'
s368.solub['90°C'] = '52.9'
s368.solub['100°C'] = '50.2'
sublist.append(s368)

s369 = substance('Magnesium thiosulfate', 'MgS2O3')
s369.solub['0°C'] = 'N/A'
s369.solub['10°C'] = 'N/A'
s369.solub['20°C'] = '50'
s369.solub['30°C'] = 'N/A'
s369.solub['40°C'] = 'N/A'
s369.solub['50°C'] = 'N/A'
s369.solub['60°C'] = 'N/A'
s369.solub['70°C'] = 'N/A'
s369.solub['80°C'] = 'N/A'
s369.solub['90°C'] = 'N/A'
s369.solub['100°C'] = 'N/A'
sublist.append(s369)

s370 = substance('Maltose', 'C12H22O11')
s370.solub['0°C'] = 'N/A'
s370.solub['10°C'] = 'N/A'
s370.solub['20°C'] = '108'
s370.solub['30°C'] = 'N/A'
s370.solub['40°C'] = 'N/A'
s370.solub['50°C'] = 'N/A'
s370.solub['60°C'] = 'N/A'
s370.solub['70°C'] = 'N/A'
s370.solub['80°C'] = 'N/A'
s370.solub['90°C'] = 'N/A'
s370.solub['100°C'] = 'N/A'
sublist.append(s370)

s371 = substance('D-Mannose', 'C6H12O6')
s371.solub['0°C'] = 'N/A'
s371.solub['10°C'] = 'N/A'
s371.solub['20°C'] = '248'
s371.solub['30°C'] = 'N/A'
s371.solub['40°C'] = 'N/A'
s371.solub['50°C'] = 'N/A'
s371.solub['60°C'] = 'N/A'
s371.solub['70°C'] = 'N/A'
s371.solub['80°C'] = 'N/A'
s371.solub['90°C'] = 'N/A'
s371.solub['100°C'] = 'N/A'
sublist.append(s371)

s372 = substance('Manganese(II) bromide', 'MnBr2')
s372.solub['0°C'] = '127'
s372.solub['10°C'] = '136'
s372.solub['20°C'] = '147'
s372.solub['30°C'] = '157'
s372.solub['40°C'] = '169'
s372.solub['50°C'] = 'N/A'
s372.solub['60°C'] = '197'
s372.solub['70°C'] = 'N/A'
s372.solub['80°C'] = '225'
s372.solub['90°C'] = '226'
s372.solub['100°C'] = '228'
sublist.append(s372)

s373 = substance('Manganese(II) carbonate', 'MnCO3')
s373.solub['0°C'] = 'N/A'
s373.solub['10°C'] = 'N/A'
s373.solub['20°C'] = '4.877×10-5'
s373.solub['30°C'] = 'N/A'
s373.solub['40°C'] = 'N/A'
s373.solub['50°C'] = 'N/A'
s373.solub['60°C'] = 'N/A'
s373.solub['70°C'] = 'N/A'
s373.solub['80°C'] = 'N/A'
s373.solub['90°C'] = 'N/A'
s373.solub['100°C'] = 'N/A'
sublist.append(s373)

s374 = substance('Manganese(II) chloride', 'MnCl2')
s374.solub['0°C'] = '63.4'
s374.solub['10°C'] = '68.1'
s374.solub['20°C'] = '73.9'
s374.solub['30°C'] = '80.8'
s374.solub['40°C'] = '88.5'
s374.solub['50°C'] = 'N/A'
s374.solub['60°C'] = '109'
s374.solub['70°C'] = 'N/A'
s374.solub['80°C'] = '113'
s374.solub['90°C'] = '114'
s374.solub['100°C'] = '115'
sublist.append(s374)

s375 = substance('Manganese(II) ferrocyanide', 'Mn2Fe(CN)6')
s375.solub['0°C'] = 'N/A'
s375.solub['10°C'] = 'N/A'
s375.solub['20°C'] = '0.001882'
s375.solub['30°C'] = 'N/A'
s375.solub['40°C'] = 'N/A'
s375.solub['50°C'] = 'N/A'
s375.solub['60°C'] = 'N/A'
s375.solub['70°C'] = 'N/A'
s375.solub['80°C'] = 'N/A'
s375.solub['90°C'] = 'N/A'
s375.solub['100°C'] = 'N/A'
sublist.append(s375)

s376 = substance('Manganese(II) fluoride', 'MnF2')
s376.solub['0°C'] = 'N/A'
s376.solub['10°C'] = 'N/A'
s376.solub['20°C'] = '0.96'
s376.solub['30°C'] = 'N/A'
s376.solub['40°C'] = '0.67'
s376.solub['50°C'] = 'N/A'
s376.solub['60°C'] = '0.44'
s376.solub['70°C'] = 'N/A'
s376.solub['80°C'] = 'N/A'
s376.solub['90°C'] = 'N/A'
s376.solub['100°C'] = '0.48'
sublist.append(s376)

s377 = substance('Manganese(II) fluorosilicate', 'MnSiF6.6H2O')
s377.solub['0°C'] = 'N/A'
s377.solub['10°C'] = 'N/A'
s377.solub['20°C'] = '140'
s377.solub['30°C'] = 'N/A'
s377.solub['40°C'] = 'N/A'
s377.solub['50°C'] = 'N/A'
s377.solub['60°C'] = 'N/A'
s377.solub['70°C'] = 'N/A'
s377.solub['80°C'] = 'N/A'
s377.solub['90°C'] = 'N/A'
s377.solub['100°C'] = 'N/A'
sublist.append(s377)

s378 = substance('Manganese(II) hydroxide', 'Mn(OH)2')
s378.solub['0°C'] = 'N/A'
s378.solub['10°C'] = 'N/A'
s378.solub['20°C'] = '3.221×10-4'
s378.solub['30°C'] = 'N/A'
s378.solub['40°C'] = 'N/A'
s378.solub['50°C'] = 'N/A'
s378.solub['60°C'] = 'N/A'
s378.solub['70°C'] = 'N/A'
s378.solub['80°C'] = 'N/A'
s378.solub['90°C'] = 'N/A'
s378.solub['100°C'] = 'N/A'
sublist.append(s378)

s379 = substance('Manganese(II) nitrate', 'Mn(NO3)2')
s379.solub['0°C'] = '102'
s379.solub['10°C'] = '118'
s379.solub['20°C'] = '139'
s379.solub['30°C'] = '206'
s379.solub['40°C'] = 'N/A'
s379.solub['50°C'] = 'N/A'
s379.solub['60°C'] = 'N/A'
s379.solub['70°C'] = 'N/A'
s379.solub['80°C'] = 'N/A'
s379.solub['90°C'] = 'N/A'
s379.solub['100°C'] = 'N/A'
sublist.append(s379)

s380 = substance('Manganese(II) oxalate', 'MnC2O4.2H2O')
s380.solub['0°C'] = '0.02'
s380.solub['10°C'] = '0.024'
s380.solub['20°C'] = '0.028'
s380.solub['30°C'] = '0.033'
s380.solub['40°C'] = 'N/A'
s380.solub['50°C'] = 'N/A'
s380.solub['60°C'] = 'N/A'
s380.solub['70°C'] = 'N/A'
s380.solub['80°C'] = 'N/A'
s380.solub['90°C'] = 'N/A'
s380.solub['100°C'] = 'N/A'
sublist.append(s380)

s381 = substance('Manganese(II) sulfate', 'MnSO4')
s381.solub['0°C'] = '52.9'
s381.solub['10°C'] = '59.7'
s381.solub['20°C'] = '62.9'
s381.solub['30°C'] = '62.9'
s381.solub['40°C'] = '60'
s381.solub['50°C'] = 'N/A'
s381.solub['60°C'] = '53.6'
s381.solub['70°C'] = 'N/A'
s381.solub['80°C'] = '45.6'
s381.solub['90°C'] = '40.9'
s381.solub['100°C'] = '35.3'
sublist.append(s381)

s382 = substance('Mercury(I) azide', 'Hg2(N3)2')
s382.solub['0°C'] = 'N/A'
s382.solub['10°C'] = 'N/A'
s382.solub['20°C'] = '0.02727'
s382.solub['30°C'] = 'N/A'
s382.solub['40°C'] = 'N/A'
s382.solub['50°C'] = 'N/A'
s382.solub['60°C'] = 'N/A'
s382.solub['70°C'] = 'N/A'
s382.solub['80°C'] = 'N/A'
s382.solub['90°C'] = 'N/A'
s382.solub['100°C'] = 'N/A'
sublist.append(s382)

s383 = substance('Mercury(I) bromide', 'Hg2Br2')
s383.solub['0°C'] = 'N/A'
s383.solub['10°C'] = 'N/A'
s383.solub['20°C'] = '1.352×10-6'
s383.solub['30°C'] = 'N/A'
s383.solub['40°C'] = 'N/A'
s383.solub['50°C'] = 'N/A'
s383.solub['60°C'] = 'N/A'
s383.solub['70°C'] = 'N/A'
s383.solub['80°C'] = 'N/A'
s383.solub['90°C'] = 'N/A'
s383.solub['100°C'] = 'N/A'
sublist.append(s383)

s384 = substance('Mercury(I) carbonate', 'Hg2CO3')
s384.solub['0°C'] = 'N/A'
s384.solub['10°C'] = 'N/A'
s384.solub['20°C'] = '4.351×10-7'
s384.solub['30°C'] = 'N/A'
s384.solub['40°C'] = 'N/A'
s384.solub['50°C'] = 'N/A'
s384.solub['60°C'] = 'N/A'
s384.solub['70°C'] = 'N/A'
s384.solub['80°C'] = 'N/A'
s384.solub['90°C'] = 'N/A'
s384.solub['100°C'] = 'N/A'
sublist.append(s384)

s385 = substance('Mercury(I) chloride', 'Hg2Cl2')
s385.solub['0°C'] = 'N/A'
s385.solub['10°C'] = 'N/A'
s385.solub['20°C'] = '3.246×10-5'
s385.solub['30°C'] = 'N/A'
s385.solub['40°C'] = 'N/A'
s385.solub['50°C'] = 'N/A'
s385.solub['60°C'] = 'N/A'
s385.solub['70°C'] = 'N/A'
s385.solub['80°C'] = 'N/A'
s385.solub['90°C'] = 'N/A'
s385.solub['100°C'] = 'N/A'
sublist.append(s385)

s386 = substance('Mercury(I) chromate', 'Hg2CrO4')
s386.solub['0°C'] = 'N/A'
s386.solub['10°C'] = 'N/A'
s386.solub['20°C'] = '0.002313'
s386.solub['30°C'] = 'N/A'
s386.solub['40°C'] = 'N/A'
s386.solub['50°C'] = 'N/A'
s386.solub['60°C'] = 'N/A'
s386.solub['70°C'] = 'N/A'
s386.solub['80°C'] = 'N/A'
s386.solub['90°C'] = 'N/A'
s386.solub['100°C'] = 'N/A'
sublist.append(s386)

s387 = substance('Mercury(I) cyanide', 'Hg2(CN)2')
s387.solub['0°C'] = 'N/A'
s387.solub['10°C'] = 'N/A'
s387.solub['20°C'] = '2.266×10-12'
s387.solub['30°C'] = 'N/A'
s387.solub['40°C'] = 'N/A'
s387.solub['50°C'] = 'N/A'
s387.solub['60°C'] = 'N/A'
s387.solub['70°C'] = 'N/A'
s387.solub['80°C'] = 'N/A'
s387.solub['90°C'] = 'N/A'
s387.solub['100°C'] = 'N/A'
sublist.append(s387)

s388 = substance('Mercury(I) perchlorate', 'Hg2(ClO4)2')
s388.solub['0°C'] = '282'
s388.solub['10°C'] = '325'
s388.solub['20°C'] = '407'
s388.solub['30°C'] = '455'
s388.solub['40°C'] = 'N/A'
s388.solub['50°C'] = '499'
s388.solub['60°C'] = 'N/A'
s388.solub['70°C'] = '541'
s388.solub['80°C'] = 'N/A'
s388.solub['90°C'] = '580'
s388.solub['100°C'] = 'N/A'
sublist.append(s388)

s389 = substance('Mercury(I) sulfate', 'Hg2SO4')
s389.solub['0°C'] = 'N/A'
s389.solub['10°C'] = 'N/A'
s389.solub['20°C'] = '0.04277'
s389.solub['30°C'] = 'N/A'
s389.solub['40°C'] = 'N/A'
s389.solub['50°C'] = 'N/A'
s389.solub['60°C'] = 'N/A'
s389.solub['70°C'] = 'N/A'
s389.solub['80°C'] = 'N/A'
s389.solub['90°C'] = 'N/A'
s389.solub['100°C'] = 'N/A'
sublist.append(s389)

s390 = substance('Mercury(II) acetate', 'Hg(C2H3O2)2')
s390.solub['0°C'] = 'N/A'
s390.solub['10°C'] = 'N/A'
s390.solub['20°C'] = '25'
s390.solub['30°C'] = 'N/A'
s390.solub['40°C'] = 'N/A'
s390.solub['50°C'] = 'N/A'
s390.solub['60°C'] = 'N/A'
s390.solub['70°C'] = 'N/A'
s390.solub['80°C'] = 'N/A'
s390.solub['90°C'] = 'N/A'
s390.solub['100°C'] = 'N/A'
sublist.append(s390)

s391 = substance('Mercury(II) benzoate', 'Hg(C7H5O2)2.2O')
s391.solub['0°C'] = 'N/A'
s391.solub['10°C'] = 'N/A'
s391.solub['20°C'] = '1.1'
s391.solub['30°C'] = 'N/A'
s391.solub['40°C'] = 'N/A'
s391.solub['50°C'] = 'N/A'
s391.solub['60°C'] = 'N/A'
s391.solub['70°C'] = 'N/A'
s391.solub['80°C'] = 'N/A'
s391.solub['90°C'] = 'N/A'
s391.solub['100°C'] = 'N/A'
sublist.append(s391)

s392 = substance('Mercury(II) bromate', 'Hg(BrO3)2.2H2O')
s392.solub['0°C'] = 'N/A'
s392.solub['10°C'] = 'N/A'
s392.solub['20°C'] = '0.08'
s392.solub['30°C'] = 'N/A'
s392.solub['40°C'] = 'N/A'
s392.solub['50°C'] = 'N/A'
s392.solub['60°C'] = 'N/A'
s392.solub['70°C'] = 'N/A'
s392.solub['80°C'] = 'N/A'
s392.solub['90°C'] = 'N/A'
s392.solub['100°C'] = 'N/A'
sublist.append(s392)

s393 = substance('Mercury(II) bromide', 'HgBr2')
s393.solub['0°C'] = '0.3'
s393.solub['10°C'] = '0.4'
s393.solub['20°C'] = '0.56'
s393.solub['30°C'] = '0.66'
s393.solub['40°C'] = '0.91'
s393.solub['50°C'] = 'N/A'
s393.solub['60°C'] = '1.68'
s393.solub['70°C'] = 'N/A'
s393.solub['80°C'] = '2.77'
s393.solub['90°C'] = 'N/A'
s393.solub['100°C'] = '4.9'
sublist.append(s393)

s394 = substance('Mercury(II) chlorate', 'Hg(ClO3)2')
s394.solub['0°C'] = 'N/A'
s394.solub['10°C'] = 'N/A'
s394.solub['20°C'] = '25'
s394.solub['30°C'] = 'N/A'
s394.solub['40°C'] = 'N/A'
s394.solub['50°C'] = 'N/A'
s394.solub['60°C'] = 'N/A'
s394.solub['70°C'] = 'N/A'
s394.solub['80°C'] = 'N/A'
s394.solub['90°C'] = 'N/A'
s394.solub['100°C'] = 'N/A'
sublist.append(s394)

s395 = substance('Mercury(II) chloride', 'HgCl2')
s395.solub['0°C'] = '3.63'
s395.solub['10°C'] = '4.82'
s395.solub['20°C'] = '6.57'
s395.solub['30°C'] = '8.34'
s395.solub['40°C'] = '10.2'
s395.solub['50°C'] = 'N/A'
s395.solub['60°C'] = '16.3'
s395.solub['70°C'] = 'N/A'
s395.solub['80°C'] = '30'
s395.solub['90°C'] = 'N/A'
s395.solub['100°C'] = '61.3'
sublist.append(s395)

s396 = substance('Mercury(II) cyanide', 'Hg(CN)2')
s396.solub['0°C'] = 'N/A'
s396.solub['10°C'] = 'N/A'
s396.solub['20°C'] = '9.3'
s396.solub['30°C'] = 'N/A'
s396.solub['40°C'] = 'N/A'
s396.solub['50°C'] = 'N/A'
s396.solub['60°C'] = 'N/A'
s396.solub['70°C'] = 'N/A'
s396.solub['80°C'] = 'N/A'
s396.solub['90°C'] = 'N/A'
s396.solub['100°C'] = 'N/A'
sublist.append(s396)

s397 = substance('Mercury(II) iodate', 'Hg(IO3)2')
s397.solub['0°C'] = 'N/A'
s397.solub['10°C'] = 'N/A'
s397.solub['20°C'] = '0.002372'
s397.solub['30°C'] = 'N/A'
s397.solub['40°C'] = 'N/A'
s397.solub['50°C'] = 'N/A'
s397.solub['60°C'] = 'N/A'
s397.solub['70°C'] = 'N/A'
s397.solub['80°C'] = 'N/A'
s397.solub['90°C'] = 'N/A'
s397.solub['100°C'] = 'N/A'
sublist.append(s397)

s398 = substance('Mercury(II) iodide', 'HgI2')
s398.solub['0°C'] = 'N/A'
s398.solub['10°C'] = 'N/A'
s398.solub['20°C'] = '0.006'
s398.solub['30°C'] = 'N/A'
s398.solub['40°C'] = 'N/A'
s398.solub['50°C'] = 'N/A'
s398.solub['60°C'] = 'N/A'
s398.solub['70°C'] = 'N/A'
s398.solub['80°C'] = 'N/A'
s398.solub['90°C'] = 'N/A'
s398.solub['100°C'] = 'N/A'
sublist.append(s398)

s399 = substance('Mercury(II) oxalate', 'HgC2O4')
s399.solub['0°C'] = 'N/A'
s399.solub['10°C'] = 'N/A'
s399.solub['20°C'] = '0.011'
s399.solub['30°C'] = 'N/A'
s399.solub['40°C'] = 'N/A'
s399.solub['50°C'] = 'N/A'
s399.solub['60°C'] = 'N/A'
s399.solub['70°C'] = 'N/A'
s399.solub['80°C'] = 'N/A'
s399.solub['90°C'] = 'N/A'
s399.solub['100°C'] = 'N/A'
sublist.append(s399)

s400 = substance('Mercury(II) sulfide', 'HgS')
s400.solub['0°C'] = 'N/A'
s400.solub['10°C'] = 'N/A'
s400.solub['20°C'] = '2.943×10-25'
s400.solub['30°C'] = 'N/A'
s400.solub['40°C'] = 'N/A'
s400.solub['50°C'] = 'N/A'
s400.solub['60°C'] = 'N/A'
s400.solub['70°C'] = 'N/A'
s400.solub['80°C'] = 'N/A'
s400.solub['90°C'] = 'N/A'
s400.solub['100°C'] = 'N/A'
sublist.append(s400)

s401 = substance('Mercury(II) thiocyanate', 'Hg(SCN)2')
s401.solub['0°C'] = 'N/A'
s401.solub['10°C'] = 'N/A'
s401.solub['20°C'] = '0.063'
s401.solub['30°C'] = 'N/A'
s401.solub['40°C'] = 'N/A'
s401.solub['50°C'] = 'N/A'
s401.solub['60°C'] = 'N/A'
s401.solub['70°C'] = 'N/A'
s401.solub['80°C'] = 'N/A'
s401.solub['90°C'] = 'N/A'
s401.solub['100°C'] = 'N/A'
sublist.append(s401)

s402 = substance('Neodymium(III) acetate', 'Nd(C2H3O2)3.H2O')
s402.solub['0°C'] = 'N/A'
s402.solub['10°C'] = 'N/A'
s402.solub['20°C'] = '26.2'
s402.solub['30°C'] = 'N/A'
s402.solub['40°C'] = 'N/A'
s402.solub['50°C'] = 'N/A'
s402.solub['60°C'] = 'N/A'
s402.solub['70°C'] = 'N/A'
s402.solub['80°C'] = 'N/A'
s402.solub['90°C'] = 'N/A'
s402.solub['100°C'] = 'N/A'
sublist.append(s402)

s403 = substance('Neodymium(III) bromate', 'Nd(BrO3)3')
s403.solub['0°C'] = '43.9'
s403.solub['10°C'] = '59.2'
s403.solub['20°C'] = '75.6'
s403.solub['30°C'] = '95.2'
s403.solub['40°C'] = '116'
s403.solub['50°C'] = 'N/A'
s403.solub['60°C'] = 'N/A'
s403.solub['70°C'] = 'N/A'
s403.solub['80°C'] = 'N/A'
s403.solub['90°C'] = 'N/A'
s403.solub['100°C'] = 'N/A'
sublist.append(s403)

s404 = substance('Neodymium(III) chloride', 'NdCl3')
s404.solub['0°C'] = 'N/A'
s404.solub['10°C'] = '96.7'
s404.solub['20°C'] = '98'
s404.solub['30°C'] = '99.6'
s404.solub['40°C'] = '102'
s404.solub['50°C'] = 'N/A'
s404.solub['60°C'] = '105'
s404.solub['70°C'] = 'N/A'
s404.solub['80°C'] = 'N/A'
s404.solub['90°C'] = 'N/A'
s404.solub['100°C'] = 'N/A'
sublist.append(s404)

s405 = substance('Neodymium(III) molybdate', 'Nd2(MoO4)3')
s405.solub['0°C'] = 'N/A'
s405.solub['10°C'] = 'N/A'
s405.solub['20°C'] = 'N/A'
s405.solub['30°C'] = '0.0019'
s405.solub['40°C'] = 'N/A'
s405.solub['50°C'] = 'N/A'
s405.solub['60°C'] = 'N/A'
s405.solub['70°C'] = 'N/A'
s405.solub['80°C'] = 'N/A'
s405.solub['90°C'] = 'N/A'
s405.solub['100°C'] = 'N/A'
sublist.append(s405)

s406 = substance('Neodymium(III) nitrate', 'Nd(NO3)3')
s406.solub['0°C'] = '127'
s406.solub['10°C'] = '133'
s406.solub['20°C'] = '142'
s406.solub['30°C'] = '145'
s406.solub['40°C'] = '159'
s406.solub['50°C'] = 'N/A'
s406.solub['60°C'] = '211'
s406.solub['70°C'] = 'N/A'
s406.solub['80°C'] = 'N/A'
s406.solub['90°C'] = 'N/A'
s406.solub['100°C'] = 'N/A'
sublist.append(s406)

s407 = substance('Neodymium(III) selenate', 'Nd2(SeO4)3')
s407.solub['0°C'] = '45.2'
s407.solub['10°C'] = '44.6'
s407.solub['20°C'] = '41.8'
s407.solub['30°C'] = '39.9'
s407.solub['40°C'] = '39.9'
s407.solub['50°C'] = 'N/A'
s407.solub['60°C'] = '43.9'
s407.solub['70°C'] = 'N/A'
s407.solub['80°C'] = '7'
s407.solub['90°C'] = '3.3'
s407.solub['100°C'] = 'N/A'
sublist.append(s407)

s408 = substance('Neodymium(III) sulfate', 'Nd2(SO4)3')
s408.solub['0°C'] = '13'
s408.solub['10°C'] = '9.7'
s408.solub['20°C'] = '7.1'
s408.solub['30°C'] = '5.3'
s408.solub['40°C'] = '4.1'
s408.solub['50°C'] = 'N/A'
s408.solub['60°C'] = '2.8'
s408.solub['70°C'] = 'N/A'
s408.solub['80°C'] = '2.2'
s408.solub['90°C'] = '1.2'
s408.solub['100°C'] = 'N/A'
sublist.append(s408)

s409 = substance('Nickel(II) acetate', 'Ni(C2H3O2)2')
s409.solub['0°C'] = 'N/A'
s409.solub['10°C'] = 'N/A'
s409.solub['20°C'] = 'N/A'
s409.solub['30°C'] = 'N/A'
s409.solub['40°C'] = 'N/A'
s409.solub['50°C'] = 'N/A'
s409.solub['60°C'] = 'N/A'
s409.solub['70°C'] = 'N/A'
s409.solub['80°C'] = 'N/A'
s409.solub['90°C'] = 'N/A'
s409.solub['100°C'] = 'N/A'
sublist.append(s409)

s410 = substance('Nickel(II) bromate', 'Ni(BrO3)2.6H2O')
s410.solub['0°C'] = 'N/A'
s410.solub['10°C'] = 'N/A'
s410.solub['20°C'] = '28'
s410.solub['30°C'] = 'N/A'
s410.solub['40°C'] = 'N/A'
s410.solub['50°C'] = 'N/A'
s410.solub['60°C'] = 'N/A'
s410.solub['70°C'] = 'N/A'
s410.solub['80°C'] = 'N/A'
s410.solub['90°C'] = 'N/A'
s410.solub['100°C'] = 'N/A'
sublist.append(s410)

s411 = substance('Nickel(II) bromide', 'NiBr2')
s411.solub['0°C'] = '113'
s411.solub['10°C'] = '122'
s411.solub['20°C'] = '131'
s411.solub['30°C'] = '138'
s411.solub['40°C'] = '144'
s411.solub['50°C'] = 'N/A'
s411.solub['60°C'] = '153'
s411.solub['70°C'] = 'N/A'
s411.solub['80°C'] = '154'
s411.solub['90°C'] = 'N/A'
s411.solub['100°C'] = '155'
sublist.append(s411)

s412 = substance('Nickel(II) carbonate', 'NiCO3')
s412.solub['0°C'] = 'N/A'
s412.solub['10°C'] = 'N/A'
s412.solub['20°C'] = '9.643×10-4'
s412.solub['30°C'] = 'N/A'
s412.solub['40°C'] = 'N/A'
s412.solub['50°C'] = 'N/A'
s412.solub['60°C'] = 'N/A'
s412.solub['70°C'] = 'N/A'
s412.solub['80°C'] = 'N/A'
s412.solub['90°C'] = 'N/A'
s412.solub['100°C'] = 'N/A'
sublist.append(s412)

s413 = substance('Nickel(II) chlorate', 'Ni(ClO3)2')
s413.solub['0°C'] = '111'
s413.solub['10°C'] = '120'
s413.solub['20°C'] = '133'
s413.solub['30°C'] = '155'
s413.solub['40°C'] = '181'
s413.solub['50°C'] = 'N/A'
s413.solub['60°C'] = '221'
s413.solub['70°C'] = 'N/A'
s413.solub['80°C'] = '308'
s413.solub['90°C'] = 'N/A'
s413.solub['100°C'] = 'N/A'
sublist.append(s413)

s414 = substance('Nickel(II) chloride', 'NiCl2')
s414.solub['0°C'] = '53.4'
s414.solub['10°C'] = '56.3'
s414.solub['20°C'] = '66.8'
s414.solub['30°C'] = '70.6'
s414.solub['40°C'] = '73.2'
s414.solub['50°C'] = 'N/A'
s414.solub['60°C'] = '81.2'
s414.solub['70°C'] = 'N/A'
s414.solub['80°C'] = '86.6'
s414.solub['90°C'] = 'N/A'
s414.solub['100°C'] = '87.6'
sublist.append(s414)

s415 = substance('Nickel(II) fluoride', 'NiF2')
s415.solub['0°C'] = 'N/A'
s415.solub['10°C'] = '2.55'
s415.solub['20°C'] = '2.56'
s415.solub['30°C'] = 'N/A'
s415.solub['40°C'] = 'N/A'
s415.solub['50°C'] = 'N/A'
s415.solub['60°C'] = '2.56'
s415.solub['70°C'] = 'N/A'
s415.solub['80°C'] = 'N/A'
s415.solub['90°C'] = '2.59'
s415.solub['100°C'] = 'N/A'
sublist.append(s415)

s416 = substance('Nickel(II) formate', 'Ni(HCO2)2.2H2O')
s416.solub['0°C'] = 'N/A'
s416.solub['10°C'] = '3.15'
s416.solub['20°C'] = '3.25'
s416.solub['30°C'] = 'N/A'
s416.solub['40°C'] = 'N/A'
s416.solub['50°C'] = 'N/A'
s416.solub['60°C'] = 'N/A'
s416.solub['70°C'] = 'N/A'
s416.solub['80°C'] = 'N/A'
s416.solub['90°C'] = 'N/A'
s416.solub['100°C'] = 'N/A'
sublist.append(s416)

s417 = substance('Nickel(II) hydroxide', 'Ni(OH)2')
s417.solub['0°C'] = 'N/A'
s417.solub['10°C'] = 'N/A'
s417.solub['20°C'] = '0.013'
s417.solub['30°C'] = 'N/A'
s417.solub['40°C'] = 'N/A'
s417.solub['50°C'] = 'N/A'
s417.solub['60°C'] = 'N/A'
s417.solub['70°C'] = 'N/A'
s417.solub['80°C'] = 'N/A'
s417.solub['90°C'] = 'N/A'
s417.solub['100°C'] = 'N/A'
sublist.append(s417)

s418 = substance('Nickel(II) iodate', 'Ni(IO3)2')
s418.solub['0°C'] = '0.74'
s418.solub['10°C'] = 'N/A'
s418.solub['20°C'] = '0.062'
s418.solub['30°C'] = '1.43'
s418.solub['40°C'] = 'N/A'
s418.solub['50°C'] = 'N/A'
s418.solub['60°C'] = 'N/A'
s418.solub['70°C'] = 'N/A'
s418.solub['80°C'] = 'N/A'
s418.solub['90°C'] = 'N/A'
s418.solub['100°C'] = 'N/A'
sublist.append(s418)

s419 = substance('Nickel(II) iodide', 'NiI2')
s419.solub['0°C'] = '124'
s419.solub['10°C'] = '135'
s419.solub['20°C'] = '148'
s419.solub['30°C'] = '161'
s419.solub['40°C'] = '174'
s419.solub['50°C'] = 'N/A'
s419.solub['60°C'] = '184'
s419.solub['70°C'] = 'N/A'
s419.solub['80°C'] = '187'
s419.solub['90°C'] = '188'
s419.solub['100°C'] = 'N/A'
sublist.append(s419)

s420 = substance('Nickel(II) nitrate', 'Ni(NO3)2')
s420.solub['0°C'] = '79.2'
s420.solub['10°C'] = 'N/A'
s420.solub['20°C'] = '94.2'
s420.solub['30°C'] = '105'
s420.solub['40°C'] = '119'
s420.solub['50°C'] = 'N/A'
s420.solub['60°C'] = '158'
s420.solub['70°C'] = 'N/A'
s420.solub['80°C'] = '187'
s420.solub['90°C'] = '188'
s420.solub['100°C'] = 'N/A'
sublist.append(s420)

s421 = substance('Nickel oxalate', 'NiC2O4.2H2O')
s421.solub['0°C'] = 'N/A'
s421.solub['10°C'] = 'N/A'
s421.solub['20°C'] = '0.00118'
s421.solub['30°C'] = 'N/A'
s421.solub['40°C'] = 'N/A'
s421.solub['50°C'] = 'N/A'
s421.solub['60°C'] = 'N/A'
s421.solub['70°C'] = 'N/A'
s421.solub['80°C'] = 'N/A'
s421.solub['90°C'] = 'N/A'
s421.solub['100°C'] = 'N/A'
sublist.append(s421)

s422 = substance('Nickel(II) perchlorate', 'Ni(ClO4)2')
s422.solub['0°C'] = '105'
s422.solub['10°C'] = '107'
s422.solub['20°C'] = '110'
s422.solub['30°C'] = '113'
s422.solub['40°C'] = '117'
s422.solub['50°C'] = 'N/A'
s422.solub['60°C'] = 'N/A'
s422.solub['70°C'] = 'N/A'
s422.solub['80°C'] = 'N/A'
s422.solub['90°C'] = 'N/A'
s422.solub['100°C'] = 'N/A'
sublist.append(s422)

s423 = substance('Nickel(II) pyrophosphate', 'Ni2P2O7')
s423.solub['0°C'] = 'N/A'
s423.solub['10°C'] = 'N/A'
s423.solub['20°C'] = '0.001017'
s423.solub['30°C'] = 'N/A'
s423.solub['40°C'] = 'N/A'
s423.solub['50°C'] = 'N/A'
s423.solub['60°C'] = 'N/A'
s423.solub['70°C'] = 'N/A'
s423.solub['80°C'] = 'N/A'
s423.solub['90°C'] = 'N/A'
s423.solub['100°C'] = 'N/A'
sublist.append(s423)

s424 = substance('Nickel(II) sulfate', 'NiSO4.6H2O')
s424.solub['0°C'] = 'N/A'
s424.solub['10°C'] = 'N/A'
s424.solub['20°C'] = '44.4'
s424.solub['30°C'] = '46.6'
s424.solub['40°C'] = '49.2'
s424.solub['50°C'] = 'N/A'
s424.solub['60°C'] = '55.6'
s424.solub['70°C'] = 'N/A'
s424.solub['80°C'] = '64.5'
s424.solub['90°C'] = '70.1'
s424.solub['100°C'] = '76.7'
sublist.append(s424)

s425 = substance('Nitric oxide', 'NO')
s425.solub['0°C'] = 'N/A'
s425.solub['10°C'] = 'N/A'
s425.solub['20°C'] = '0.0056'
s425.solub['30°C'] = 'N/A'
s425.solub['40°C'] = 'N/A'
s425.solub['50°C'] = 'N/A'
s425.solub['60°C'] = 'N/A'
s425.solub['70°C'] = 'N/A'
s425.solub['80°C'] = 'N/A'
s425.solub['90°C'] = 'N/A'
s425.solub['100°C'] = 'N/A'
sublist.append(s425)

s426 = substance('Nitrous oxide', 'N2O')
s426.solub['0°C'] = 'N/A'
s426.solub['10°C'] = 'N/A'
s426.solub['20°C'] = '0.112'
s426.solub['30°C'] = 'N/A'
s426.solub['40°C'] = 'N/A'
s426.solub['50°C'] = 'N/A'
s426.solub['60°C'] = 'N/A'
s426.solub['70°C'] = 'N/A'
s426.solub['80°C'] = 'N/A'
s426.solub['90°C'] = 'N/A'
s426.solub['100°C'] = 'N/A'
sublist.append(s426)

s427 = substance('Oxygen', 'O2')
s427.solub['0°C'] = '0.00146'
s427.solub['10°C'] = '0.00113'
s427.solub['20°C'] = '0.00091'
s427.solub['30°C'] = '0.00076'
s427.solub['40°C'] = '0.00065'
s427.solub['50°C'] = 'N/A'
s427.solub['60°C'] = 'N/A'
s427.solub['70°C'] = 'N/A'
s427.solub['80°C'] = 'N/A'
s427.solub['90°C'] = 'N/A'
s427.solub['100°C'] = 'N/A'
sublist.append(s427)

s428 = substance('Oxalic acid', 'H2C2O4·2H2O')
s428.solub['0°C'] = '4.96'
s428.solub['10°C'] = '8.51'
s428.solub['20°C'] = '13.3'
s428.solub['30°C'] = '19.9'
s428.solub['40°C'] = '30.1'
s428.solub['50°C'] = 'N/A'
s428.solub['60°C'] = '62.1'
s428.solub['70°C'] = 'N/A'
s428.solub['80°C'] = '118'
s428.solub['90°C'] = '168'
s428.solub['100°C'] = 'N/A'
sublist.append(s428)

s429 = substance('Palladium(II) hydroxide', 'Pd(OH)2')
s429.solub['0°C'] = 'N/A'
s429.solub['10°C'] = 'N/A'
s429.solub['20°C'] = '4.106×10-10'
s429.solub['30°C'] = 'N/A'
s429.solub['40°C'] = 'N/A'
s429.solub['50°C'] = 'N/A'
s429.solub['60°C'] = 'N/A'
s429.solub['70°C'] = 'N/A'
s429.solub['80°C'] = 'N/A'
s429.solub['90°C'] = 'N/A'
s429.solub['100°C'] = 'N/A'
sublist.append(s429)

s430 = substance('Palladium(IV) hydroxide', 'Pd(OH)4')
s430.solub['0°C'] = 'N/A'
s430.solub['10°C'] = 'N/A'
s430.solub['20°C'] = '5.247×10-14'
s430.solub['30°C'] = 'N/A'
s430.solub['40°C'] = 'N/A'
s430.solub['50°C'] = 'N/A'
s430.solub['60°C'] = 'N/A'
s430.solub['70°C'] = 'N/A'
s430.solub['80°C'] = 'N/A'
s430.solub['90°C'] = 'N/A'
s430.solub['100°C'] = 'N/A'
sublist.append(s430)

s431 = substance('Phenol', 'C6H5OH')
s431.solub['0°C'] = 'N/A'
s431.solub['10°C'] = 'N/A'
s431.solub['20°C'] = '8.3'
s431.solub['30°C'] = 'N/A'
s431.solub['40°C'] = 'miscible'
s431.solub['50°C'] = 'N/A'
s431.solub['60°C'] = 'N/A'
s431.solub['70°C'] = 'N/A'
s431.solub['80°C'] = 'N/A'
s431.solub['90°C'] = 'N/A'
s431.solub['100°C'] = 'N/A'
sublist.append(s431)

s432 = substance('Platinum(II) hydroxide', 'Pt(OH)2')
s432.solub['0°C'] = 'N/A'
s432.solub['10°C'] = 'N/A'
s432.solub['20°C'] = '3.109×10-11'
s432.solub['30°C'] = 'N/A'
s432.solub['40°C'] = 'N/A'
s432.solub['50°C'] = 'N/A'
s432.solub['60°C'] = 'N/A'
s432.solub['70°C'] = 'N/A'
s432.solub['80°C'] = 'N/A'
s432.solub['90°C'] = 'N/A'
s432.solub['100°C'] = 'N/A'
sublist.append(s432)

s433 = substance('Platinum(IV) bromide', 'PtBr4')
s433.solub['0°C'] = 'N/A'
s433.solub['10°C'] = 'N/A'
s433.solub['20°C'] = '1.352×10-7'
s433.solub['30°C'] = 'N/A'
s433.solub['40°C'] = 'N/A'
s433.solub['50°C'] = 'N/A'
s433.solub['60°C'] = 'N/A'
s433.solub['70°C'] = 'N/A'
s433.solub['80°C'] = 'N/A'
s433.solub['90°C'] = 'N/A'
s433.solub['100°C'] = 'N/A'
sublist.append(s433)

s434 = substance('Plutonium(III) fluoride', 'PuF3')
s434.solub['0°C'] = 'N/A'
s434.solub['10°C'] = 'N/A'
s434.solub['20°C'] = '3.144×10-4'
s434.solub['30°C'] = 'N/A'
s434.solub['40°C'] = 'N/A'
s434.solub['50°C'] = 'N/A'
s434.solub['60°C'] = 'N/A'
s434.solub['70°C'] = 'N/A'
s434.solub['80°C'] = 'N/A'
s434.solub['90°C'] = 'N/A'
s434.solub['100°C'] = 'N/A'
sublist.append(s434)

s435 = substance('Plutonium(IV) fluoride', 'PuF4')
s435.solub['0°C'] = 'N/A'
s435.solub['10°C'] = 'N/A'
s435.solub['20°C'] = '3.622×10-4'
s435.solub['30°C'] = 'N/A'
s435.solub['40°C'] = 'N/A'
s435.solub['50°C'] = 'N/A'
s435.solub['60°C'] = 'N/A'
s435.solub['70°C'] = 'N/A'
s435.solub['80°C'] = 'N/A'
s435.solub['90°C'] = 'N/A'
s435.solub['100°C'] = 'N/A'
sublist.append(s435)

s436 = substance('Plutonium(IV) iodate', 'Pu(IO3)4')
s436.solub['0°C'] = 'N/A'
s436.solub['10°C'] = 'N/A'
s436.solub['20°C'] = '0.07998'
s436.solub['30°C'] = 'N/A'
s436.solub['40°C'] = 'N/A'
s436.solub['50°C'] = 'N/A'
s436.solub['60°C'] = 'N/A'
s436.solub['70°C'] = 'N/A'
s436.solub['80°C'] = 'N/A'
s436.solub['90°C'] = 'N/A'
s436.solub['100°C'] = 'N/A'
sublist.append(s436)

s437 = substance('Polonium(II) sulfide', 'PoS')
s437.solub['0°C'] = 'N/A'
s437.solub['10°C'] = 'N/A'
s437.solub['20°C'] = '2.378×10-14'
s437.solub['30°C'] = 'N/A'
s437.solub['40°C'] = 'N/A'
s437.solub['50°C'] = 'N/A'
s437.solub['60°C'] = 'N/A'
s437.solub['70°C'] = 'N/A'
s437.solub['80°C'] = 'N/A'
s437.solub['90°C'] = 'N/A'
s437.solub['100°C'] = 'N/A'
sublist.append(s437)

s438 = substance('Potassium acetate', 'KC2H3O2')
s438.solub['0°C'] = '216'
s438.solub['10°C'] = '233'
s438.solub['20°C'] = '256'
s438.solub['30°C'] = '283'
s438.solub['40°C'] = '324'
s438.solub['50°C'] = 'N/A'
s438.solub['60°C'] = '350'
s438.solub['70°C'] = 'N/A'
s438.solub['80°C'] = '381'
s438.solub['90°C'] = '398'
s438.solub['100°C'] = 'N/A'
sublist.append(s438)

s439 = substance('Potassium arsenate', 'K3AsO4')
s439.solub['0°C'] = 'N/A'
s439.solub['10°C'] = 'N/A'
s439.solub['20°C'] = '19'
s439.solub['30°C'] = 'N/A'
s439.solub['40°C'] = 'N/A'
s439.solub['50°C'] = 'N/A'
s439.solub['60°C'] = 'N/A'
s439.solub['70°C'] = 'N/A'
s439.solub['80°C'] = 'N/A'
s439.solub['90°C'] = 'N/A'
s439.solub['100°C'] = 'N/A'
sublist.append(s439)

s440 = substance('Potassium azide', 'KN3')
s440.solub['0°C'] = '41.4'
s440.solub['10°C'] = '46.2'
s440.solub['20°C'] = '50.8'
s440.solub['30°C'] = '55.8'
s440.solub['40°C'] = '61'
s440.solub['50°C'] = 'N/A'
s440.solub['60°C'] = 'N/A'
s440.solub['70°C'] = 'N/A'
s440.solub['80°C'] = 'N/A'
s440.solub['90°C'] = 'N/A'
s440.solub['100°C'] = '106'
sublist.append(s440)

s441 = substance('Potassium benzoate', 'KC7H5O2')
s441.solub['0°C'] = 'N/A'
s441.solub['10°C'] = '65.8'
s441.solub['20°C'] = '70.7'
s441.solub['30°C'] = '76.7'
s441.solub['40°C'] = '82.1'
s441.solub['50°C'] = 'N/A'
s441.solub['60°C'] = 'N/A'
s441.solub['70°C'] = 'N/A'
s441.solub['80°C'] = 'N/A'
s441.solub['90°C'] = 'N/A'
s441.solub['100°C'] = 'N/A'
sublist.append(s441)

s442 = substance('Potassium bromate', 'KBrO3')
s442.solub['0°C'] = '3.09'
s442.solub['10°C'] = '4.72'
s442.solub['20°C'] = '6.91'
s442.solub['30°C'] = '9.64'
s442.solub['40°C'] = '13.1'
s442.solub['50°C'] = 'N/A'
s442.solub['60°C'] = '22.7'
s442.solub['70°C'] = 'N/A'
s442.solub['80°C'] = '34.1'
s442.solub['90°C'] = 'N/A'
s442.solub['100°C'] = '49.9'
sublist.append(s442)

s443 = substance('Potassium bromide', 'KBr')
s443.solub['0°C'] = '53.6'
s443.solub['10°C'] = '59.5'
s443.solub['20°C'] = '65.3'
s443.solub['30°C'] = '70.7'
s443.solub['40°C'] = '75.4'
s443.solub['50°C'] = 'N/A'
s443.solub['60°C'] = '85.5'
s443.solub['70°C'] = 'N/A'
s443.solub['80°C'] = '94.9'
s443.solub['90°C'] = '99.2'
s443.solub['100°C'] = '104'
sublist.append(s443)

s444 = substance('Potassium hexabromoplatinate', 'K2PtBr6')
s444.solub['0°C'] = 'N/A'
s444.solub['10°C'] = 'N/A'
s444.solub['20°C'] = '1.89'
s444.solub['30°C'] = 'N/A'
s444.solub['40°C'] = 'N/A'
s444.solub['50°C'] = 'N/A'
s444.solub['60°C'] = 'N/A'
s444.solub['70°C'] = 'N/A'
s444.solub['80°C'] = 'N/A'
s444.solub['90°C'] = 'N/A'
s444.solub['100°C'] = 'N/A'
sublist.append(s444)

s445 = substance('Potassium carbonate', 'K2CO3')
s445.solub['0°C'] = '105'
s445.solub['10°C'] = '109'
s445.solub['20°C'] = '111'
s445.solub['30°C'] = '114'
s445.solub['40°C'] = '117'
s445.solub['50°C'] = '121.2'
s445.solub['60°C'] = '127'
s445.solub['70°C'] = 'N/A'
s445.solub['80°C'] = '140'
s445.solub['90°C'] = '148'
s445.solub['100°C'] = '156'
sublist.append(s445)

s446 = substance('Potassium chlorate', 'KClO3')
s446.solub['0°C'] = '3.3'
s446.solub['10°C'] = '5.2'
s446.solub['20°C'] = '7.3'
s446.solub['30°C'] = '10.1'
s446.solub['40°C'] = '13.9'
s446.solub['50°C'] = 'N/A'
s446.solub['60°C'] = '23.8'
s446.solub['70°C'] = 'N/A'
s446.solub['80°C'] = '37.5'
s446.solub['90°C'] = '46'
s446.solub['100°C'] = '56.3'
sublist.append(s446)

s447 = substance('Potassium chloride', 'KCl')
s447.solub['0°C'] = '28'
s447.solub['10°C'] = '31.2'
s447.solub['20°C'] = '34.2'
s447.solub['30°C'] = '37.2'
s447.solub['40°C'] = '40.1'
s447.solub['50°C'] = '42.6'
s447.solub['60°C'] = '45.8'
s447.solub['70°C'] = 'N/A'
s447.solub['80°C'] = '51.3'
s447.solub['90°C'] = '53.9'
s447.solub['100°C'] = '56.3'
sublist.append(s447)

s448 = substance('Potassium chromate', 'K2CrO4')
s448.solub['0°C'] = '56.3'
s448.solub['10°C'] = '60'
s448.solub['20°C'] = '63.7'
s448.solub['30°C'] = '66.7'
s448.solub['40°C'] = '67.8'
s448.solub['50°C'] = 'N/A'
s448.solub['60°C'] = '70.1'
s448.solub['70°C'] = 'N/A'
s448.solub['80°C'] = 'N/A'
s448.solub['90°C'] = '74.5'
s448.solub['100°C'] = 'N/A'
sublist.append(s448)

s449 = substance('Potassium cyanide', 'KCN')
s449.solub['0°C'] = 'N/A'
s449.solub['10°C'] = 'N/A'
s449.solub['20°C'] = '50'
s449.solub['30°C'] = 'N/A'
s449.solub['40°C'] = 'N/A'
s449.solub['50°C'] = 'N/A'
s449.solub['60°C'] = 'N/A'
s449.solub['70°C'] = 'N/A'
s449.solub['80°C'] = 'N/A'
s449.solub['90°C'] = 'N/A'
s449.solub['100°C'] = 'N/A'
sublist.append(s449)

s450 = substance('Potassium dichromate', 'K2Cr2O7')
s450.solub['0°C'] = '4.7'
s450.solub['10°C'] = '7'
s450.solub['20°C'] = '12.3'
s450.solub['30°C'] = '18.1'
s450.solub['40°C'] = '26.3'
s450.solub['50°C'] = '34'
s450.solub['60°C'] = '45.6'
s450.solub['70°C'] = 'N/A'
s450.solub['80°C'] = '73'
s450.solub['90°C'] = 'N/A'
s450.solub['100°C'] = 'N/A'
sublist.append(s450)

s451 = substance('Potassium dihydrogen arsenate', 'KH2AsO4')
s451.solub['0°C'] = 'N/A'
s451.solub['10°C'] = 'N/A'
s451.solub['20°C'] = '19'
s451.solub['30°C'] = 'N/A'
s451.solub['40°C'] = 'N/A'
s451.solub['50°C'] = 'N/A'
s451.solub['60°C'] = 'N/A'
s451.solub['70°C'] = 'N/A'
s451.solub['80°C'] = 'N/A'
s451.solub['90°C'] = 'N/A'
s451.solub['100°C'] = 'N/A'
sublist.append(s451)

s452 = substance('Potassium dihydrogen phosphate', 'KH2PO4')
s452.solub['0°C'] = '14.8'
s452.solub['10°C'] = '18.3'
s452.solub['20°C'] = '22.6'
s452.solub['30°C'] = '28'
s452.solub['40°C'] = '35.5'
s452.solub['50°C'] = '41'
s452.solub['60°C'] = '50.2'
s452.solub['70°C'] = 'N/A'
s452.solub['80°C'] = '70.4'
s452.solub['90°C'] = '83.5'
s452.solub['100°C'] = 'N/A'
sublist.append(s452)

s453 = substance('Potassium ferricyanide', 'K3Fe(CN)6')
s453.solub['0°C'] = '30.2'
s453.solub['10°C'] = '38'
s453.solub['20°C'] = '46'
s453.solub['30°C'] = '53'
s453.solub['40°C'] = '59.3'
s453.solub['50°C'] = 'N/A'
s453.solub['60°C'] = '70'
s453.solub['70°C'] = 'N/A'
s453.solub['80°C'] = 'N/A'
s453.solub['90°C'] = 'N/A'
s453.solub['100°C'] = '91'
sublist.append(s453)

s454 = substance('Potassium ferrocyanide', 'K4Fe(CN)6')
s454.solub['0°C'] = '14.3'
s454.solub['10°C'] = '21.1'
s454.solub['20°C'] = '28.2'
s454.solub['30°C'] = '35.1'
s454.solub['40°C'] = '41.4'
s454.solub['50°C'] = 'N/A'
s454.solub['60°C'] = '54.8'
s454.solub['70°C'] = 'N/A'
s454.solub['80°C'] = '66.9'
s454.solub['90°C'] = '71.5'
s454.solub['100°C'] = '74.2'
sublist.append(s454)

s455 = substance('Potassium fluoride', 'KF')
s455.solub['0°C'] = '44.7'
s455.solub['10°C'] = '53.5'
s455.solub['20°C'] = '94.9'
s455.solub['30°C'] = '108'
s455.solub['40°C'] = '138'
s455.solub['50°C'] = 'N/A'
s455.solub['60°C'] = '142'
s455.solub['70°C'] = 'N/A'
s455.solub['80°C'] = '150'
s455.solub['90°C'] = 'N/A'
s455.solub['100°C'] = 'N/A'
sublist.append(s455)

s456 = substance('Potassium formate', 'KHCO2')
s456.solub['0°C'] = '32.8'
s456.solub['10°C'] = '313'
s456.solub['20°C'] = '337'
s456.solub['30°C'] = '361'
s456.solub['40°C'] = '398'
s456.solub['50°C'] = 'N/A'
s456.solub['60°C'] = '471'
s456.solub['70°C'] = 'N/A'
s456.solub['80°C'] = '580'
s456.solub['90°C'] = '658'
s456.solub['100°C'] = 'N/A'
sublist.append(s456)

s457 = substance('Potassium hydrogen carbonate', 'KHCO3')
s457.solub['0°C'] = '22.5'
s457.solub['10°C'] = '27.4'
s457.solub['20°C'] = '33.7'
s457.solub['30°C'] = '39.9'
s457.solub['40°C'] = '47.5'
s457.solub['50°C'] = 'N/A'
s457.solub['60°C'] = '65.6'
s457.solub['70°C'] = 'N/A'
s457.solub['80°C'] = 'N/A'
s457.solub['90°C'] = 'N/A'
s457.solub['100°C'] = 'N/A'
sublist.append(s457)

s458 = substance('Potassium hydrogen phosphate', 'K2HPO4')
s458.solub['0°C'] = 'N/A'
s458.solub['10°C'] = 'N/A'
s458.solub['20°C'] = '150'
s458.solub['30°C'] = 'N/A'
s458.solub['40°C'] = 'N/A'
s458.solub['50°C'] = 'N/A'
s458.solub['60°C'] = 'N/A'
s458.solub['70°C'] = 'N/A'
s458.solub['80°C'] = 'N/A'
s458.solub['90°C'] = 'N/A'
s458.solub['100°C'] = 'N/A'
sublist.append(s458)

s459 = substance('Potassium hydrogen sulfate', 'KHSO4')
s459.solub['0°C'] = '36.2'
s459.solub['10°C'] = 'N/A'
s459.solub['20°C'] = '48.6'
s459.solub['30°C'] = '54.3'
s459.solub['40°C'] = '61'
s459.solub['50°C'] = 'N/A'
s459.solub['60°C'] = '76.4'
s459.solub['70°C'] = 'N/A'
s459.solub['80°C'] = '96.1'
s459.solub['90°C'] = 'N/A'
s459.solub['100°C'] = '122'
sublist.append(s459)

s460 = substance('Potassium hydrogen tartrate', 'KHC4H4O6')
s460.solub['0°C'] = 'N/A'
s460.solub['10°C'] = 'N/A'
s460.solub['20°C'] = '0.6'
s460.solub['30°C'] = 'N/A'
s460.solub['40°C'] = 'N/A'
s460.solub['50°C'] = 'N/A'
s460.solub['60°C'] = 'N/A'
s460.solub['70°C'] = 'N/A'
s460.solub['80°C'] = 'N/A'
s460.solub['90°C'] = 'N/A'
s460.solub['100°C'] = '62'
sublist.append(s460)

s461 = substance('Potassium hydroxide', 'KOH')
s461.solub['0°C'] = '95.7'
s461.solub['10°C'] = '103'
s461.solub['20°C'] = '112'
s461.solub['30°C'] = '126'
s461.solub['40°C'] = '134'
s461.solub['50°C'] = 'N/A'
s461.solub['60°C'] = '154'
s461.solub['70°C'] = 'N/A'
s461.solub['80°C'] = 'N/A'
s461.solub['90°C'] = 'N/A'
s461.solub['100°C'] = '178'
sublist.append(s461)

s462 = substance('Potassium iodate', 'KIO3')
s462.solub['0°C'] = '4.6'
s462.solub['10°C'] = '6.27'
s462.solub['20°C'] = '8.08'
s462.solub['30°C'] = '10.3'
s462.solub['40°C'] = '12.6'
s462.solub['50°C'] = '14'
s462.solub['60°C'] = '18.3'
s462.solub['70°C'] = 'N/A'
s462.solub['80°C'] = '24.8'
s462.solub['90°C'] = 'N/A'
s462.solub['100°C'] = '32.3'
sublist.append(s462)

s463 = substance('Potassium iodide', 'KI')
s463.solub['0°C'] = '128'
s463.solub['10°C'] = '136'
s463.solub['20°C'] = '144'
s463.solub['30°C'] = '153'
s463.solub['40°C'] = '162'
s463.solub['50°C'] = 'N/A'
s463.solub['60°C'] = '176'
s463.solub['70°C'] = 'N/A'
s463.solub['80°C'] = '192'
s463.solub['90°C'] = '198'
s463.solub['100°C'] = '206'
sublist.append(s463)

s464 = substance('Potassium metabisulfite', 'K2S2O5')
s464.solub['0°C'] = 'N/A'
s464.solub['10°C'] = 'N/A'
s464.solub['20°C'] = 'N/A'
s464.solub['30°C'] = '45'
s464.solub['40°C'] = 'N/A'
s464.solub['50°C'] = 'N/A'
s464.solub['60°C'] = 'N/A'
s464.solub['70°C'] = 'N/A'
s464.solub['80°C'] = 'N/A'
s464.solub['90°C'] = 'N/A'
s464.solub['100°C'] = 'N/A'
sublist.append(s464)

s465 = substance('Potassium nitrate', 'KNO3')
s465.solub['0°C'] = '13.3'
s465.solub['10°C'] = '20.9'
s465.solub['20°C'] = '31.6'
s465.solub['30°C'] = '45.8'
s465.solub['40°C'] = '63.9'
s465.solub['50°C'] = '85.5'
s465.solub['60°C'] = '110.0'
s465.solub['70°C'] = '138'
s465.solub['80°C'] = '169'
s465.solub['90°C'] = '202'
s465.solub['100°C'] = '246'
sublist.append(s465)

s466 = substance('Potassium nitrite', 'KNO2')
s466.solub['0°C'] = '279'
s466.solub['10°C'] = '292'
s466.solub['20°C'] = '306'
s466.solub['30°C'] = '320'
s466.solub['40°C'] = '329'
s466.solub['50°C'] = 'N/A'
s466.solub['60°C'] = '348'
s466.solub['70°C'] = 'N/A'
s466.solub['80°C'] = '376'
s466.solub['90°C'] = '390'
s466.solub['100°C'] = '410'
sublist.append(s466)

s467 = substance('Potassium oxalate', 'K2C2O4')
s467.solub['0°C'] = '25.5'
s467.solub['10°C'] = '31.9'
s467.solub['20°C'] = '36.4'
s467.solub['30°C'] = '39.9'
s467.solub['40°C'] = '43.8'
s467.solub['50°C'] = 'N/A'
s467.solub['60°C'] = '53.2'
s467.solub['70°C'] = 'N/A'
s467.solub['80°C'] = '63.6'
s467.solub['90°C'] = '69.2'
s467.solub['100°C'] = '75.3'
sublist.append(s467)

s468 = substance('Potassium perchlorate', 'KClO4')
s468.solub['0°C'] = '0.76'
s468.solub['10°C'] = '1.06'
s468.solub['20°C'] = '1.68'
s468.solub['30°C'] = '2.56'
s468.solub['40°C'] = '3.73'
s468.solub['50°C'] = 'N/A'
s468.solub['60°C'] = '7.3'
s468.solub['70°C'] = 'N/A'
s468.solub['80°C'] = '13.4'
s468.solub['90°C'] = '17.7'
s468.solub['100°C'] = '22.3'
sublist.append(s468)

s469 = substance('Potassium periodate', 'KIO4')
s469.solub['0°C'] = '0.17'
s469.solub['10°C'] = '0.28'
s469.solub['20°C'] = '0.42'
s469.solub['30°C'] = '0.65'
s469.solub['40°C'] = '1'
s469.solub['50°C'] = 'N/A'
s469.solub['60°C'] = '2.1'
s469.solub['70°C'] = 'N/A'
s469.solub['80°C'] = '4.4'
s469.solub['90°C'] = '5.9'
s469.solub['100°C'] = 'N/A'
sublist.append(s469)

s470 = substance('Potassium permanganate', 'KMnO4')
s470.solub['0°C'] = '2.83'
s470.solub['10°C'] = '4.31'
s470.solub['20°C'] = '6.34'
s470.solub['30°C'] = '9.03'
s470.solub['40°C'] = '12.6'
s470.solub['50°C'] = '16.9'
s470.solub['60°C'] = '22.1'
s470.solub['70°C'] = 'N/A'
s470.solub['80°C'] = 'N/A'
s470.solub['90°C'] = 'N/A'
s470.solub['100°C'] = 'N/A'
sublist.append(s470)

s471 = substance('Potassium persulfate', 'K2S2O8')
s471.solub['0°C'] = 'N/A'
s471.solub['10°C'] = 'N/A'
s471.solub['20°C'] = '4.7'
s471.solub['30°C'] = 'N/A'
s471.solub['40°C'] = 'N/A'
s471.solub['50°C'] = 'N/A'
s471.solub['60°C'] = 'N/A'
s471.solub['70°C'] = 'N/A'
s471.solub['80°C'] = 'N/A'
s471.solub['90°C'] = 'N/A'
s471.solub['100°C'] = 'N/A'
sublist.append(s471)

s472 = substance('Potassium phosphate', 'K3PO4')
s472.solub['0°C'] = 'N/A'
s472.solub['10°C'] = '81.5'
s472.solub['20°C'] = '92.3'
s472.solub['30°C'] = '108'
s472.solub['40°C'] = '133'
s472.solub['50°C'] = 'N/A'
s472.solub['60°C'] = 'N/A'
s472.solub['70°C'] = 'N/A'
s472.solub['80°C'] = 'N/A'
s472.solub['90°C'] = 'N/A'
s472.solub['100°C'] = 'N/A'
sublist.append(s472)

s473 = substance('Potassium selenate', 'K2SeO4')
s473.solub['0°C'] = '107'
s473.solub['10°C'] = '109'
s473.solub['20°C'] = '111'
s473.solub['30°C'] = '113'
s473.solub['40°C'] = '115'
s473.solub['50°C'] = 'N/A'
s473.solub['60°C'] = '119'
s473.solub['70°C'] = 'N/A'
s473.solub['80°C'] = '121'
s473.solub['90°C'] = 'N/A'
s473.solub['100°C'] = '122'
sublist.append(s473)

s474 = substance('Potassium sulfate', 'K2SO4')
s474.solub['0°C'] = '7.4'
s474.solub['10°C'] = '9.3'
s474.solub['20°C'] = '11.1'
s474.solub['30°C'] = '13'
s474.solub['40°C'] = '14.8'
s474.solub['50°C'] = 'N/A'
s474.solub['60°C'] = '18.2'
s474.solub['70°C'] = 'N/A'
s474.solub['80°C'] = '21.4'
s474.solub['90°C'] = '22.9'
s474.solub['100°C'] = '24.1'
sublist.append(s474)

s475 = substance('Potassium tetraphenylborate', 'KB(C6H5)4')
s475.solub['0°C'] = 'N/A'
s475.solub['10°C'] = 'N/A'
s475.solub['20°C'] = '1.8×10-5'
s475.solub['30°C'] = 'N/A'
s475.solub['40°C'] = 'N/A'
s475.solub['50°C'] = 'N/A'
s475.solub['60°C'] = 'N/A'
s475.solub['70°C'] = 'N/A'
s475.solub['80°C'] = 'N/A'
s475.solub['90°C'] = 'N/A'
s475.solub['100°C'] = 'N/A'
sublist.append(s475)

s476 = substance('Potassium thiocyanate', 'KSCN')
s476.solub['0°C'] = '177'
s476.solub['10°C'] = '198'
s476.solub['20°C'] = '224'
s476.solub['30°C'] = '255'
s476.solub['40°C'] = '289'
s476.solub['50°C'] = 'N/A'
s476.solub['60°C'] = '372'
s476.solub['70°C'] = 'N/A'
s476.solub['80°C'] = '492'
s476.solub['90°C'] = '571'
s476.solub['100°C'] = '675'
sublist.append(s476)

s477 = substance('Potassium thiosulfate', 'K2S2O3')
s477.solub['0°C'] = '96'
s477.solub['10°C'] = 'N/A'
s477.solub['20°C'] = '155'
s477.solub['30°C'] = '175'
s477.solub['40°C'] = '205'
s477.solub['50°C'] = 'N/A'
s477.solub['60°C'] = '238'
s477.solub['70°C'] = 'N/A'
s477.solub['80°C'] = '293'
s477.solub['90°C'] = '312'
s477.solub['100°C'] = 'N/A'
sublist.append(s477)

s478 = substance('Potassium tungstate', 'K2WO4')
s478.solub['0°C'] = 'N/A'
s478.solub['10°C'] = 'N/A'
s478.solub['20°C'] = '51.5'
s478.solub['30°C'] = 'N/A'
s478.solub['40°C'] = 'N/A'
s478.solub['50°C'] = 'N/A'
s478.solub['60°C'] = 'N/A'
s478.solub['70°C'] = 'N/A'
s478.solub['80°C'] = 'N/A'
s478.solub['90°C'] = 'N/A'
s478.solub['100°C'] = 'N/A'
sublist.append(s478)

s479 = substance('Praseodymium(III) acetate', 'Pr(C2H3O2)3.H2O')
s479.solub['0°C'] = 'N/A'
s479.solub['10°C'] = 'N/A'
s479.solub['20°C'] = '32'
s479.solub['30°C'] = 'N/A'
s479.solub['40°C'] = 'N/A'
s479.solub['50°C'] = 'N/A'
s479.solub['60°C'] = 'N/A'
s479.solub['70°C'] = 'N/A'
s479.solub['80°C'] = 'N/A'
s479.solub['90°C'] = 'N/A'
s479.solub['100°C'] = 'N/A'
sublist.append(s479)

s480 = substance('Praseodymium(III) bromate', 'Pr(BrO3)3')
s480.solub['0°C'] = '55.9'
s480.solub['10°C'] = '73'
s480.solub['20°C'] = '91.8'
s480.solub['30°C'] = '114'
s480.solub['40°C'] = '144'
s480.solub['50°C'] = 'N/A'
s480.solub['60°C'] = 'N/A'
s480.solub['70°C'] = 'N/A'
s480.solub['80°C'] = 'N/A'
s480.solub['90°C'] = 'N/A'
s480.solub['100°C'] = 'N/A'
sublist.append(s480)

s481 = substance('Praseodymium(III) chloride', 'PrCl3')
s481.solub['0°C'] = 'N/A'
s481.solub['10°C'] = 'N/A'
s481.solub['20°C'] = '104'
s481.solub['30°C'] = 'N/A'
s481.solub['40°C'] = 'N/A'
s481.solub['50°C'] = 'N/A'
s481.solub['60°C'] = 'N/A'
s481.solub['70°C'] = 'N/A'
s481.solub['80°C'] = 'N/A'
s481.solub['90°C'] = 'N/A'
s481.solub['100°C'] = 'N/A'
sublist.append(s481)

s482 = substance('Praseodymium(III) molybdate', 'Pr2(MoO4)3')
s482.solub['0°C'] = 'N/A'
s482.solub['10°C'] = 'N/A'
s482.solub['20°C'] = '0.0015'
s482.solub['30°C'] = 'N/A'
s482.solub['40°C'] = 'N/A'
s482.solub['50°C'] = 'N/A'
s482.solub['60°C'] = 'N/A'
s482.solub['70°C'] = 'N/A'
s482.solub['80°C'] = 'N/A'
s482.solub['90°C'] = 'N/A'
s482.solub['100°C'] = 'N/A'
sublist.append(s482)

s483 = substance('Praseodymium(III) nitrate', 'Pr(NO3)3')
s483.solub['0°C'] = 'N/A'
s483.solub['10°C'] = 'N/A'
s483.solub['20°C'] = '112'
s483.solub['30°C'] = '162'
s483.solub['40°C'] = '178'
s483.solub['50°C'] = 'N/A'
s483.solub['60°C'] = 'N/A'
s483.solub['70°C'] = 'N/A'
s483.solub['80°C'] = 'N/A'
s483.solub['90°C'] = 'N/A'
s483.solub['100°C'] = 'N/A'
sublist.append(s483)

s484 = substance('Praseodymium(III) sulfate', 'Pr2(SO4)3')
s484.solub['0°C'] = '19.8'
s484.solub['10°C'] = '15.6'
s484.solub['20°C'] = '12.6'
s484.solub['30°C'] = '9.89'
s484.solub['40°C'] = '2.56'
s484.solub['50°C'] = 'N/A'
s484.solub['60°C'] = '5.04'
s484.solub['70°C'] = 'N/A'
s484.solub['80°C'] = '3.5'
s484.solub['90°C'] = '1.1'
s484.solub['100°C'] = '0.91'
sublist.append(s484)

s485 = substance('Radium chloride', 'RaCl2')
s485.solub['0°C'] = 'N/A'
s485.solub['10°C'] = 'N/A'
s485.solub['20°C'] = '19.6'
s485.solub['30°C'] = 'N/A'
s485.solub['40°C'] = 'N/A'
s485.solub['50°C'] = 'N/A'
s485.solub['60°C'] = 'N/A'
s485.solub['70°C'] = 'N/A'
s485.solub['80°C'] = 'N/A'
s485.solub['90°C'] = 'N/A'
s485.solub['100°C'] = 'N/A'
sublist.append(s485)

s486 = substance('Radium iodate', 'Ra(IO3)2')
s486.solub['0°C'] = 'N/A'
s486.solub['10°C'] = 'N/A'
s486.solub['20°C'] = '0.04'
s486.solub['30°C'] = 'N/A'
s486.solub['40°C'] = 'N/A'
s486.solub['50°C'] = 'N/A'
s486.solub['60°C'] = 'N/A'
s486.solub['70°C'] = 'N/A'
s486.solub['80°C'] = 'N/A'
s486.solub['90°C'] = 'N/A'
s486.solub['100°C'] = 'N/A'
sublist.append(s486)

s487 = substance('Radium nitrate', 'Ra(NO3)2')
s487.solub['0°C'] = 'N/A'
s487.solub['10°C'] = 'N/A'
s487.solub['20°C'] = '12'
s487.solub['30°C'] = 'N/A'
s487.solub['40°C'] = 'N/A'
s487.solub['50°C'] = 'N/A'
s487.solub['60°C'] = 'N/A'
s487.solub['70°C'] = 'N/A'
s487.solub['80°C'] = 'N/A'
s487.solub['90°C'] = 'N/A'
s487.solub['100°C'] = 'N/A'
sublist.append(s487)

s488 = substance('Radium sulfate', 'RaSO4')
s488.solub['0°C'] = 'N/A'
s488.solub['10°C'] = 'N/A'
s488.solub['20°C'] = '2.1×10-4'
s488.solub['30°C'] = 'N/A'
s488.solub['40°C'] = 'N/A'
s488.solub['50°C'] = 'N/A'
s488.solub['60°C'] = 'N/A'
s488.solub['70°C'] = 'N/A'
s488.solub['80°C'] = 'N/A'
s488.solub['90°C'] = 'N/A'
s488.solub['100°C'] = 'N/A'
sublist.append(s488)

s489 = substance('Raffinose', 'C18H32O16.5H2O')
s489.solub['0°C'] = 'N/A'
s489.solub['10°C'] = 'N/A'
s489.solub['20°C'] = '14'
s489.solub['30°C'] = 'N/A'
s489.solub['40°C'] = 'N/A'
s489.solub['50°C'] = 'N/A'
s489.solub['60°C'] = 'N/A'
s489.solub['70°C'] = 'N/A'
s489.solub['80°C'] = 'N/A'
s489.solub['90°C'] = 'N/A'
s489.solub['100°C'] = 'N/A'
sublist.append(s489)

s490 = substance('Rubidium acetate', 'RbC2H3O2')
s490.solub['0°C'] = 'N/A'
s490.solub['10°C'] = 'N/A'
s490.solub['20°C'] = 'N/A'
s490.solub['30°C'] = 'N/A'
s490.solub['40°C'] = '86'
s490.solub['50°C'] = 'N/A'
s490.solub['60°C'] = 'N/A'
s490.solub['70°C'] = 'N/A'
s490.solub['80°C'] = 'N/A'
s490.solub['90°C'] = 'N/A'
s490.solub['100°C'] = 'N/A'
sublist.append(s490)

s491 = substance('Rubidium bromate', 'RbBrO3')
s491.solub['0°C'] = 'N/A'
s491.solub['10°C'] = 'N/A'
s491.solub['20°C'] = 'N/A'
s491.solub['30°C'] = '3.6'
s491.solub['40°C'] = '5.1'
s491.solub['50°C'] = 'N/A'
s491.solub['60°C'] = 'N/A'
s491.solub['70°C'] = 'N/A'
s491.solub['80°C'] = 'N/A'
s491.solub['90°C'] = 'N/A'
s491.solub['100°C'] = 'N/A'
sublist.append(s491)

s492 = substance('Rubidium bromide', 'RbBr')
s492.solub['0°C'] = '90'
s492.solub['10°C'] = '99'
s492.solub['20°C'] = '108'
s492.solub['30°C'] = '119'
s492.solub['40°C'] = '132'
s492.solub['50°C'] = 'N/A'
s492.solub['60°C'] = '158'
s492.solub['70°C'] = 'N/A'
s492.solub['80°C'] = 'N/A'
s492.solub['90°C'] = 'N/A'
s492.solub['100°C'] = 'N/A'
sublist.append(s492)

s493 = substance('Rubidium chlorate', 'RbClO3')
s493.solub['0°C'] = '2.1'
s493.solub['10°C'] = '3.1'
s493.solub['20°C'] = '5.4'
s493.solub['30°C'] = '8'
s493.solub['40°C'] = '11.6'
s493.solub['50°C'] = 'N/A'
s493.solub['60°C'] = '22'
s493.solub['70°C'] = 'N/A'
s493.solub['80°C'] = '38'
s493.solub['90°C'] = '49'
s493.solub['100°C'] = '63'
sublist.append(s493)

s494 = substance('Rubidium chloride', 'RbCl')
s494.solub['0°C'] = '77'
s494.solub['10°C'] = '84'
s494.solub['20°C'] = '91'
s494.solub['30°C'] = '98'
s494.solub['40°C'] = '104'
s494.solub['50°C'] = 'N/A'
s494.solub['60°C'] = '115'
s494.solub['70°C'] = 'N/A'
s494.solub['80°C'] = '127'
s494.solub['90°C'] = '133'
s494.solub['100°C'] = '143'
sublist.append(s494)

s495 = substance('Rubidium chromate', 'Rb2CrO4')
s495.solub['0°C'] = '62'
s495.solub['10°C'] = '67.5'
s495.solub['20°C'] = '73.6'
s495.solub['30°C'] = '78.9'
s495.solub['40°C'] = '85.6'
s495.solub['50°C'] = 'N/A'
s495.solub['60°C'] = '95.7'
s495.solub['70°C'] = 'N/A'
s495.solub['80°C'] = 'N/A'
s495.solub['90°C'] = 'N/A'
s495.solub['100°C'] = 'N/A'
sublist.append(s495)

s496 = substance('Rubidium dichromate', 'Rb2Cr2O7')
s496.solub['0°C'] = 'N/A'
s496.solub['10°C'] = 'N/A'
s496.solub['20°C'] = '5.9'
s496.solub['30°C'] = '10'
s496.solub['40°C'] = '15.2'
s496.solub['50°C'] = 'N/A'
s496.solub['60°C'] = '32.3'
s496.solub['70°C'] = 'N/A'
s496.solub['80°C'] = 'N/A'
s496.solub['90°C'] = 'N/A'
s496.solub['100°C'] = 'N/A'
sublist.append(s496)

s497 = substance('Rubidium fluoride', 'RbF')
s497.solub['0°C'] = 'N/A'
s497.solub['10°C'] = 'N/A'
s497.solub['20°C'] = '130.6(18°C)'
s497.solub['30°C'] = 'N/A'
s497.solub['40°C'] = 'N/A'
s497.solub['50°C'] = 'N/A'
s497.solub['60°C'] = 'N/A'
s497.solub['70°C'] = 'N/A'
s497.solub['80°C'] = 'N/A'
s497.solub['90°C'] = 'N/A'
s497.solub['100°C'] = 'N/A'
sublist.append(s497)

s498 = substance('Rubidium fluorosilicate', 'Rb2SiF6')
s498.solub['0°C'] = 'N/A'
s498.solub['10°C'] = 'N/A'
s498.solub['20°C'] = '0.157'
s498.solub['30°C'] = 'N/A'
s498.solub['40°C'] = 'N/A'
s498.solub['50°C'] = 'N/A'
s498.solub['60°C'] = 'N/A'
s498.solub['70°C'] = 'N/A'
s498.solub['80°C'] = 'N/A'
s498.solub['90°C'] = 'N/A'
s498.solub['100°C'] = 'N/A'
sublist.append(s498)

s499 = substance('Rubidium formate', 'RbHCO2')
s499.solub['0°C'] = 'N/A'
s499.solub['10°C'] = '443'
s499.solub['20°C'] = '554'
s499.solub['30°C'] = '614'
s499.solub['40°C'] = '694'
s499.solub['50°C'] = 'N/A'
s499.solub['60°C'] = '900'
s499.solub['70°C'] = 'N/A'
s499.solub['80°C'] = 'N/A'
s499.solub['90°C'] = 'N/A'
s499.solub['100°C'] = 'N/A'
sublist.append(s499)

s500 = substance('Rubidium hydrogen carbonate', 'RbHCO3')
s500.solub['0°C'] = 'N/A'
s500.solub['10°C'] = 'N/A'
s500.solub['20°C'] = '110'
s500.solub['30°C'] = 'N/A'
s500.solub['40°C'] = 'N/A'
s500.solub['50°C'] = 'N/A'
s500.solub['60°C'] = 'N/A'
s500.solub['70°C'] = 'N/A'
s500.solub['80°C'] = 'N/A'
s500.solub['90°C'] = 'N/A'
s500.solub['100°C'] = 'N/A'
sublist.append(s500)

s501 = substance('Rubidium hydroxide', 'RbOH')
s501.solub['0°C'] = 'N/A'
s501.solub['10°C'] = 'N/A'
s501.solub['20°C'] = '180'
s501.solub['30°C'] = 'N/A'
s501.solub['40°C'] = 'N/A'
s501.solub['50°C'] = 'N/A'
s501.solub['60°C'] = 'N/A'
s501.solub['70°C'] = 'N/A'
s501.solub['80°C'] = 'N/A'
s501.solub['90°C'] = 'N/A'
s501.solub['100°C'] = 'N/A'
sublist.append(s501)

s502 = substance('Rubidium iodate', 'RbIO3')
s502.solub['0°C'] = 'N/A'
s502.solub['10°C'] = 'N/A'
s502.solub['20°C'] = '1.96'
s502.solub['30°C'] = 'N/A'
s502.solub['40°C'] = 'N/A'
s502.solub['50°C'] = 'N/A'
s502.solub['60°C'] = 'N/A'
s502.solub['70°C'] = 'N/A'
s502.solub['80°C'] = 'N/A'
s502.solub['90°C'] = 'N/A'
s502.solub['100°C'] = 'N/A'
sublist.append(s502)

s503 = substance('Rubidium iodide', 'RbI')
s503.solub['0°C'] = 'N/A'
s503.solub['10°C'] = 'N/A'
s503.solub['20°C'] = '144'
s503.solub['30°C'] = 'N/A'
s503.solub['40°C'] = 'N/A'
s503.solub['50°C'] = 'N/A'
s503.solub['60°C'] = 'N/A'
s503.solub['70°C'] = 'N/A'
s503.solub['80°C'] = 'N/A'
s503.solub['90°C'] = 'N/A'
s503.solub['100°C'] = 'N/A'
sublist.append(s503)

s504 = substance('Rubidium nitrate', 'RbNO3')
s504.solub['0°C'] = '19.5'
s504.solub['10°C'] = '33'
s504.solub['20°C'] = '52.9'
s504.solub['30°C'] = '81.2'
s504.solub['40°C'] = '117'
s504.solub['50°C'] = 'N/A'
s504.solub['60°C'] = '200'
s504.solub['70°C'] = 'N/A'
s504.solub['80°C'] = '310'
s504.solub['90°C'] = '374'
s504.solub['100°C'] = '452'
sublist.append(s504)

s505 = substance('Rubidium perchlorate', 'RbClO4')
s505.solub['0°C'] = '1.09'
s505.solub['10°C'] = '1.19'
s505.solub['20°C'] = '1.55'
s505.solub['30°C'] = '2.2'
s505.solub['40°C'] = '3.26'
s505.solub['50°C'] = 'N/A'
s505.solub['60°C'] = '6.27'
s505.solub['70°C'] = 'N/A'
s505.solub['80°C'] = '11'
s505.solub['90°C'] = '15.5'
s505.solub['100°C'] = '22'
sublist.append(s505)

s506 = substance('Rubidium periodate', 'RbIO4')
s506.solub['0°C'] = 'N/A'
s506.solub['10°C'] = 'N/A'
s506.solub['20°C'] = '0.648'
s506.solub['30°C'] = 'N/A'
s506.solub['40°C'] = 'N/A'
s506.solub['50°C'] = 'N/A'
s506.solub['60°C'] = 'N/A'
s506.solub['70°C'] = 'N/A'
s506.solub['80°C'] = 'N/A'
s506.solub['90°C'] = 'N/A'
s506.solub['100°C'] = 'N/A'
sublist.append(s506)

s507 = substance('Rubidium selenate', 'Rb2SeO4')
s507.solub['0°C'] = 'N/A'
s507.solub['10°C'] = 'N/A'
s507.solub['20°C'] = '159'
s507.solub['30°C'] = 'N/A'
s507.solub['40°C'] = 'N/A'
s507.solub['50°C'] = 'N/A'
s507.solub['60°C'] = 'N/A'
s507.solub['70°C'] = 'N/A'
s507.solub['80°C'] = 'N/A'
s507.solub['90°C'] = 'N/A'
s507.solub['100°C'] = 'N/A'
sublist.append(s507)

s508 = substance('Rubidium sulfate', 'Rb2SO4')
s508.solub['0°C'] = '37.5'
s508.solub['10°C'] = '42.6'
s508.solub['20°C'] = '48.1'
s508.solub['30°C'] = '53.6'
s508.solub['40°C'] = '58.5'
s508.solub['50°C'] = 'N/A'
s508.solub['60°C'] = '67.5'
s508.solub['70°C'] = 'N/A'
s508.solub['80°C'] = '75.1'
s508.solub['90°C'] = '78.6'
s508.solub['100°C'] = '81.8'
sublist.append(s508)

s509 = substance('Samarium acetate', 'Sm(C2H3O2)3.3H2O')
s509.solub['0°C'] = 'N/A'
s509.solub['10°C'] = 'N/A'
s509.solub['20°C'] = '15'
s509.solub['30°C'] = 'N/A'
s509.solub['40°C'] = 'N/A'
s509.solub['50°C'] = 'N/A'
s509.solub['60°C'] = 'N/A'
s509.solub['70°C'] = 'N/A'
s509.solub['80°C'] = 'N/A'
s509.solub['90°C'] = 'N/A'
s509.solub['100°C'] = 'N/A'
sublist.append(s509)

s510 = substance('Samarium bromate', 'Sm(BrO3)3')
s510.solub['0°C'] = '34.2'
s510.solub['10°C'] = '47.6'
s510.solub['20°C'] = '62.5'
s510.solub['30°C'] = '79'
s510.solub['40°C'] = '98'
s510.solub['50°C'] = 'N/A'
s510.solub['60°C'] = 'N/A'
s510.solub['70°C'] = 'N/A'
s510.solub['80°C'] = 'N/A'
s510.solub['90°C'] = 'N/A'
s510.solub['100°C'] = 'N/A'
sublist.append(s510)

s511 = substance('Samarium chloride', 'SmCl3')
s511.solub['0°C'] = 'N/A'
s511.solub['10°C'] = '92.4'
s511.solub['20°C'] = '93.4'
s511.solub['30°C'] = '94.6'
s511.solub['40°C'] = '96.9'
s511.solub['50°C'] = 'N/A'
s511.solub['60°C'] = 'N/A'
s511.solub['70°C'] = 'N/A'
s511.solub['80°C'] = 'N/A'
s511.solub['90°C'] = 'N/A'
s511.solub['100°C'] = 'N/A'
sublist.append(s511)

s512 = substance('Samarium sulfate', 'Sm2(SO4)3.8H2O')
s512.solub['0°C'] = 'N/A'
s512.solub['10°C'] = 'N/A'
s512.solub['20°C'] = '2.7'
s512.solub['30°C'] = '3.1'
s512.solub['40°C'] = 'N/A'
s512.solub['50°C'] = 'N/A'
s512.solub['60°C'] = 'N/A'
s512.solub['70°C'] = 'N/A'
s512.solub['80°C'] = 'N/A'
s512.solub['90°C'] = 'N/A'
s512.solub['100°C'] = 'N/A'
sublist.append(s512)

s513 = substance('Scandium oxalate', 'Sc2(C2O4)3.6H2O')
s513.solub['0°C'] = 'N/A'
s513.solub['10°C'] = 'N/A'
s513.solub['20°C'] = '0.006'
s513.solub['30°C'] = 'N/A'
s513.solub['40°C'] = 'N/A'
s513.solub['50°C'] = 'N/A'
s513.solub['60°C'] = 'N/A'
s513.solub['70°C'] = 'N/A'
s513.solub['80°C'] = 'N/A'
s513.solub['90°C'] = 'N/A'
s513.solub['100°C'] = 'N/A'
sublist.append(s513)

s514 = substance('Scandium sulfate', 'Sc2(SO4)3.5H2O')
s514.solub['0°C'] = 'N/A'
s514.solub['10°C'] = 'N/A'
s514.solub['20°C'] = '54.6'
s514.solub['30°C'] = 'N/A'
s514.solub['40°C'] = 'N/A'
s514.solub['50°C'] = 'N/A'
s514.solub['60°C'] = 'N/A'
s514.solub['70°C'] = 'N/A'
s514.solub['80°C'] = 'N/A'
s514.solub['90°C'] = 'N/A'
s514.solub['100°C'] = 'N/A'
sublist.append(s514)

s515 = substance('Silicon dioxide', 'SiO2')
s515.solub['0°C'] = 'N/A'
s515.solub['10°C'] = 'N/A'
s515.solub['20°C'] = '0.012'
s515.solub['30°C'] = 'N/A'
s515.solub['40°C'] = 'N/A'
s515.solub['50°C'] = 'N/A'
s515.solub['60°C'] = 'N/A'
s515.solub['70°C'] = 'N/A'
s515.solub['80°C'] = 'N/A'
s515.solub['90°C'] = 'N/A'
s515.solub['100°C'] = 'N/A'
sublist.append(s515)

s516 = substance('Silver acetate', 'AgC2H3O2')
s516.solub['0°C'] = '0.73'
s516.solub['10°C'] = '0.89'
s516.solub['20°C'] = '1.05'
s516.solub['30°C'] = '1.23'
s516.solub['40°C'] = '1.43'
s516.solub['50°C'] = 'N/A'
s516.solub['60°C'] = '1.93'
s516.solub['70°C'] = 'N/A'
s516.solub['80°C'] = '2.59'
s516.solub['90°C'] = 'N/A'
s516.solub['100°C'] = 'N/A'
sublist.append(s516)

s517 = substance('Silver azide', 'AgN3')
s517.solub['0°C'] = 'N/A'
s517.solub['10°C'] = 'N/A'
s517.solub['20°C'] = '7.931×10-4'
s517.solub['30°C'] = 'N/A'
s517.solub['40°C'] = 'N/A'
s517.solub['50°C'] = 'N/A'
s517.solub['60°C'] = 'N/A'
s517.solub['70°C'] = 'N/A'
s517.solub['80°C'] = 'N/A'
s517.solub['90°C'] = 'N/A'
s517.solub['100°C'] = 'N/A'
sublist.append(s517)

s518 = substance('Silver bromate', 'AgBrO3')
s518.solub['0°C'] = 'N/A'
s518.solub['10°C'] = '0.11'
s518.solub['20°C'] = '0.16'
s518.solub['30°C'] = '0.23'
s518.solub['40°C'] = '0.32'
s518.solub['50°C'] = 'N/A'
s518.solub['60°C'] = '0.57'
s518.solub['70°C'] = 'N/A'
s518.solub['80°C'] = '0.94'
s518.solub['90°C'] = '1.33'
s518.solub['100°C'] = 'N/A'
sublist.append(s518)

s519 = substance('Silver bromide', 'AgBr')
s519.solub['0°C'] = 'N/A'
s519.solub['10°C'] = 'N/A'
s519.solub['20°C'] = '1.328×10-5'
s519.solub['30°C'] = 'N/A'
s519.solub['40°C'] = 'N/A'
s519.solub['50°C'] = 'N/A'
s519.solub['60°C'] = 'N/A'
s519.solub['70°C'] = 'N/A'
s519.solub['80°C'] = 'N/A'
s519.solub['90°C'] = 'N/A'
s519.solub['100°C'] = 'N/A'
sublist.append(s519)

s520 = substance('Silver carbonate', 'Ag2CO3')
s520.solub['0°C'] = 'N/A'
s520.solub['10°C'] = 'N/A'
s520.solub['20°C'] = '0.003489'
s520.solub['30°C'] = 'N/A'
s520.solub['40°C'] = 'N/A'
s520.solub['50°C'] = 'N/A'
s520.solub['60°C'] = 'N/A'
s520.solub['70°C'] = 'N/A'
s520.solub['80°C'] = 'N/A'
s520.solub['90°C'] = 'N/A'
s520.solub['100°C'] = 'N/A'
sublist.append(s520)

s521 = substance('Silver chlorate', 'AgClO3')
s521.solub['0°C'] = 'N/A'
s521.solub['10°C'] = '10.4'
s521.solub['20°C'] = '15.3'
s521.solub['30°C'] = '20.9'
s521.solub['40°C'] = '26.8'
s521.solub['50°C'] = 'N/A'
s521.solub['60°C'] = 'N/A'
s521.solub['70°C'] = 'N/A'
s521.solub['80°C'] = 'N/A'
s521.solub['90°C'] = 'N/A'
s521.solub['100°C'] = 'N/A'
sublist.append(s521)

s522 = substance('Silver chloride', 'AgCl')
s522.solub['0°C'] = 'N/A'
s522.solub['10°C'] = 'N/A'
s522.solub['20°C'] = '1.923×10-4'
s522.solub['30°C'] = 'N/A'
s522.solub['40°C'] = 'N/A'
s522.solub['50°C'] = '5.2×10-5'
s522.solub['60°C'] = 'N/A'
s522.solub['70°C'] = 'N/A'
s522.solub['80°C'] = 'N/A'
s522.solub['90°C'] = 'N/A'
s522.solub['100°C'] = 'N/A'
sublist.append(s522)

s523 = substance('Silver chlorite', 'AgClO2')
s523.solub['0°C'] = 'N/A'
s523.solub['10°C'] = 'N/A'
s523.solub['20°C'] = '0.248'
s523.solub['30°C'] = 'N/A'
s523.solub['40°C'] = 'N/A'
s523.solub['50°C'] = 'N/A'
s523.solub['60°C'] = 'N/A'
s523.solub['70°C'] = 'N/A'
s523.solub['80°C'] = 'N/A'
s523.solub['90°C'] = 'N/A'
s523.solub['100°C'] = 'N/A'
sublist.append(s523)

s524 = substance('Silver chromate', 'Ag2CrO4')
s524.solub['0°C'] = 'N/A'
s524.solub['10°C'] = 'N/A'
s524.solub['20°C'] = '0.002157'
s524.solub['30°C'] = 'N/A'
s524.solub['40°C'] = 'N/A'
s524.solub['50°C'] = 'N/A'
s524.solub['60°C'] = 'N/A'
s524.solub['70°C'] = 'N/A'
s524.solub['80°C'] = 'N/A'
s524.solub['90°C'] = 'N/A'
s524.solub['100°C'] = 'N/A'
sublist.append(s524)

s525 = substance('Silver cyanide', 'AgCN')
s525.solub['0°C'] = 'N/A'
s525.solub['10°C'] = 'N/A'
s525.solub['20°C'] = '1.467×10-7'
s525.solub['30°C'] = 'N/A'
s525.solub['40°C'] = 'N/A'
s525.solub['50°C'] = 'N/A'
s525.solub['60°C'] = 'N/A'
s525.solub['70°C'] = 'N/A'
s525.solub['80°C'] = 'N/A'
s525.solub['90°C'] = 'N/A'
s525.solub['100°C'] = 'N/A'
sublist.append(s525)

s526 = substance('Silver dichromate', 'Ag2Cr2O7')
s526.solub['0°C'] = 'N/A'
s526.solub['10°C'] = 'N/A'
s526.solub['20°C'] = '0.159'
s526.solub['30°C'] = 'N/A'
s526.solub['40°C'] = 'N/A'
s526.solub['50°C'] = 'N/A'
s526.solub['60°C'] = 'N/A'
s526.solub['70°C'] = 'N/A'
s526.solub['80°C'] = 'N/A'
s526.solub['90°C'] = 'N/A'
s526.solub['100°C'] = 'N/A'
sublist.append(s526)

s527 = substance('Silver fluoride', 'AgF')
s527.solub['0°C'] = '85.9'
s527.solub['10°C'] = '120'
s527.solub['20°C'] = '172'
s527.solub['30°C'] = '190'
s527.solub['40°C'] = '203'
s527.solub['50°C'] = 'N/A'
s527.solub['60°C'] = 'N/A'
s527.solub['70°C'] = 'N/A'
s527.solub['80°C'] = 'N/A'
s527.solub['90°C'] = 'N/A'
s527.solub['100°C'] = 'N/A'
sublist.append(s527)

s528 = substance('Silver nitrate', 'AgNO3')
s528.solub['0°C'] = '122'
s528.solub['10°C'] = '167'
s528.solub['20°C'] = '216'
s528.solub['30°C'] = '265'
s528.solub['40°C'] = '311'
s528.solub['50°C'] = 'N/A'
s528.solub['60°C'] = '440'
s528.solub['70°C'] = 'N/A'
s528.solub['80°C'] = '585'
s528.solub['90°C'] = '652'
s528.solub['100°C'] = '733'
sublist.append(s528)

s529 = substance('Silver oxalate', 'Ag2C2O4')
s529.solub['0°C'] = 'N/A'
s529.solub['10°C'] = 'N/A'
s529.solub['20°C'] = '0.00327'
s529.solub['30°C'] = 'N/A'
s529.solub['40°C'] = 'N/A'
s529.solub['50°C'] = 'N/A'
s529.solub['60°C'] = 'N/A'
s529.solub['70°C'] = 'N/A'
s529.solub['80°C'] = 'N/A'
s529.solub['90°C'] = 'N/A'
s529.solub['100°C'] = 'N/A'
sublist.append(s529)

s530 = substance('Silver oxide', 'Ag2O')
s530.solub['0°C'] = 'N/A'
s530.solub['10°C'] = 'N/A'
s530.solub['20°C'] = '0.0012'
s530.solub['30°C'] = 'N/A'
s530.solub['40°C'] = 'N/A'
s530.solub['50°C'] = 'N/A'
s530.solub['60°C'] = 'N/A'
s530.solub['70°C'] = 'N/A'
s530.solub['80°C'] = 'N/A'
s530.solub['90°C'] = 'N/A'
s530.solub['100°C'] = 'N/A'
sublist.append(s530)

s531 = substance('Silver perchlorate', 'AgClO4')
s531.solub['0°C'] = '455'
s531.solub['10°C'] = '484'
s531.solub['20°C'] = '525'
s531.solub['30°C'] = '594'
s531.solub['40°C'] = '635'
s531.solub['50°C'] = 'N/A'
s531.solub['60°C'] = 'N/A'
s531.solub['70°C'] = 'N/A'
s531.solub['80°C'] = 'N/A'
s531.solub['90°C'] = 'N/A'
s531.solub['100°C'] = '793'
sublist.append(s531)

s532 = substance('Silver permanganate', 'AgMnO4')
s532.solub['0°C'] = 'N/A'
s532.solub['10°C'] = 'N/A'
s532.solub['20°C'] = '0.9'
s532.solub['30°C'] = 'N/A'
s532.solub['40°C'] = 'N/A'
s532.solub['50°C'] = 'N/A'
s532.solub['60°C'] = 'N/A'
s532.solub['70°C'] = 'N/A'
s532.solub['80°C'] = 'N/A'
s532.solub['90°C'] = 'N/A'
s532.solub['100°C'] = 'N/A'
sublist.append(s532)

s533 = substance('Silver sulfate', 'Ag2SO4')
s533.solub['0°C'] = '0.57'
s533.solub['10°C'] = '0.7'
s533.solub['20°C'] = '0.8'
s533.solub['30°C'] = '0.89'
s533.solub['40°C'] = '0.98'
s533.solub['50°C'] = 'N/A'
s533.solub['60°C'] = '1.15'
s533.solub['70°C'] = 'N/A'
s533.solub['80°C'] = '1.3'
s533.solub['90°C'] = '1.36'
s533.solub['100°C'] = '1.41'
sublist.append(s533)

s534 = substance('Silver vanadate', 'AgVO3')
s534.solub['0°C'] = 'N/A'
s534.solub['10°C'] = 'N/A'
s534.solub['20°C'] = '0.01462'
s534.solub['30°C'] = 'N/A'
s534.solub['40°C'] = 'N/A'
s534.solub['50°C'] = 'N/A'
s534.solub['60°C'] = 'N/A'
s534.solub['70°C'] = 'N/A'
s534.solub['80°C'] = 'N/A'
s534.solub['90°C'] = 'N/A'
s534.solub['100°C'] = 'N/A'
sublist.append(s534)

s535 = substance('Sodium acetate', 'NaC2H3O2')
s535.solub['0°C'] = '36.2'
s535.solub['10°C'] = '40.8'
s535.solub['20°C'] = '46.4'
s535.solub['30°C'] = '54.6'
s535.solub['40°C'] = '65.6'
s535.solub['50°C'] = 'N/A'
s535.solub['60°C'] = '139'
s535.solub['70°C'] = 'N/A'
s535.solub['80°C'] = '153'
s535.solub['90°C'] = '161'
s535.solub['100°C'] = '170'
sublist.append(s535)

s536 = substance('Sodium azide', 'NaN3')
s536.solub['0°C'] = '38.9'
s536.solub['10°C'] = '39.9'
s536.solub['20°C'] = '40.8'
s536.solub['30°C'] = 'N/A'
s536.solub['40°C'] = 'N/A'
s536.solub['50°C'] = 'N/A'
s536.solub['60°C'] = 'N/A'
s536.solub['70°C'] = 'N/A'
s536.solub['80°C'] = 'N/A'
s536.solub['90°C'] = 'N/A'
s536.solub['100°C'] = 'N/A'
sublist.append(s536)

s537 = substance('Sodium benzoate', 'NaC7H5O2')
s537.solub['0°C'] = 'N/A'
s537.solub['10°C'] = 'N/A'
s537.solub['20°C'] = '66'
s537.solub['30°C'] = 'N/A'
s537.solub['40°C'] = 'N/A'
s537.solub['50°C'] = 'N/A'
s537.solub['60°C'] = 'N/A'
s537.solub['70°C'] = 'N/A'
s537.solub['80°C'] = 'N/A'
s537.solub['90°C'] = 'N/A'
s537.solub['100°C'] = 'N/A'
sublist.append(s537)

s538 = substance('Sodium borohydride', 'NaBH4')
s538.solub['0°C'] = '25'
s538.solub['10°C'] = 'N/A'
s538.solub['20°C'] = '55'
s538.solub['30°C'] = 'N/A'
s538.solub['40°C'] = '88.5'
s538.solub['50°C'] = 'N/A'
s538.solub['60°C'] = 'N/A'
s538.solub['70°C'] = 'N/A'
s538.solub['80°C'] = 'N/A'
s538.solub['90°C'] = 'N/A'
s538.solub['100°C'] = 'N/A'
sublist.append(s538)

s539 = substance('Sodium bromate', 'NaBrO3')
s539.solub['0°C'] = '24.2'
s539.solub['10°C'] = '30.3'
s539.solub['20°C'] = '36.4'
s539.solub['30°C'] = '42.6'
s539.solub['40°C'] = '48.8'
s539.solub['50°C'] = 'N/A'
s539.solub['60°C'] = '62.6'
s539.solub['70°C'] = 'N/A'
s539.solub['80°C'] = '75.7'
s539.solub['90°C'] = 'N/A'
s539.solub['100°C'] = '90.8'
sublist.append(s539)

s540 = substance('Sodium bromide', 'NaBr')
s540.solub['0°C'] = '80.2'
s540.solub['10°C'] = '85.2'
s540.solub['20°C'] = '90.8'
s540.solub['30°C'] = '98.4'
s540.solub['40°C'] = '107'
s540.solub['50°C'] = 'N/A'
s540.solub['60°C'] = '118'
s540.solub['70°C'] = 'N/A'
s540.solub['80°C'] = '120'
s540.solub['90°C'] = '121'
s540.solub['100°C'] = '121'
sublist.append(s540)

s541 = substance('Sodium carbonate', 'Na2CO3')
s541.solub['0°C'] = '7'
s541.solub['10°C'] = '12.5'
s541.solub['20°C'] = '21.5'
s541.solub['30°C'] = '39.7'
s541.solub['40°C'] = '49'
s541.solub['50°C'] = 'N/A'
s541.solub['60°C'] = '46'
s541.solub['70°C'] = 'N/A'
s541.solub['80°C'] = '43.9'
s541.solub['90°C'] = '43.9'
s541.solub['100°C'] = '45.5'
sublist.append(s541)

s542 = substance('Sodium chlorate', 'NaClO3')
s542.solub['0°C'] = '79.6'
s542.solub['10°C'] = '87.6'
s542.solub['20°C'] = '95.9'
s542.solub['30°C'] = '105'
s542.solub['40°C'] = '115'
s542.solub['50°C'] = 'N/A'
s542.solub['60°C'] = '137'
s542.solub['70°C'] = 'N/A'
s542.solub['80°C'] = '167'
s542.solub['90°C'] = '184'
s542.solub['100°C'] = '204'
sublist.append(s542)

s543 = substance('Sodium chloride', 'NaCl')
s543.solub['0°C'] = '35.65'
s543.solub['10°C'] = '35.72'
s543.solub['20°C'] = '35.89'
s543.solub['30°C'] = '36.09'
s543.solub['40°C'] = '36.37'
s543.solub['50°C'] = '36.69'
s543.solub['60°C'] = '37.04'
s543.solub['70°C'] = '37.46'
s543.solub['80°C'] = '37.93'
s543.solub['90°C'] = '38.47'
s543.solub['100°C'] = '38.99'
sublist.append(s543)

s544 = substance('Sodium chromate', 'Na2CrO4')
s544.solub['0°C'] = '31.7'
s544.solub['10°C'] = '50.1'
s544.solub['20°C'] = '84'
s544.solub['30°C'] = '88'
s544.solub['40°C'] = '96'
s544.solub['50°C'] = 'N/A'
s544.solub['60°C'] = '115'
s544.solub['70°C'] = 'N/A'
s544.solub['80°C'] = '125'
s544.solub['90°C'] = 'N/A'
s544.solub['100°C'] = '126'
sublist.append(s544)

s545 = substance('Sodium cyanide', 'NaCN')
s545.solub['0°C'] = '40.8'
s545.solub['10°C'] = '48.1'
s545.solub['20°C'] = '58.7'
s545.solub['30°C'] = '71.2'
s545.solub['40°C'] = 'dec'
s545.solub['50°C'] = 'N/A'
s545.solub['60°C'] = 'N/A'
s545.solub['70°C'] = 'N/A'
s545.solub['80°C'] = 'N/A'
s545.solub['90°C'] = 'N/A'
s545.solub['100°C'] = 'N/A'
sublist.append(s545)

s546 = substance('Sodium dichromate', 'Na2Cr2O7')
s546.solub['0°C'] = '163'
s546.solub['10°C'] = '172'
s546.solub['20°C'] = '183'
s546.solub['30°C'] = '198'
s546.solub['40°C'] = '215'
s546.solub['50°C'] = 'N/A'
s546.solub['60°C'] = '269'
s546.solub['70°C'] = 'N/A'
s546.solub['80°C'] = '376'
s546.solub['90°C'] = '405'
s546.solub['100°C'] = '415'
sublist.append(s546)

s547 = substance('Monosodium phosphate', 'NaH2PO4')
s547.solub['0°C'] = '56.5'
s547.solub['10°C'] = '69.8'
s547.solub['20°C'] = '86.9'
s547.solub['30°C'] = '107'
s547.solub['40°C'] = '133'
s547.solub['50°C'] = 'N/A'
s547.solub['60°C'] = '172'
s547.solub['70°C'] = 'N/A'
s547.solub['80°C'] = '211'
s547.solub['90°C'] = '234'
s547.solub['100°C'] = 'N/A'
sublist.append(s547)

s548 = substance('Sodium fluoride', 'NaF')
s548.solub['0°C'] = '3.66'
s548.solub['10°C'] = 'N/A'
s548.solub['20°C'] = '4.06'
s548.solub['30°C'] = '4.22'
s548.solub['40°C'] = '4.4'
s548.solub['50°C'] = 'N/A'
s548.solub['60°C'] = '4.68'
s548.solub['70°C'] = 'N/A'
s548.solub['80°C'] = '4.89'
s548.solub['90°C'] = 'N/A'
s548.solub['100°C'] = '5.08'
sublist.append(s548)

s549 = substance('Sodium formate', 'HCOONa')
s549.solub['0°C'] = '43.9'
s549.solub['10°C'] = '62.5'
s549.solub['20°C'] = '81.2'
s549.solub['30°C'] = '102'
s549.solub['40°C'] = '108'
s549.solub['50°C'] = 'N/A'
s549.solub['60°C'] = '122'
s549.solub['70°C'] = 'N/A'
s549.solub['80°C'] = '138'
s549.solub['90°C'] = '147'
s549.solub['100°C'] = '160'
sublist.append(s549)

s550 = substance('Sodium hydrogen carbonate', 'NaHCO3')
s550.solub['0°C'] = '7'
s550.solub['10°C'] = '8.1'
s550.solub['20°C'] = '9.6'
s550.solub['30°C'] = '11.1'
s550.solub['40°C'] = '12.7'
s550.solub['50°C'] = 'N/A'
s550.solub['60°C'] = '16'
s550.solub['70°C'] = 'N/A'
s550.solub['80°C'] = 'N/A'
s550.solub['90°C'] = 'N/A'
s550.solub['100°C'] = 'N/A'
sublist.append(s550)

s551 = substance('Sodium hydroxide', 'NaOH')
s551.solub['0°C'] = 'N/A'
s551.solub['10°C'] = '98'
s551.solub['20°C'] = '109'
s551.solub['30°C'] = '119'
s551.solub['40°C'] = '129'
s551.solub['50°C'] = 'N/A'
s551.solub['60°C'] = '174'
s551.solub['70°C'] = 'N/A'
s551.solub['80°C'] = 'N/A'
s551.solub['90°C'] = 'N/A'
s551.solub['100°C'] = 'N/A'
sublist.append(s551)

s552 = substance('Sodium iodate', 'NaIO3')
s552.solub['0°C'] = '2.48'
s552.solub['10°C'] = '4.59'
s552.solub['20°C'] = '8.08'
s552.solub['30°C'] = '10.7'
s552.solub['40°C'] = '13.3'
s552.solub['50°C'] = 'N/A'
s552.solub['60°C'] = '19.8'
s552.solub['70°C'] = 'N/A'
s552.solub['80°C'] = '26.6'
s552.solub['90°C'] = '29.5'
s552.solub['100°C'] = '33'
sublist.append(s552)

s553 = substance('Sodium iodide', 'NaI')
s553.solub['0°C'] = '159'
s553.solub['10°C'] = '167'
s553.solub['20°C'] = '178'
s553.solub['30°C'] = '191'
s553.solub['40°C'] = '205'
s553.solub['50°C'] = 'N/A'
s553.solub['60°C'] = '257'
s553.solub['70°C'] = 'N/A'
s553.solub['80°C'] = '295'
s553.solub['90°C'] = 'N/A'
s553.solub['100°C'] = '302'
sublist.append(s553)

s554 = substance('Sodium metabisulfite', 'Na2S2O5')
s554.solub['0°C'] = '45.1'
s554.solub['10°C'] = 'N/A'
s554.solub['20°C'] = '65.3'
s554.solub['30°C'] = 'N/A'
s554.solub['40°C'] = 'N/A'
s554.solub['50°C'] = 'N/A'
s554.solub['60°C'] = 'N/A'
s554.solub['70°C'] = 'N/A'
s554.solub['80°C'] = '88.7'
s554.solub['90°C'] = 'N/A'
s554.solub['100°C'] = '96.3'
sublist.append(s554)

s555 = substance('Sodium metaborate', 'NaBO2')
s555.solub['0°C'] = '16.4'
s555.solub['10°C'] = '20.8'
s555.solub['20°C'] = '25.4'
s555.solub['30°C'] = '31.4'
s555.solub['40°C'] = '40.4'
s555.solub['50°C'] = 'N/A'
s555.solub['60°C'] = '63.9'
s555.solub['70°C'] = 'N/A'
s555.solub['80°C'] = '84.5'
s555.solub['90°C'] = 'N/A'
s555.solub['100°C'] = '125.2'
sublist.append(s555)

s556 = substance('Sodium molybdate', 'Na2MoO4')
s556.solub['0°C'] = '44.1'
s556.solub['10°C'] = '64.7'
s556.solub['20°C'] = '65.3'
s556.solub['30°C'] = '66.9'
s556.solub['40°C'] = '68.6'
s556.solub['50°C'] = 'N/A'
s556.solub['60°C'] = '71.8'
s556.solub['70°C'] = 'N/A'
s556.solub['80°C'] = 'N/A'
s556.solub['90°C'] = 'N/A'
s556.solub['100°C'] = 'N/A'
sublist.append(s556)

s557 = substance('Sodium nitrate', 'NaNO3')
s557.solub['0°C'] = '73'
s557.solub['10°C'] = '80.8'
s557.solub['20°C'] = '87.6'
s557.solub['30°C'] = '94.9'
s557.solub['40°C'] = '102'
s557.solub['50°C'] = 'N/A'
s557.solub['60°C'] = '122'
s557.solub['70°C'] = 'N/A'
s557.solub['80°C'] = '148'
s557.solub['90°C'] = 'N/A'
s557.solub['100°C'] = '180'
sublist.append(s557)

s558 = substance('Sodium nitrite', 'NaNO2')
s558.solub['0°C'] = '71.2'
s558.solub['10°C'] = '75.1'
s558.solub['20°C'] = '80.8'
s558.solub['30°C'] = '87.6'
s558.solub['40°C'] = '94.9'
s558.solub['50°C'] = 'N/A'
s558.solub['60°C'] = '111'
s558.solub['70°C'] = 'N/A'
s558.solub['80°C'] = '133'
s558.solub['90°C'] = 'N/A'
s558.solub['100°C'] = '160'
sublist.append(s558)

s559 = substance('Sodium oxalate', 'Na2C2O4')
s559.solub['0°C'] = '2.69'
s559.solub['10°C'] = '3.05'
s559.solub['20°C'] = '3.41'
s559.solub['30°C'] = '3.81'
s559.solub['40°C'] = '4.18'
s559.solub['50°C'] = 'N/A'
s559.solub['60°C'] = '4.93'
s559.solub['70°C'] = 'N/A'
s559.solub['80°C'] = '5.71'
s559.solub['90°C'] = 'N/A'
s559.solub['100°C'] = '6.5'
sublist.append(s559)

s560 = substance('Sodium perchlorate', 'NaClO4')
s560.solub['0°C'] = '167'
s560.solub['10°C'] = '183'
s560.solub['20°C'] = '201'
s560.solub['30°C'] = '222'
s560.solub['40°C'] = '245'
s560.solub['50°C'] = 'N/A'
s560.solub['60°C'] = '288'
s560.solub['70°C'] = 'N/A'
s560.solub['80°C'] = '306'
s560.solub['90°C'] = 'N/A'
s560.solub['100°C'] = '329'
sublist.append(s560)

s561 = substance('Sodium periodate', 'NaIO4')
s561.solub['0°C'] = '1.83'
s561.solub['10°C'] = '5.6'
s561.solub['20°C'] = '10.3'
s561.solub['30°C'] = '19.9'
s561.solub['40°C'] = '30.4'
s561.solub['50°C'] = 'N/A'
s561.solub['60°C'] = 'N/A'
s561.solub['70°C'] = 'N/A'
s561.solub['80°C'] = 'N/A'
s561.solub['90°C'] = 'N/A'
s561.solub['100°C'] = 'N/A'
sublist.append(s561)

s562 = substance('Sodium permanganate', 'NaMnO4')
s562.solub['0°C'] = 'N/A'
s562.solub['10°C'] = 'N/A'
s562.solub['20°C'] = '90'
s562.solub['30°C'] = 'N/A'
s562.solub['40°C'] = 'N/A'
s562.solub['50°C'] = 'N/A'
s562.solub['60°C'] = 'N/A'
s562.solub['70°C'] = 'N/A'
s562.solub['80°C'] = 'N/A'
s562.solub['90°C'] = 'N/A'
s562.solub['100°C'] = 'N/A'
sublist.append(s562)

s563 = substance('Sodium phosphate', 'Na3PO4')
s563.solub['0°C'] = '4.5'
s563.solub['10°C'] = '8.2'
s563.solub['20°C'] = '12.1'
s563.solub['30°C'] = '16.3'
s563.solub['40°C'] = '20.2'
s563.solub['50°C'] = 'N/A'
s563.solub['60°C'] = '20.9'
s563.solub['70°C'] = 'N/A'
s563.solub['80°C'] = '60'
s563.solub['90°C'] = '68.1'
s563.solub['100°C'] = '77'
sublist.append(s563)

s564 = substance('Sodium pyrophosphate', 'Na4P2O7')
s564.solub['0°C'] = '2.26'
s564.solub['10°C'] = 'N/A'
s564.solub['20°C'] = 'N/A'
s564.solub['30°C'] = 'N/A'
s564.solub['40°C'] = 'N/A'
s564.solub['50°C'] = 'N/A'
s564.solub['60°C'] = 'N/A'
s564.solub['70°C'] = 'N/A'
s564.solub['80°C'] = 'N/A'
s564.solub['90°C'] = 'N/A'
s564.solub['100°C'] = 'N/A'
sublist.append(s564)

s565 = substance('Sodium selenate', 'Na2SeO4')
s565.solub['0°C'] = '13.3'
s565.solub['10°C'] = '25.2'
s565.solub['20°C'] = '26.9'
s565.solub['30°C'] = '77'
s565.solub['40°C'] = '81.8'
s565.solub['50°C'] = 'N/A'
s565.solub['60°C'] = '78.6'
s565.solub['70°C'] = 'N/A'
s565.solub['80°C'] = '74.8'
s565.solub['90°C'] = '73'
s565.solub['100°C'] = '72.7'
sublist.append(s565)

s566 = substance('Sodium sulfate', 'Na2SO4')
s566.solub['0°C'] = '4.9'
s566.solub['10°C'] = '9.1'
s566.solub['20°C'] = '19.5'
s566.solub['30°C'] = '40.8'
s566.solub['40°C'] = '48.8'
s566.solub['50°C'] = 'N/A'
s566.solub['60°C'] = '45.3'
s566.solub['70°C'] = 'N/A'
s566.solub['80°C'] = '43.7'
s566.solub['90°C'] = '42.7'
s566.solub['100°C'] = '42.5'
sublist.append(s566)

s567 = substance('Sodium sulfite', 'Na2SO3')
s567.solub['0°C'] = 'N/A'
s567.solub['10°C'] = 'N/A'
s567.solub['20°C'] = 'N/A'
s567.solub['30°C'] = '27.0'
s567.solub['40°C'] = 'N/A'
s567.solub['50°C'] = 'N/A'
s567.solub['60°C'] = 'N/A'
s567.solub['70°C'] = 'N/A'
s567.solub['80°C'] = 'N/A'
s567.solub['90°C'] = 'N/A'
s567.solub['100°C'] = 'N/A'
sublist.append(s567)

s568 = substance('Sodium tetraborate decahydrate', 'Na2B4O710H2O')
s568.solub['0°C'] = '2'
s568.solub['10°C'] = '2.3'
s568.solub['20°C'] = '2.5'
s568.solub['30°C'] = '4'
s568.solub['40°C'] = '6'
s568.solub['50°C'] = '10'
s568.solub['60°C'] = '15'
s568.solub['70°C'] = 'N/A'
s568.solub['80°C'] = 'N/A'
s568.solub['90°C'] = 'N/A'
s568.solub['100°C'] = 'N/A'
sublist.append(s568)

s569 = substance('Sodium tetraborate pentahydrate', 'Na2B4O75H2O')
s569.solub['0°C'] = 'N/A'
s569.solub['10°C'] = 'N/A'
s569.solub['20°C'] = 'N/A'
s569.solub['30°C'] = 'N/A'
s569.solub['40°C'] = 'N/A'
s569.solub['50°C'] = 'N/A'
s569.solub['60°C'] = 'N/A'
s569.solub['70°C'] = '20'
s569.solub['80°C'] = '23'
s569.solub['90°C'] = '28'
s569.solub['100°C'] = '35'
sublist.append(s569)

s570 = substance('Sodium tetraborate tetrahydrate', 'Na2B4O74H2O')
s570.solub['0°C'] = 'N/A'
s570.solub['10°C'] = 'N/A'
s570.solub['20°C'] = 'N/A'
s570.solub['30°C'] = 'N/A'
s570.solub['40°C'] = 'N/A'
s570.solub['50°C'] = 'N/A'
s570.solub['60°C'] = 'N/A'
s570.solub['70°C'] = '17'
s570.solub['80°C'] = '20'
s570.solub['90°C'] = '23'
s570.solub['100°C'] = '28'
sublist.append(s570)

s571 = substance('Sodium tetraphenylborate', 'NaB(C6H5)4')
s571.solub['0°C'] = 'N/A'
s571.solub['10°C'] = 'N/A'
s571.solub['20°C'] = '47'
s571.solub['30°C'] = 'N/A'
s571.solub['40°C'] = 'N/A'
s571.solub['50°C'] = 'N/A'
s571.solub['60°C'] = 'N/A'
s571.solub['70°C'] = 'N/A'
s571.solub['80°C'] = 'N/A'
s571.solub['90°C'] = 'N/A'
s571.solub['100°C'] = 'N/A'
sublist.append(s571)

s572 = substance('Sodium thiosulfate', 'Na2S2O3')
s572.solub['0°C'] = '71.5'
s572.solub['10°C'] = 'N/A'
s572.solub['20°C'] = '73'
s572.solub['30°C'] = 'N/A'
s572.solub['40°C'] = '77.6'
s572.solub['50°C'] = 'N/A'
s572.solub['60°C'] = 'N/A'
s572.solub['70°C'] = 'N/A'
s572.solub['80°C'] = '90.8'
s572.solub['90°C'] = 'N/A'
s572.solub['100°C'] = '97.2'
sublist.append(s572)

s573 = substance('Strontium acetate', 'Sr(C2H3O2)2')
s573.solub['0°C'] = '37'
s573.solub['10°C'] = '42.9'
s573.solub['20°C'] = '41.1'
s573.solub['30°C'] = '39.5'
s573.solub['40°C'] = '38.3'
s573.solub['50°C'] = 'N/A'
s573.solub['60°C'] = '36.8'
s573.solub['70°C'] = 'N/A'
s573.solub['80°C'] = '36.1'
s573.solub['90°C'] = '36.2'
s573.solub['100°C'] = '36.4'
sublist.append(s573)

s574 = substance('Strontium bromate', 'Sr(BrO3)2.H2O')
s574.solub['0°C'] = 'N/A'
s574.solub['10°C'] = 'N/A'
s574.solub['20°C'] = '30.9'
s574.solub['30°C'] = 'N/A'
s574.solub['40°C'] = 'N/A'
s574.solub['50°C'] = 'N/A'
s574.solub['60°C'] = 'N/A'
s574.solub['70°C'] = 'N/A'
s574.solub['80°C'] = 'N/A'
s574.solub['90°C'] = 'N/A'
s574.solub['100°C'] = '41'
sublist.append(s574)

s575 = substance('Strontium bromide', 'SrBr2')
s575.solub['0°C'] = '85.2'
s575.solub['10°C'] = '93.4'
s575.solub['20°C'] = '102'
s575.solub['30°C'] = '112'
s575.solub['40°C'] = '123'
s575.solub['50°C'] = 'N/A'
s575.solub['60°C'] = '150'
s575.solub['70°C'] = 'N/A'
s575.solub['80°C'] = '182'
s575.solub['90°C'] = 'N/A'
s575.solub['100°C'] = '223'
sublist.append(s575)

s576 = substance('Strontium carbonate', 'SrCO3')
s576.solub['0°C'] = 'N/A'
s576.solub['10°C'] = 'N/A'
s576.solub['20°C'] = '0.0011'
s576.solub['30°C'] = 'N/A'
s576.solub['40°C'] = 'N/A'
s576.solub['50°C'] = 'N/A'
s576.solub['60°C'] = 'N/A'
s576.solub['70°C'] = 'N/A'
s576.solub['80°C'] = 'N/A'
s576.solub['90°C'] = 'N/A'
s576.solub['100°C'] = '0.065'
sublist.append(s576)

s577 = substance('Strontium chlorate', 'Sr(ClO3)2')
s577.solub['0°C'] = 'N/A'
s577.solub['10°C'] = 'N/A'
s577.solub['20°C'] = '175'
s577.solub['30°C'] = 'N/A'
s577.solub['40°C'] = 'N/A'
s577.solub['50°C'] = 'N/A'
s577.solub['60°C'] = 'N/A'
s577.solub['70°C'] = 'N/A'
s577.solub['80°C'] = 'N/A'
s577.solub['90°C'] = 'N/A'
s577.solub['100°C'] = 'N/A'
sublist.append(s577)

s578 = substance('Strontium chloride', 'SrCl2')
s578.solub['0°C'] = '43.5'
s578.solub['10°C'] = '47.7'
s578.solub['20°C'] = '52.9'
s578.solub['30°C'] = '58.7'
s578.solub['40°C'] = '65.3'
s578.solub['50°C'] = 'N/A'
s578.solub['60°C'] = '81.8'
s578.solub['70°C'] = 'N/A'
s578.solub['80°C'] = '90.5'
s578.solub['90°C'] = 'N/A'
s578.solub['100°C'] = '101'
sublist.append(s578)

s579 = substance('Strontium chromate', 'SrCrO4')
s579.solub['0°C'] = 'N/A'
s579.solub['10°C'] = 'N/A'
s579.solub['20°C'] = '0.085'
s579.solub['30°C'] = '0.090'
s579.solub['40°C'] = 'N/A'
s579.solub['50°C'] = 'N/A'
s579.solub['60°C'] = 'N/A'
s579.solub['70°C'] = 'N/A'
s579.solub['80°C'] = 'N/A'
s579.solub['90°C'] = 'N/A'
s579.solub['100°C'] = 'N/A'
sublist.append(s579)

s580 = substance('Strontium fluoride', 'SrF2')
s580.solub['0°C'] = 'N/A'
s580.solub['10°C'] = 'N/A'
s580.solub['20°C'] = '1.2×10-4'
s580.solub['30°C'] = 'N/A'
s580.solub['40°C'] = 'N/A'
s580.solub['50°C'] = 'N/A'
s580.solub['60°C'] = 'N/A'
s580.solub['70°C'] = 'N/A'
s580.solub['80°C'] = 'N/A'
s580.solub['90°C'] = 'N/A'
s580.solub['100°C'] = 'N/A'
sublist.append(s580)

s581 = substance('Strontium formate', 'Sr(HCO2)2')
s581.solub['0°C'] = '9.1'
s581.solub['10°C'] = '10.6'
s581.solub['20°C'] = '12.7'
s581.solub['30°C'] = '15.2'
s581.solub['40°C'] = '17.8'
s581.solub['50°C'] = 'N/A'
s581.solub['60°C'] = '25'
s581.solub['70°C'] = 'N/A'
s581.solub['80°C'] = '31.9'
s581.solub['90°C'] = '32.9'
s581.solub['100°C'] = '34.4'
sublist.append(s581)

s582 = substance('Strontium hydroxide', 'Sr(OH)2.8H2O')
s582.solub['0°C'] = '0.91'
s582.solub['10°C'] = '1.25'
s582.solub['20°C'] = '1.77'
s582.solub['30°C'] = '2.64'
s582.solub['40°C'] = '3.95'
s582.solub['50°C'] = 'N/A'
s582.solub['60°C'] = '8.42'
s582.solub['70°C'] = 'N/A'
s582.solub['80°C'] = '20.2'
s582.solub['90°C'] = '44.5'
s582.solub['100°C'] = '91.2'
sublist.append(s582)

s583 = substance('Strontium iodate', 'Sr(IO3)2')
s583.solub['0°C'] = 'N/A'
s583.solub['10°C'] = 'N/A'
s583.solub['20°C'] = '0.19'
s583.solub['30°C'] = 'N/A'
s583.solub['40°C'] = 'N/A'
s583.solub['50°C'] = 'N/A'
s583.solub['60°C'] = 'N/A'
s583.solub['70°C'] = 'N/A'
s583.solub['80°C'] = 'N/A'
s583.solub['90°C'] = 'N/A'
s583.solub['100°C'] = '0.35'
sublist.append(s583)

s584 = substance('Strontium iodide', 'SrI2')
s584.solub['0°C'] = '165'
s584.solub['10°C'] = 'N/A'
s584.solub['20°C'] = '178'
s584.solub['30°C'] = 'N/A'
s584.solub['40°C'] = '192'
s584.solub['50°C'] = 'N/A'
s584.solub['60°C'] = '218'
s584.solub['70°C'] = 'N/A'
s584.solub['80°C'] = '270'
s584.solub['90°C'] = '365'
s584.solub['100°C'] = '383'
sublist.append(s584)

s585 = substance('Strontium molybdate', 'SrMoO4')
s585.solub['0°C'] = 'N/A'
s585.solub['10°C'] = 'N/A'
s585.solub['20°C'] = '0.01107'
s585.solub['30°C'] = 'N/A'
s585.solub['40°C'] = 'N/A'
s585.solub['50°C'] = 'N/A'
s585.solub['60°C'] = 'N/A'
s585.solub['70°C'] = 'N/A'
s585.solub['80°C'] = 'N/A'
s585.solub['90°C'] = 'N/A'
s585.solub['100°C'] = 'N/A'
sublist.append(s585)

s586 = substance('Strontium nitrate', 'Sr(NO3)2')
s586.solub['0°C'] = '39.5'
s586.solub['10°C'] = '54.9'
s586.solub['20°C'] = '70.8'
s586.solub['30°C'] = '87.6'
s586.solub['40°C'] = '91.3'
s586.solub['50°C'] = '92.6'
s586.solub['60°C'] = '94.0'
s586.solub['70°C'] = '97.2'
s586.solub['80°C'] = '99.0'
s586.solub['90°C'] = '101.1'
s586.solub['100°C'] = 'N/A'
sublist.append(s586)

s587 = substance('Strontium perchlorate', 'Sr(ClO4)2')
s587.solub['0°C'] = '233.8'
s587.solub['10°C'] = '258.7'
s587.solub['20°C'] = '291.7'
s587.solub['30°C'] = '327.5'
s587.solub['40°C'] = '363.9'
s587.solub['50°C'] = 'N/A'
s587.solub['60°C'] = 'N/A'
s587.solub['70°C'] = 'N/A'
s587.solub['80°C'] = 'N/A'
s587.solub['90°C'] = 'N/A'
s587.solub['100°C'] = 'N/A'
sublist.append(s587)

s588 = substance('Strontium selenate', 'SrSeO4')
s588.solub['0°C'] = 'N/A'
s588.solub['10°C'] = 'N/A'
s588.solub['20°C'] = '0.656'
s588.solub['30°C'] = 'N/A'
s588.solub['40°C'] = 'N/A'
s588.solub['50°C'] = 'N/A'
s588.solub['60°C'] = 'N/A'
s588.solub['70°C'] = 'N/A'
s588.solub['80°C'] = 'N/A'
s588.solub['90°C'] = 'N/A'
s588.solub['100°C'] = 'N/A'
sublist.append(s588)

s589 = substance('Strontium sulfate', 'SrSO4')
s589.solub['0°C'] = '0.0113'
s589.solub['10°C'] = '0.0129'
s589.solub['20°C'] = '0.0132'
s589.solub['30°C'] = '0.0138'
s589.solub['40°C'] = '0.0141'
s589.solub['50°C'] = 'N/A'
s589.solub['60°C'] = '0.0131'
s589.solub['70°C'] = 'N/A'
s589.solub['80°C'] = '0.0116'
s589.solub['90°C'] = '0.0115'
s589.solub['100°C'] = 'N/A'
sublist.append(s589)

s590 = substance('Strontium thiosulfate', 'SrS2O3.5H2O')
s590.solub['0°C'] = 'N/A'
s590.solub['10°C'] = '2.5'
s590.solub['20°C'] = 'N/A'
s590.solub['30°C'] = 'N/A'
s590.solub['40°C'] = 'N/A'
s590.solub['50°C'] = 'N/A'
s590.solub['60°C'] = 'N/A'
s590.solub['70°C'] = 'N/A'
s590.solub['80°C'] = 'N/A'
s590.solub['90°C'] = 'N/A'
s590.solub['100°C'] = 'N/A'
sublist.append(s590)

s591 = substance('Strontium tungstate', 'SrWO4')
s591.solub['0°C'] = 'N/A'
s591.solub['10°C'] = 'N/A'
s591.solub['20°C'] = '3.957×10-4'
s591.solub['30°C'] = 'N/A'
s591.solub['40°C'] = 'N/A'
s591.solub['50°C'] = 'N/A'
s591.solub['60°C'] = 'N/A'
s591.solub['70°C'] = 'N/A'
s591.solub['80°C'] = 'N/A'
s591.solub['90°C'] = 'N/A'
s591.solub['100°C'] = 'N/A'
sublist.append(s591)

s592 = substance('Sucrose', 'C12H22O11')
s592.solub['0°C'] = '181.9'
s592.solub['10°C'] = '190.6'
s592.solub['20°C'] = '201.9'
s592.solub['30°C'] = '216.7'
s592.solub['40°C'] = '235.6'
s592.solub['50°C'] = '259.6'
s592.solub['60°C'] = '288.8'
s592.solub['70°C'] = '323.7'
s592.solub['80°C'] = '365.1'
s592.solub['90°C'] = '414.9'
s592.solub['100°C'] = '476.0'
sublist.append(s592)

s593 = substance('Sulfur dioxide', 'SO2')
s593.solub['0°C'] = 'N/A'
s593.solub['10°C'] = 'N/A'
s593.solub['20°C'] = '9.4'
s593.solub['30°C'] = 'N/A'
s593.solub['40°C'] = 'N/A'
s593.solub['50°C'] = 'N/A'
s593.solub['60°C'] = 'N/A'
s593.solub['70°C'] = 'N/A'
s593.solub['80°C'] = 'N/A'
s593.solub['90°C'] = 'N/A'
s593.solub['100°C'] = 'N/A'
sublist.append(s593)

s594 = substance('Terbium bromate', 'Tb(BrO3)3.9H2O')
s594.solub['0°C'] = '66.4'
s594.solub['10°C'] = '89.7'
s594.solub['20°C'] = '117'
s594.solub['30°C'] = '152'
s594.solub['40°C'] = '198'
s594.solub['50°C'] = 'N/A'
s594.solub['60°C'] = 'N/A'
s594.solub['70°C'] = 'N/A'
s594.solub['80°C'] = 'N/A'
s594.solub['90°C'] = 'N/A'
s594.solub['100°C'] = 'N/A'
sublist.append(s594)

s595 = substance('Terbium sulfate', 'Tb2(SO4)3.8H2O')
s595.solub['0°C'] = 'N/A'
s595.solub['10°C'] = 'N/A'
s595.solub['20°C'] = '3.56'
s595.solub['30°C'] = 'N/A'
s595.solub['40°C'] = 'N/A'
s595.solub['50°C'] = 'N/A'
s595.solub['60°C'] = 'N/A'
s595.solub['70°C'] = 'N/A'
s595.solub['80°C'] = 'N/A'
s595.solub['90°C'] = 'N/A'
s595.solub['100°C'] = 'N/A'
sublist.append(s595)

s596 = substance('Thallium(I) azide', 'TlN3')
s596.solub['0°C'] = '0.171'
s596.solub['10°C'] = '0.236'
s596.solub['20°C'] = '0.364'
s596.solub['30°C'] = 'N/A'
s596.solub['40°C'] = 'N/A'
s596.solub['50°C'] = 'N/A'
s596.solub['60°C'] = 'N/A'
s596.solub['70°C'] = 'N/A'
s596.solub['80°C'] = 'N/A'
s596.solub['90°C'] = 'N/A'
s596.solub['100°C'] = 'N/A'
sublist.append(s596)

s597 = substance('Thallium(I) bromate', 'TlBrO3')
s597.solub['0°C'] = 'N/A'
s597.solub['10°C'] = 'N/A'
s597.solub['20°C'] = '0.306'
s597.solub['30°C'] = 'N/A'
s597.solub['40°C'] = 'N/A'
s597.solub['50°C'] = 'N/A'
s597.solub['60°C'] = 'N/A'
s597.solub['70°C'] = 'N/A'
s597.solub['80°C'] = 'N/A'
s597.solub['90°C'] = 'N/A'
s597.solub['100°C'] = 'N/A'
sublist.append(s597)

s598 = substance('Thallium(I) bromide', 'TlBr')
s598.solub['0°C'] = '0.022'
s598.solub['10°C'] = '0.032'
s598.solub['20°C'] = '0.048'
s598.solub['30°C'] = '0.068'
s598.solub['40°C'] = '0.097'
s598.solub['50°C'] = 'N/A'
s598.solub['60°C'] = '0.117'
s598.solub['70°C'] = 'N/A'
s598.solub['80°C'] = 'N/A'
s598.solub['90°C'] = 'N/A'
s598.solub['100°C'] = 'N/A'
sublist.append(s598)

s599 = substance('Thallium(I) carbonate', 'Tl2CO3')
s599.solub['0°C'] = 'N/A'
s599.solub['10°C'] = 'N/A'
s599.solub['20°C'] = '5.3'
s599.solub['30°C'] = 'N/A'
s599.solub['40°C'] = 'N/A'
s599.solub['50°C'] = 'N/A'
s599.solub['60°C'] = 'N/A'
s599.solub['70°C'] = 'N/A'
s599.solub['80°C'] = 'N/A'
s599.solub['90°C'] = 'N/A'
s599.solub['100°C'] = 'N/A'
sublist.append(s599)

s600 = substance('Thallium(I) chlorate', 'TlClO3')
s600.solub['0°C'] = '2'
s600.solub['10°C'] = 'N/A'
s600.solub['20°C'] = '3.92'
s600.solub['30°C'] = 'N/A'
s600.solub['40°C'] = '12.7'
s600.solub['50°C'] = 'N/A'
s600.solub['60°C'] = 'N/A'
s600.solub['70°C'] = 'N/A'
s600.solub['80°C'] = '36.6'
s600.solub['90°C'] = 'N/A'
s600.solub['100°C'] = '57.3'
sublist.append(s600)

s601 = substance('Thallium(I) cyanide', 'TlCN')
s601.solub['0°C'] = 'N/A'
s601.solub['10°C'] = 'N/A'
s601.solub['20°C'] = '16.8'
s601.solub['30°C'] = 'N/A'
s601.solub['40°C'] = 'N/A'
s601.solub['50°C'] = 'N/A'
s601.solub['60°C'] = 'N/A'
s601.solub['70°C'] = 'N/A'
s601.solub['80°C'] = 'N/A'
s601.solub['90°C'] = 'N/A'
s601.solub['100°C'] = 'N/A'
sublist.append(s601)

s602 = substance('Thallium(I) fluoride', 'TlF')
s602.solub['0°C'] = 'N/A'
s602.solub['10°C'] = '78.6(15°C)'
s602.solub['20°C'] = 'N/A'
s602.solub['30°C'] = 'N/A'
s602.solub['40°C'] = 'N/A'
s602.solub['50°C'] = 'N/A'
s602.solub['60°C'] = 'N/A'
s602.solub['70°C'] = 'N/A'
s602.solub['80°C'] = 'N/A'
s602.solub['90°C'] = 'N/A'
s602.solub['100°C'] = 'N/A'
sublist.append(s602)

s603 = substance('Thallium(I) formate', 'TlHCO2')
s603.solub['0°C'] = 'N/A'
s603.solub['10°C'] = 'N/A'
s603.solub['20°C'] = '500'
s603.solub['30°C'] = 'N/A'
s603.solub['40°C'] = 'N/A'
s603.solub['50°C'] = 'N/A'
s603.solub['60°C'] = 'N/A'
s603.solub['70°C'] = 'N/A'
s603.solub['80°C'] = 'N/A'
s603.solub['90°C'] = 'N/A'
s603.solub['100°C'] = 'N/A'
sublist.append(s603)

s604 = substance('Thallium(I) hydroxide', 'TlOH')
s604.solub['0°C'] = '25.4'
s604.solub['10°C'] = '29.6'
s604.solub['20°C'] = '35'
s604.solub['30°C'] = '40.4'
s604.solub['40°C'] = '49.4'
s604.solub['50°C'] = 'N/A'
s604.solub['60°C'] = '73.3'
s604.solub['70°C'] = 'N/A'
s604.solub['80°C'] = '106'
s604.solub['90°C'] = '126'
s604.solub['100°C'] = '150'
sublist.append(s604)

s605 = substance('Thallium(I) iodate', 'TlIO3')
s605.solub['0°C'] = 'N/A'
s605.solub['10°C'] = 'N/A'
s605.solub['20°C'] = '0.06678'
s605.solub['30°C'] = 'N/A'
s605.solub['40°C'] = 'N/A'
s605.solub['50°C'] = 'N/A'
s605.solub['60°C'] = 'N/A'
s605.solub['70°C'] = 'N/A'
s605.solub['80°C'] = 'N/A'
s605.solub['90°C'] = 'N/A'
s605.solub['100°C'] = 'N/A'
sublist.append(s605)

s606 = substance('Thallium(I) iodide', 'TlI')
s606.solub['0°C'] = '0.002'
s606.solub['10°C'] = 'N/A'
s606.solub['20°C'] = '0.006'
s606.solub['30°C'] = 'N/A'
s606.solub['40°C'] = '0.015'
s606.solub['50°C'] = 'N/A'
s606.solub['60°C'] = '0.035'
s606.solub['70°C'] = 'N/A'
s606.solub['80°C'] = '0.07'
s606.solub['90°C'] = 'N/A'
s606.solub['100°C'] = '0.12'
sublist.append(s606)

s607 = substance('Thallium(I) nitrate', 'TlNO3')
s607.solub['0°C'] = '3.9'
s607.solub['10°C'] = '6.22'
s607.solub['20°C'] = '9.55'
s607.solub['30°C'] = '14.3'
s607.solub['40°C'] = '21'
s607.solub['50°C'] = 'N/A'
s607.solub['60°C'] = '46.1'
s607.solub['70°C'] = 'N/A'
s607.solub['80°C'] = '110'
s607.solub['90°C'] = '200'
s607.solub['100°C'] = '414'
sublist.append(s607)

s608 = substance('Thallium(I) oxalate', 'Tl2C2O4')
s608.solub['0°C'] = 'N/A'
s608.solub['10°C'] = 'N/A'
s608.solub['20°C'] = '1.83'
s608.solub['30°C'] = 'N/A'
s608.solub['40°C'] = 'N/A'
s608.solub['50°C'] = 'N/A'
s608.solub['60°C'] = 'N/A'
s608.solub['70°C'] = 'N/A'
s608.solub['80°C'] = 'N/A'
s608.solub['90°C'] = 'N/A'
s608.solub['100°C'] = 'N/A'
sublist.append(s608)

s609 = substance('Thallium(I) perchlorate', 'TlClO4')
s609.solub['0°C'] = '6'
s609.solub['10°C'] = '8.04'
s609.solub['20°C'] = '13.1'
s609.solub['30°C'] = '19.7'
s609.solub['40°C'] = '28.3'
s609.solub['50°C'] = 'N/A'
s609.solub['60°C'] = '50.8'
s609.solub['70°C'] = 'N/A'
s609.solub['80°C'] = '81.5'
s609.solub['90°C'] = 'N/A'
s609.solub['100°C'] = 'N/A'
sublist.append(s609)

s610 = substance('Thallium(I) phosphate', 'Tl3PO4')
s610.solub['0°C'] = 'N/A'
s610.solub['10°C'] = 'N/A'
s610.solub['20°C'] = '0.15'
s610.solub['30°C'] = 'N/A'
s610.solub['40°C'] = 'N/A'
s610.solub['50°C'] = 'N/A'
s610.solub['60°C'] = 'N/A'
s610.solub['70°C'] = 'N/A'
s610.solub['80°C'] = 'N/A'
s610.solub['90°C'] = 'N/A'
s610.solub['100°C'] = 'N/A'
sublist.append(s610)

s611 = substance('Thallium(I) pyrophosphate', 'Tl4P2O7')
s611.solub['0°C'] = 'N/A'
s611.solub['10°C'] = 'N/A'
s611.solub['20°C'] = '40'
s611.solub['30°C'] = 'N/A'
s611.solub['40°C'] = 'N/A'
s611.solub['50°C'] = 'N/A'
s611.solub['60°C'] = 'N/A'
s611.solub['70°C'] = 'N/A'
s611.solub['80°C'] = 'N/A'
s611.solub['90°C'] = 'N/A'
s611.solub['100°C'] = 'N/A'
sublist.append(s611)

s612 = substance('Thallium(I) selenate', 'Tl2SeO4')
s612.solub['0°C'] = 'N/A'
s612.solub['10°C'] = '2.17'
s612.solub['20°C'] = '2.8'
s612.solub['30°C'] = 'N/A'
s612.solub['40°C'] = 'N/A'
s612.solub['50°C'] = 'N/A'
s612.solub['60°C'] = 'N/A'
s612.solub['70°C'] = 'N/A'
s612.solub['80°C'] = '8.5'
s612.solub['90°C'] = 'N/A'
s612.solub['100°C'] = '10.8'
sublist.append(s612)

s613 = substance('Thallium(I) sulfate', 'Tl2SO4')
s613.solub['0°C'] = '2.73'
s613.solub['10°C'] = '3.7'
s613.solub['20°C'] = '4.87'
s613.solub['30°C'] = '6.16'
s613.solub['40°C'] = '7.53'
s613.solub['50°C'] = 'N/A'
s613.solub['60°C'] = '11'
s613.solub['70°C'] = 'N/A'
s613.solub['80°C'] = '14.6'
s613.solub['90°C'] = '16.5'
s613.solub['100°C'] = '18.4'
sublist.append(s613)

s614 = substance('Thallium(I) vanadate', 'TlVO3')
s614.solub['0°C'] = 'N/A'
s614.solub['10°C'] = 'N/A'
s614.solub['20°C'] = '0.87'
s614.solub['30°C'] = 'N/A'
s614.solub['40°C'] = 'N/A'
s614.solub['50°C'] = 'N/A'
s614.solub['60°C'] = 'N/A'
s614.solub['70°C'] = 'N/A'
s614.solub['80°C'] = 'N/A'
s614.solub['90°C'] = 'N/A'
s614.solub['100°C'] = 'N/A'
sublist.append(s614)

s615 = substance('Thorium(IV) fluoride', 'ThF4.4H2O')
s615.solub['0°C'] = 'N/A'
s615.solub['10°C'] = 'N/A'
s615.solub['20°C'] = '0.914'
s615.solub['30°C'] = 'N/A'
s615.solub['40°C'] = 'N/A'
s615.solub['50°C'] = 'N/A'
s615.solub['60°C'] = 'N/A'
s615.solub['70°C'] = 'N/A'
s615.solub['80°C'] = 'N/A'
s615.solub['90°C'] = 'N/A'
s615.solub['100°C'] = 'N/A'
sublist.append(s615)

s616 = substance('Thorium(IV) iodate', 'Th(IO3)4')
s616.solub['0°C'] = 'N/A'
s616.solub['10°C'] = 'N/A'
s616.solub['20°C'] = '0.03691'
s616.solub['30°C'] = 'N/A'
s616.solub['40°C'] = 'N/A'
s616.solub['50°C'] = 'N/A'
s616.solub['60°C'] = 'N/A'
s616.solub['70°C'] = 'N/A'
s616.solub['80°C'] = 'N/A'
s616.solub['90°C'] = 'N/A'
s616.solub['100°C'] = 'N/A'
sublist.append(s616)

s617 = substance('Thorium(IV) nitrate', 'Th(NO3)4')
s617.solub['0°C'] = '186'
s617.solub['10°C'] = '187'
s617.solub['20°C'] = '191'
s617.solub['30°C'] = 'N/A'
s617.solub['40°C'] = 'N/A'
s617.solub['50°C'] = 'N/A'
s617.solub['60°C'] = 'N/A'
s617.solub['70°C'] = 'N/A'
s617.solub['80°C'] = 'N/A'
s617.solub['90°C'] = 'N/A'
s617.solub['100°C'] = 'N/A'
sublist.append(s617)

s618 = substance('Thorium(IV) selenate', 'Th(SeO4)2.9H2O')
s618.solub['0°C'] = '0.65'
s618.solub['10°C'] = 'N/A'
s618.solub['20°C'] = 'N/A'
s618.solub['30°C'] = 'N/A'
s618.solub['40°C'] = 'N/A'
s618.solub['50°C'] = 'N/A'
s618.solub['60°C'] = 'N/A'
s618.solub['70°C'] = 'N/A'
s618.solub['80°C'] = 'N/A'
s618.solub['90°C'] = 'N/A'
s618.solub['100°C'] = 'N/A'
sublist.append(s618)

s619 = substance('Thorium(IV) sulfate', 'Th(SO4)2.9H2O')
s619.solub['0°C'] = '0.74'
s619.solub['10°C'] = '0.99'
s619.solub['20°C'] = '1.38'
s619.solub['30°C'] = '1.99'
s619.solub['40°C'] = '3'
s619.solub['50°C'] = 'N/A'
s619.solub['60°C'] = 'N/A'
s619.solub['70°C'] = 'N/A'
s619.solub['80°C'] = 'N/A'
s619.solub['90°C'] = 'N/A'
s619.solub['100°C'] = 'N/A'
sublist.append(s619)

s620 = substance('Thulium(III) nitrate', 'Tm(NO3)3')
s620.solub['0°C'] = 'N/A'
s620.solub['10°C'] = 'N/A'
s620.solub['20°C'] = '212'
s620.solub['30°C'] = 'N/A'
s620.solub['40°C'] = 'N/A'
s620.solub['50°C'] = 'N/A'
s620.solub['60°C'] = 'N/A'
s620.solub['70°C'] = 'N/A'
s620.solub['80°C'] = 'N/A'
s620.solub['90°C'] = 'N/A'
s620.solub['100°C'] = 'N/A'
sublist.append(s620)

s621 = substance('Tin(II) bromide', 'SnBr2')
s621.solub['0°C'] = '85'
s621.solub['10°C'] = 'N/A'
s621.solub['20°C'] = 'N/A'
s621.solub['30°C'] = 'N/A'
s621.solub['40°C'] = 'N/A'
s621.solub['50°C'] = 'N/A'
s621.solub['60°C'] = 'N/A'
s621.solub['70°C'] = 'N/A'
s621.solub['80°C'] = 'N/A'
s621.solub['90°C'] = 'N/A'
s621.solub['100°C'] = 'N/A'
sublist.append(s621)

s622 = substance('Tin(II) chloride', 'SnCl2')
s622.solub['0°C'] = '84'
s622.solub['10°C'] = 'N/A'
s622.solub['20°C'] = 'N/A'
s622.solub['30°C'] = 'N/A'
s622.solub['40°C'] = 'N/A'
s622.solub['50°C'] = 'N/A'
s622.solub['60°C'] = 'N/A'
s622.solub['70°C'] = 'N/A'
s622.solub['80°C'] = 'N/A'
s622.solub['90°C'] = 'N/A'
s622.solub['100°C'] = 'N/A'
sublist.append(s622)

s623 = substance('Tin(II) fluoride', 'SnF2')
s623.solub['0°C'] = 'N/A'
s623.solub['10°C'] = 'N/A'
s623.solub['20°C'] = '30'
s623.solub['30°C'] = 'N/A'
s623.solub['40°C'] = 'N/A'
s623.solub['50°C'] = 'N/A'
s623.solub['60°C'] = 'N/A'
s623.solub['70°C'] = 'N/A'
s623.solub['80°C'] = 'N/A'
s623.solub['90°C'] = 'N/A'
s623.solub['100°C'] = 'N/A'
sublist.append(s623)

s624 = substance('Tin(II) iodide', 'SnI2')
s624.solub['0°C'] = 'N/A'
s624.solub['10°C'] = 'N/A'
s624.solub['20°C'] = '0.99'
s624.solub['30°C'] = '1.17'
s624.solub['40°C'] = '1.42'
s624.solub['50°C'] = 'N/A'
s624.solub['60°C'] = '2.11'
s624.solub['70°C'] = 'N/A'
s624.solub['80°C'] = '3.04'
s624.solub['90°C'] = '3.58'
s624.solub['100°C'] = '4.2'
sublist.append(s624)

s625 = substance('Tin(II) sulfate', 'SnSO4')
s625.solub['0°C'] = 'N/A'
s625.solub['10°C'] = 'N/A'
s625.solub['20°C'] = '18.9'
s625.solub['30°C'] = 'N/A'
s625.solub['40°C'] = 'N/A'
s625.solub['50°C'] = 'N/A'
s625.solub['60°C'] = 'N/A'
s625.solub['70°C'] = 'N/A'
s625.solub['80°C'] = 'N/A'
s625.solub['90°C'] = 'N/A'
s625.solub['100°C'] = 'N/A'
sublist.append(s625)

s626 = substance('Trehalose', 'C12H22O11')
s626.solub['0°C'] = 'N/A'
s626.solub['10°C'] = 'N/A'
s626.solub['20°C'] = '68.9'
s626.solub['30°C'] = 'N/A'
s626.solub['40°C'] = 'N/A'
s626.solub['50°C'] = 'N/A'
s626.solub['60°C'] = 'N/A'
s626.solub['70°C'] = 'N/A'
s626.solub['80°C'] = 'N/A'
s626.solub['90°C'] = 'N/A'
s626.solub['100°C'] = 'N/A'
sublist.append(s626)

s627 = substance('Uranyl acetate', 'UO2(C2H3O2)2.2H2O')
s627.solub['0°C'] = 'N/A'
s627.solub['10°C'] = 'N/A'
s627.solub['20°C'] = '7.69'
s627.solub['30°C'] = 'N/A'
s627.solub['40°C'] = 'N/A'
s627.solub['50°C'] = 'N/A'
s627.solub['60°C'] = 'N/A'
s627.solub['70°C'] = 'N/A'
s627.solub['80°C'] = 'N/A'
s627.solub['90°C'] = 'N/A'
s627.solub['100°C'] = 'N/A'
sublist.append(s627)

s628 = substance('Uranyl chloride', 'UO2Cl2')
s628.solub['0°C'] = 'N/A'
s628.solub['10°C'] = 'N/A'
s628.solub['20°C'] = '320'
s628.solub['30°C'] = 'N/A'
s628.solub['40°C'] = 'N/A'
s628.solub['50°C'] = 'N/A'
s628.solub['60°C'] = 'N/A'
s628.solub['70°C'] = 'N/A'
s628.solub['80°C'] = 'N/A'
s628.solub['90°C'] = 'N/A'
s628.solub['100°C'] = 'N/A'
sublist.append(s628)

s629 = substance('Uranyl formate', 'UO2(HCO2)2.H2O')
s629.solub['0°C'] = 'N/A'
s629.solub['10°C'] = 'N/A'
s629.solub['20°C'] = '7.2'
s629.solub['30°C'] = 'N/A'
s629.solub['40°C'] = 'N/A'
s629.solub['50°C'] = 'N/A'
s629.solub['60°C'] = 'N/A'
s629.solub['70°C'] = 'N/A'
s629.solub['80°C'] = 'N/A'
s629.solub['90°C'] = 'N/A'
s629.solub['100°C'] = 'N/A'
sublist.append(s629)

s630 = substance('Uranyl iodate', 'UO2(IO3)2.H2O')
s630.solub['0°C'] = 'N/A'
s630.solub['10°C'] = 'N/A'
s630.solub['20°C'] = '0.124'
s630.solub['30°C'] = 'N/A'
s630.solub['40°C'] = 'N/A'
s630.solub['50°C'] = 'N/A'
s630.solub['60°C'] = 'N/A'
s630.solub['70°C'] = 'N/A'
s630.solub['80°C'] = 'N/A'
s630.solub['90°C'] = 'N/A'
s630.solub['100°C'] = 'N/A'
sublist.append(s630)

s631 = substance('Uranyl nitrate', 'UO2(NO3)2')
s631.solub['0°C'] = '98'
s631.solub['10°C'] = '107'
s631.solub['20°C'] = '122'
s631.solub['30°C'] = '141'
s631.solub['40°C'] = '167'
s631.solub['50°C'] = 'N/A'
s631.solub['60°C'] = '317'
s631.solub['70°C'] = 'N/A'
s631.solub['80°C'] = '388'
s631.solub['90°C'] = '426'
s631.solub['100°C'] = '474'
sublist.append(s631)

s632 = substance('Uranyl oxalate', 'UO2C2O4')
s632.solub['0°C'] = 'N/A'
s632.solub['10°C'] = '0.45'
s632.solub['20°C'] = '0.5'
s632.solub['30°C'] = '0.61'
s632.solub['40°C'] = '0.8'
s632.solub['50°C'] = 'N/A'
s632.solub['60°C'] = '1.22'
s632.solub['70°C'] = 'N/A'
s632.solub['80°C'] = '1.94'
s632.solub['90°C'] = 'N/A'
s632.solub['100°C'] = '3.16'
sublist.append(s632)

s633 = substance('Uranyl sulfate', 'UO2SO4.3H2O')
s633.solub['0°C'] = 'N/A'
s633.solub['10°C'] = 'N/A'
s633.solub['20°C'] = '21'
s633.solub['30°C'] = 'N/A'
s633.solub['40°C'] = 'N/A'
s633.solub['50°C'] = 'N/A'
s633.solub['60°C'] = 'N/A'
s633.solub['70°C'] = 'N/A'
s633.solub['80°C'] = 'N/A'
s633.solub['90°C'] = 'N/A'
s633.solub['100°C'] = 'N/A'
sublist.append(s633)

s634 = substance('Urea', 'CO(NH2)2')
s634.solub['0°C'] = 'N/A'
s634.solub['10°C'] = 'N/A'
s634.solub['20°C'] = '108'
s634.solub['30°C'] = 'N/A'
s634.solub['40°C'] = '167'
s634.solub['50°C'] = 'N/A'
s634.solub['60°C'] = '251'
s634.solub['70°C'] = 'N/A'
s634.solub['80°C'] = '400'
s634.solub['90°C'] = 'N/A'
s634.solub['100°C'] = '733'
sublist.append(s634)

s635 = substance('Vanadium(V) oxide', 'V2O5')
s635.solub['0°C'] = 'N/A'
s635.solub['10°C'] = 'N/A'
s635.solub['20°C'] = '0.8'
s635.solub['30°C'] = 'N/A'
s635.solub['40°C'] = 'N/A'
s635.solub['50°C'] = 'N/A'
s635.solub['60°C'] = 'N/A'
s635.solub['70°C'] = 'N/A'
s635.solub['80°C'] = 'N/A'
s635.solub['90°C'] = 'N/A'
s635.solub['100°C'] = 'N/A'
sublist.append(s635)

s636 = substance('Xenon', 'Xe')
s636.solub['0°C'] = '24.1ml'
s636.solub['10°C'] = 'N/A'
s636.solub['20°C'] = '11.9ml25'
s636.solub['30°C'] = 'N/A'
s636.solub['40°C'] = 'N/A'
s636.solub['50°C'] = '8.4ml'
s636.solub['60°C'] = 'N/A'
s636.solub['70°C'] = 'N/A'
s636.solub['80°C'] = '7.12ml'
s636.solub['90°C'] = 'N/A'
s636.solub['100°C'] = 'N/A'
sublist.append(s636)

s637 = substance('Xylose', 'C5H10O5')
s637.solub['0°C'] = 'N/A'
s637.solub['10°C'] = 'N/A'
s637.solub['20°C'] = '117'
s637.solub['30°C'] = 'N/A'
s637.solub['40°C'] = 'N/A'
s637.solub['50°C'] = 'N/A'
s637.solub['60°C'] = 'N/A'
s637.solub['70°C'] = 'N/A'
s637.solub['80°C'] = 'N/A'
s637.solub['90°C'] = 'N/A'
s637.solub['100°C'] = 'N/A'
sublist.append(s637)

s638 = substance('Ytterbium(III) nitrate', 'Yb(NO3)3')
s638.solub['0°C'] = 'N/A'
s638.solub['10°C'] = 'N/A'
s638.solub['20°C'] = '239'
s638.solub['30°C'] = 'N/A'
s638.solub['40°C'] = 'N/A'
s638.solub['50°C'] = 'N/A'
s638.solub['60°C'] = 'N/A'
s638.solub['70°C'] = 'N/A'
s638.solub['80°C'] = 'N/A'
s638.solub['90°C'] = 'N/A'
s638.solub['100°C'] = 'N/A'
sublist.append(s638)

s639 = substance('Ytterbium(III) sulfate', 'Yb2(SO4)3')
s639.solub['0°C'] = '44.2'
s639.solub['10°C'] = '37.5'
s639.solub['20°C'] = '38.4'
s639.solub['30°C'] = '22.2'
s639.solub['40°C'] = '17.2'
s639.solub['50°C'] = 'N/A'
s639.solub['60°C'] = '10.4'
s639.solub['70°C'] = 'N/A'
s639.solub['80°C'] = '6.4'
s639.solub['90°C'] = '5.8'
s639.solub['100°C'] = '4.7'
sublist.append(s639)

s640 = substance('Yttrium(III) acetate', 'Y(C2H3O2)3.4H2O')
s640.solub['0°C'] = 'N/A'
s640.solub['10°C'] = 'N/A'
s640.solub['20°C'] = '9.03'
s640.solub['30°C'] = 'N/A'
s640.solub['40°C'] = 'N/A'
s640.solub['50°C'] = 'N/A'
s640.solub['60°C'] = 'N/A'
s640.solub['70°C'] = 'N/A'
s640.solub['80°C'] = 'N/A'
s640.solub['90°C'] = 'N/A'
s640.solub['100°C'] = 'N/A'
sublist.append(s640)

s641 = substance('Yttrium(III) bromate', 'Y(BrO3)3.9H2O')
s641.solub['0°C'] = 'N/A'
s641.solub['10°C'] = 'N/A'
s641.solub['20°C'] = '168'
s641.solub['30°C'] = 'N/A'
s641.solub['40°C'] = 'N/A'
s641.solub['50°C'] = 'N/A'
s641.solub['60°C'] = 'N/A'
s641.solub['70°C'] = 'N/A'
s641.solub['80°C'] = 'N/A'
s641.solub['90°C'] = 'N/A'
s641.solub['100°C'] = 'N/A'
sublist.append(s641)

s642 = substance('Yttrium(III) bromide', 'YBr3')
s642.solub['0°C'] = '63.9'
s642.solub['10°C'] = 'N/A'
s642.solub['20°C'] = '75.1'
s642.solub['30°C'] = 'N/A'
s642.solub['40°C'] = '87.3'
s642.solub['50°C'] = 'N/A'
s642.solub['60°C'] = '101'
s642.solub['70°C'] = 'N/A'
s642.solub['80°C'] = '116'
s642.solub['90°C'] = '123'
s642.solub['100°C'] = 'N/A'
sublist.append(s642)

s643 = substance('Yttrium(III) chloride', 'YCl3')
s643.solub['0°C'] = '77.3'
s643.solub['10°C'] = '78.1'
s643.solub['20°C'] = '78.8'
s643.solub['30°C'] = '79.6'
s643.solub['40°C'] = '80.8'
s643.solub['50°C'] = 'N/A'
s643.solub['60°C'] = 'N/A'
s643.solub['70°C'] = 'N/A'
s643.solub['80°C'] = 'N/A'
s643.solub['90°C'] = 'N/A'
s643.solub['100°C'] = 'N/A'
sublist.append(s643)

s644 = substance('Yttrium(III) fluoride', 'YF3')
s644.solub['0°C'] = 'N/A'
s644.solub['10°C'] = 'N/A'
s644.solub['20°C'] = '0.005769'
s644.solub['30°C'] = 'N/A'
s644.solub['40°C'] = 'N/A'
s644.solub['50°C'] = 'N/A'
s644.solub['60°C'] = 'N/A'
s644.solub['70°C'] = 'N/A'
s644.solub['80°C'] = 'N/A'
s644.solub['90°C'] = 'N/A'
s644.solub['100°C'] = 'N/A'
sublist.append(s644)

s645 = substance('Yttrium(III) nitrate', 'Y(NO3)3')
s645.solub['0°C'] = '93.1'
s645.solub['10°C'] = '106'
s645.solub['20°C'] = '123'
s645.solub['30°C'] = '143'
s645.solub['40°C'] = '163'
s645.solub['50°C'] = 'N/A'
s645.solub['60°C'] = '200'
s645.solub['70°C'] = 'N/A'
s645.solub['80°C'] = 'N/A'
s645.solub['90°C'] = 'N/A'
s645.solub['100°C'] = 'N/A'
sublist.append(s645)

s646 = substance('Yttrium(III) sulfate', 'Y2(SO4)3')
s646.solub['0°C'] = '8.05'
s646.solub['10°C'] = '7.67'
s646.solub['20°C'] = '7.3'
s646.solub['30°C'] = '6.78'
s646.solub['40°C'] = '6.09'
s646.solub['50°C'] = 'N/A'
s646.solub['60°C'] = '4.44'
s646.solub['70°C'] = 'N/A'
s646.solub['80°C'] = '2.89'
s646.solub['90°C'] = '2.2'
s646.solub['100°C'] = 'N/A'
sublist.append(s646)

s647 = substance('Zinc acetate', 'Zn(C2H3O2)2')
s647.solub['0°C'] = 'N/A'
s647.solub['10°C'] = 'N/A'
s647.solub['20°C'] = '30'
s647.solub['30°C'] = 'N/A'
s647.solub['40°C'] = 'N/A'
s647.solub['50°C'] = 'N/A'
s647.solub['60°C'] = 'N/A'
s647.solub['70°C'] = 'N/A'
s647.solub['80°C'] = 'N/A'
s647.solub['90°C'] = 'N/A'
s647.solub['100°C'] = 'N/A'
sublist.append(s647)

s648 = substance('Zinc bromide', 'ZnBr2')
s648.solub['0°C'] = '389'
s648.solub['10°C'] = 'N/A'
s648.solub['20°C'] = '446'
s648.solub['30°C'] = '528'
s648.solub['40°C'] = '591'
s648.solub['50°C'] = 'N/A'
s648.solub['60°C'] = '618'
s648.solub['70°C'] = 'N/A'
s648.solub['80°C'] = '645'
s648.solub['90°C'] = 'N/A'
s648.solub['100°C'] = '672'
sublist.append(s648)

s649 = substance('Zinc carbonate', 'ZnCO3')
s649.solub['0°C'] = 'N/A'
s649.solub['10°C'] = 'N/A'
s649.solub['20°C'] = '4.692×10-5'
s649.solub['30°C'] = 'N/A'
s649.solub['40°C'] = 'N/A'
s649.solub['50°C'] = 'N/A'
s649.solub['60°C'] = 'N/A'
s649.solub['70°C'] = 'N/A'
s649.solub['80°C'] = 'N/A'
s649.solub['90°C'] = 'N/A'
s649.solub['100°C'] = 'N/A'
sublist.append(s649)

s650 = substance('Zinc chlorate', 'Zn(ClO3)2')
s650.solub['0°C'] = '145'
s650.solub['10°C'] = '152'
s650.solub['20°C'] = '209'
s650.solub['30°C'] = '223'
s650.solub['40°C'] = 'N/A'
s650.solub['50°C'] = 'N/A'
s650.solub['60°C'] = 'N/A'
s650.solub['70°C'] = 'N/A'
s650.solub['80°C'] = 'N/A'
s650.solub['90°C'] = 'N/A'
s650.solub['100°C'] = 'N/A'
sublist.append(s650)

s651 = substance('Zinc chloride', 'ZnCl2')
s651.solub['0°C'] = '342'
s651.solub['10°C'] = '353'
s651.solub['20°C'] = '395'
s651.solub['30°C'] = '437'
s651.solub['40°C'] = '452'
s651.solub['50°C'] = 'N/A'
s651.solub['60°C'] = '488'
s651.solub['70°C'] = 'N/A'
s651.solub['80°C'] = '541'
s651.solub['90°C'] = 'N/A'
s651.solub['100°C'] = '614'
sublist.append(s651)

s652 = substance('Zinc cyanide', 'Zn(CN)2')
s652.solub['0°C'] = 'N/A'
s652.solub['10°C'] = 'N/A'
s652.solub['20°C'] = '0.058'
s652.solub['30°C'] = 'N/A'
s652.solub['40°C'] = 'N/A'
s652.solub['50°C'] = 'N/A'
s652.solub['60°C'] = 'N/A'
s652.solub['70°C'] = 'N/A'
s652.solub['80°C'] = 'N/A'
s652.solub['90°C'] = 'N/A'
s652.solub['100°C'] = 'N/A'
sublist.append(s652)

s653 = substance('Zinc fluoride', 'ZnF2')
s653.solub['0°C'] = 'N/A'
s653.solub['10°C'] = 'N/A'
s653.solub['20°C'] = '1.6'
s653.solub['30°C'] = 'N/A'
s653.solub['40°C'] = 'N/A'
s653.solub['50°C'] = 'N/A'
s653.solub['60°C'] = 'N/A'
s653.solub['70°C'] = 'N/A'
s653.solub['80°C'] = 'N/A'
s653.solub['90°C'] = 'N/A'
s653.solub['100°C'] = 'N/A'
sublist.append(s653)

s654 = substance('Zinc formate', 'Zn(HCO2)2')
s654.solub['0°C'] = '3.7'
s654.solub['10°C'] = '4.3'
s654.solub['20°C'] = '6.1'
s654.solub['30°C'] = '7.4'
s654.solub['40°C'] = 'N/A'
s654.solub['50°C'] = '11.8'
s654.solub['60°C'] = 'N/A'
s654.solub['70°C'] = '21.2'
s654.solub['80°C'] = '28.8'
s654.solub['90°C'] = '38'
s654.solub['100°C'] = 'N/A'
sublist.append(s654)

s655 = substance('Zinc iodate', 'Zn(IO3)2.2H2O')
s655.solub['0°C'] = 'N/A'
s655.solub['10°C'] = 'N/A'
s655.solub['20°C'] = '0.07749'
s655.solub['30°C'] = 'N/A'
s655.solub['40°C'] = 'N/A'
s655.solub['50°C'] = 'N/A'
s655.solub['60°C'] = 'N/A'
s655.solub['70°C'] = 'N/A'
s655.solub['80°C'] = 'N/A'
s655.solub['90°C'] = 'N/A'
s655.solub['100°C'] = 'N/A'
sublist.append(s655)

s656 = substance('Zinc iodide', 'ZnI2')
s656.solub['0°C'] = '430'
s656.solub['10°C'] = 'N/A'
s656.solub['20°C'] = '432'
s656.solub['30°C'] = 'N/A'
s656.solub['40°C'] = '445'
s656.solub['50°C'] = 'N/A'
s656.solub['60°C'] = '467'
s656.solub['70°C'] = 'N/A'
s656.solub['80°C'] = '490'
s656.solub['90°C'] = 'N/A'
s656.solub['100°C'] = '510'
sublist.append(s656)

s657 = substance('Zinc nitrate', 'Zn(NO3)2')
s657.solub['0°C'] = '98'
s657.solub['10°C'] = 'N/A'
s657.solub['20°C'] = 'N/A'
s657.solub['30°C'] = '138'
s657.solub['40°C'] = '211'
s657.solub['50°C'] = 'N/A'
s657.solub['60°C'] = 'N/A'
s657.solub['70°C'] = 'N/A'
s657.solub['80°C'] = 'N/A'
s657.solub['90°C'] = 'N/A'
s657.solub['100°C'] = 'N/A'
sublist.append(s657)

s658 = substance('Zinc oxalate', 'ZnC2O4.2H2O')
s658.solub['0°C'] = 'N/A'
s658.solub['10°C'] = 'N/A'
s658.solub['20°C'] = '1.38×10-9'
s658.solub['30°C'] = 'N/A'
s658.solub['40°C'] = 'N/A'
s658.solub['50°C'] = 'N/A'
s658.solub['60°C'] = 'N/A'
s658.solub['70°C'] = 'N/A'
s658.solub['80°C'] = 'N/A'
s658.solub['90°C'] = 'N/A'
s658.solub['100°C'] = 'N/A'
sublist.append(s658)

s659 = substance('Zinc permanganate', 'Zn(MnO4)2')
s659.solub['0°C'] = 'N/A'
s659.solub['10°C'] = 'N/A'
s659.solub['20°C'] = '33.3'
s659.solub['30°C'] = 'N/A'
s659.solub['40°C'] = 'N/A'
s659.solub['50°C'] = 'N/A'
s659.solub['60°C'] = 'N/A'
s659.solub['70°C'] = 'N/A'
s659.solub['80°C'] = 'N/A'
s659.solub['90°C'] = 'N/A'
s659.solub['100°C'] = 'N/A'
sublist.append(s659)

s660 = substance('Zinc sulfate', 'ZnSO4')
s660.solub['0°C'] = '41.6'
s660.solub['10°C'] = '47.2'
s660.solub['20°C'] = '53.8'
s660.solub['30°C'] = '61.3'
s660.solub['40°C'] = '70.5'
s660.solub['50°C'] = 'N/A'
s660.solub['60°C'] = '75.4'
s660.solub['70°C'] = 'N/A'
s660.solub['80°C'] = '71.1'
s660.solub['90°C'] = 'N/A'
s660.solub['100°C'] = '60.5'
sublist.append(s660)

s661 = substance('Zinc sulfite', 'ZnSO3.2H2O')
s661.solub['0°C'] = 'N/A'
s661.solub['10°C'] = 'N/A'
s661.solub['20°C'] = '0.16'
s661.solub['30°C'] = 'N/A'
s661.solub['40°C'] = 'N/A'
s661.solub['50°C'] = 'N/A'
s661.solub['60°C'] = 'N/A'
s661.solub['70°C'] = 'N/A'
s661.solub['80°C'] = 'N/A'
s661.solub['90°C'] = 'N/A'
s661.solub['100°C'] = 'N/A'
sublist.append(s661)

s662 = substance('Zinc tartrate', 'ZnC4H4O6')
s662.solub['0°C'] = 'N/A'
s662.solub['10°C'] = 'N/A'
s662.solub['20°C'] = '0.022'
s662.solub['30°C'] = '0.041'
s662.solub['40°C'] = '0.06'
s662.solub['50°C'] = 'N/A'
s662.solub['60°C'] = '0.104'
s662.solub['70°C'] = 'N/A'
s662.solub['80°C'] = '0.59'
s662.solub['90°C'] = 'N/A'
s662.solub['100°C'] = 'N/A'
sublist.append(s662)

s663 = substance('Zirconium fluoride', 'ZrF4')
s663.solub['0°C'] = 'N/A'
s663.solub['10°C'] = 'N/A'
s663.solub['20°C'] = '1.32'
s663.solub['30°C'] = 'N/A'
s663.solub['40°C'] = 'N/A'
s663.solub['50°C'] = 'N/A'
s663.solub['60°C'] = 'N/A'
s663.solub['70°C'] = 'N/A'
s663.solub['80°C'] = 'N/A'
s663.solub['90°C'] = 'N/A'
s663.solub['100°C'] = 'N/A'
sublist.append(s663)

s664 = substance('Zirconium sulfate', 'Zr(SO4)2.4H2O')
s664.solub['0°C'] = 'N/A'
s664.solub['10°C'] = 'N/A'
s664.solub['20°C'] = '52.5'
s664.solub['30°C'] = 'N/A'
s664.solub['40°C'] = 'N/A'
s664.solub['50°C'] = 'N/A'
s664.solub['60°C'] = 'N/A'
s664.solub['70°C'] = 'N/A'
s664.solub['80°C'] = 'N/A'
s664.solub['90°C'] = 'N/A'
s664.solub['100°C'] = 'N/A'
sublist.append(s664)
