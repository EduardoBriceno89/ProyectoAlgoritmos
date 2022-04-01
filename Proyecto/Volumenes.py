class VolumenCuadrado:

    def __init__(self,lado):
        self.lado = lado

    def Volumencuadrado (self):
        return self.lado * 3

class VolumenRectangulo:

     def __init__(self,largo,ancho,altura):
         self.largo = largo
         self.ancho = ancho
         self.altura = altura

     def Volumenrectangulo (self):
         return self.largo * self.ancho * self.altura

class VolumenTriangulo:

    def __init__(self, altura, base, largo):
        self.altura = altura
        self.base = base
        self.largo = largo

    def Volumentriangulo (self):
         return ((self.altura * self.base) * 2)/2

class VolumenCirculo:

    def __init__(self, pi, r):
        self.pi = pi
        self.r = r

    def Volumencirculo (self):
        self.pi = 3.1416
        return 4/3 * self.pi * pow(self.r,3)