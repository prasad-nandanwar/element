at_no= int(input('atomic number: '))
class element():
    def __init__(self):
        if at_no >> 0:
            pass
        else:
            print('atomic number can never be negative')
    def symbol(self, at_no):
        symbol_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca','Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y','Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La','Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re','Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np','Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg','Uub']
        self = symbol_list[at_no-1]
        print('atomic sumbol: ', self )
    def name(self, at_no):
        name_list = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon','Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Ununbiium']
        self = name_list[at_no - 1]
        print('chemical name: ', self)
    def mass(self, at_no):
        mass_list = [1.00797, 4.0026, 6.941, 9.01218, 10.81, 12.011, 14.0067, 15.9994, 18.998403, 20.179, 22.98977, 24.305, 26.98154, 28.0855, 30.97376, 32.06, 35.453, 39.948, 39.0983, 40.08, 44.9559, 47.9, 50.9415, 51.996, 54.938, 55.847, 58.9332, 58.7, 63.546, 65.38, 69.72, 72.59, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.22, 92.9064, 95.94, 98, 101.07, 102.9055, 106.4, 107.868, 112.41, 114.82, 118.69, 121.75, 127.6, 126.9045, 131.3, 132.9054, 137.33, 138.9055, 140.12, 140.9077, 144.24, 145, 150.4, 151.96, 157.25, 158.9254, 162.5, 164.9304, 167.26, 168.9342, 173.04, 174.967, 178.49, 180.9479, 183.85, 186.207, 190.2, 192.22, 195.09, 196.9665, 200.59, 204.37, 207.2, 208.9804, 209, 210, 222, 223, 226.0254, 227.0278, 232.0381, 231.0359, 238.029, 237.0482, 242, 243, 247, 247, 251, 252, 257, 258, 250, 260, 261, 262, 263, 262, 255, 256, 269, 272, 277]
        self = mass_list[at_no - 1]
        print('atomic mass: ',self, ' gm/mol')
    def proton(self,at_no):
        self=at_no
        print('number of protons: ', self)
    def electron(self,at_no):
        self=at_no
        print('number of electrons: ', self)
    def neutron(self, at_no ):
        mass_list = [1.00797, 4.0026, 6.941, 9.01218, 10.81, 12.011, 14.0067, 15.9994, 18.998403, 20.179, 22.98977, 24.305, 26.98154, 28.0855, 30.97376, 32.06, 35.453, 39.948, 39.0983, 40.08, 44.9559, 47.9, 50.9415, 51.996, 54.938, 55.847, 58.9332, 58.7, 63.546, 65.38, 69.72, 72.59, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.22, 92.9064, 95.94, 98, 101.07, 102.9055, 106.4, 107.868, 112.41, 114.82, 118.69, 121.75, 127.6, 126.9045, 131.3, 132.9054, 137.33, 138.9055, 140.12, 140.9077, 144.24, 145, 150.4, 151.96, 157.25, 158.9254, 162.5, 164.9304, 167.26, 168.9342, 173.04, 174.967, 178.49, 180.9479, 183.85, 186.207, 190.2, 192.22, 195.09, 196.9665, 200.59, 204.37, 207.2, 208.9804, 209, 210, 222, 223, 226.0254, 227.0278, 232.0381, 231.0359, 238.029, 237.0482, 242, 243, 247, 247, 251, 252, 257, 258, 250, 260, 261, 262, 263, 262, 255, 256, 269, 272, 277]
        chemical_mass = mass_list[at_no - 1]
        self = round(chemical_mass - at_no)
        print('number of neutrons: ', self)
    def orbit(self,at_no):
        n = 0
        v = at_no
        while v > 2 * n * n:
            n = n + 1
            v = v - 2 * (n - 1) * (n - 1)
        self = n
        print('number of orbits: ', self)
    def valence_electrons(self,at_no):
        n = 0
        v = at_no
        while v > 2 * n * n:
            n = n + 1
            v = v - 2 * (n - 1) * (n - 1)
        self = v
        print('number of valance electrons: ', self)
    def valency(self,at_no):
        n = 0
        v = at_no
        while v > 2 * n * n:
            n = n + 1
            v = v - 2 * (n - 1) * (n - 1)
        if v > 8:
            self = 2 * n * n - v
        else:
            self = v
        while self >= 12:
            self = self - 8
        print('valency: ', self)
    def mass_defect(self, at_no):
        if at_no==1:
            print('mass defect: none')
        else:
            mass_list = [1.00797, 4.0026, 6.941, 9.01218, 10.81, 12.011, 14.0067, 15.9994, 18.998403, 20.179, 22.98977,24.305, 26.98154, 28.0855, 30.97376, 32.06, 35.453, 39.948, 39.0983, 40.08, 44.9559, 47.9, 50.9415,51.996, 54.938, 55.847, 58.9332, 58.7, 63.546, 65.38, 69.72, 72.59, 74.9216, 78.96, 79.904, 83.8,85.4678, 87.62, 88.9059, 91.22, 92.9064, 95.94, 98, 101.07, 102.9055, 106.4, 107.868, 112.41,114.82, 118.69, 121.75, 127.6, 126.9045, 131.3, 132.9054, 137.33, 138.9055, 140.12, 140.9077,144.24, 145, 150.4, 151.96, 157.25, 158.9254, 162.5, 164.9304, 167.26, 168.9342, 173.04, 174.967,178.49, 180.9479, 183.85, 186.207, 190.2, 192.22, 195.09, 196.9665, 200.59, 204.37, 207.2,208.9804, 209, 210, 222, 223, 226.0254, 227.0278, 232.0381, 231.0359, 238.029, 237.0482, 242, 243,247, 247, 251, 252, 257, 258, 250, 260, 261, 262, 263, 262, 255, 256, 269, 272, 277]
            self = at_no * (1.00785) + (mass_list[at_no - 1] - at_no) * (1.0087) - mass_list[at_no - 1]
            print('mass defect: ', self, 'g/mol')
    def binding_energy(self, at_no):
        mass_list = [1.00797, 4.0026, 6.941, 9.01218, 10.81, 12.011, 14.0067, 15.9994, 18.998403, 20.179, 22.98977, 24.305, 26.98154, 28.0855, 30.97376, 32.06, 35.453, 39.948, 39.0983, 40.08, 44.9559, 47.9, 50.9415, 51.996, 54.938, 55.847, 58.9332, 58.7, 63.546, 65.38, 69.72, 72.59, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.22, 92.9064, 95.94, 98, 101.07, 102.9055, 106.4, 107.868, 112.41, 114.82, 118.69, 121.75, 127.6, 126.9045, 131.3, 132.9054, 137.33, 138.9055, 140.12, 140.9077, 144.24, 145, 150.4, 151.96, 157.25, 158.9254, 162.5, 164.9304, 167.26, 168.9342, 173.04, 174.967, 178.49, 180.9479, 183.85, 186.207, 190.2, 192.22, 195.09, 196.9665, 200.59, 204.37, 207.2, 208.9804, 209, 210, 222, 223, 226.0254, 227.0278, 232.0381, 231.0359, 238.029, 237.0482, 242, 243, 247, 247, 251, 252, 257, 258, 250, 260, 261, 262, 263, 262, 255, 256, 269, 272, 277]
        self = abs((((at_no * (1.00785) + round(mass_list[at_no - 1] - at_no) * (1.0087) - mass_list[at_no - 1]))/1000)*(2.998*100000000)**2)
        print('binding energy: ', self , 'J/mol','=', self/1000000000000, 'TJ/mol')
atom = element()
atom.symbol( at_no)
atom.name(at_no)
atom.mass(at_no)
atom.proton(at_no)
atom.electron(at_no)
atom.neutron(at_no)
atom.valency(at_no)
atom.valence_electrons(at_no)
atom.orbit(at_no)
atom.mass_defect(at_no)
atom.binding_energy(at_no)
