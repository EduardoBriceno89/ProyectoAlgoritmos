class AreaTriangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def areaTriangulo(self):
        return (self.base * self.altura)/2

class AreaRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def areaRectangulo(self):
        return self.base * self.altura

class AreaRombo:

    def __init__(self, diagonalmay, diagonalmen):
        self.diagonalmay = diagonalmay
        self.diagonalmen = diagonalmen

    def areaRombo(self):
        return (self.diagonalmay * self.diagonalmen)/2

class AreaCuadrado:

    def __init__(self, lado1, lado2) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
    
    def areaCuadrado(self):
        return self.lado1 * self.lado2
