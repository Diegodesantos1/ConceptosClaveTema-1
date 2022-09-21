class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def string(self):
        return "({0},{1})".format(self.x, self.y)
    def crear_punto(self):
        return Punto(self.x, self.y)
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0
    def vector(self, punto):
        return Punto(punto.x - self.x, punto.y - self.y)
    def distancia(self, punto):
        return ((punto.x - self.x)**2 + (punto.y - self.y)**2)**0.5
class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
