class Areas:
    def __init__(self, base, altura, diagonalmay, diagonalmen):
        self.base = base
        self.altura = altura
        self.diagonalmay = diagonalmay
        self.diagonalmen = diagonalmen
    
    def areaTriangulo(self):
        return (self.base * self.altura)/2
    
    def areaRectangulo(self):
        return self.base * self.altura

    def areaRombo(self):
        return (self.diagonalmay * self.diagonalmen)
