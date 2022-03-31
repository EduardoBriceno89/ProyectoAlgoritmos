class DistanciaCuadrado:

    def __init__(self, lado):
        self.lado = lado
    
    def distanciaCuadrado(self):
        return self.lado * 4

class DistanciaRectangulo:

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    
    def distanciaRectangulo(self):
        return (self.altura + self.base) * 2

class DistanciaTriangulo:

    def __init__(self, lado):
        self.lado = lado
    
    def distanciaTriangulo(self):
        return self.lado * 3

class DistanciaCirculo:

    def __init__(self, pi, d):
        self.pi = pi
        self.d = d
    
    def distanciaCirculo(self):
        self.pi = 3.1416
        return 2* self.pi * self.d
