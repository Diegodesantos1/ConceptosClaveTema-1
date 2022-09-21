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
            return "primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "cuarto cuadrante"
        else:
            return "origen"
    def vector(self, punto):
        return Punto(punto.x - self.x, punto.y - self.y)
    def distancia(self, punto):
        return ((punto.x - self.x)**2 + (punto.y - self.y)**2)**0.5
class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    def base(self):
        return abs(self.punto1.x - self.punto2.x)
    def altura(self):
        return abs(self.punto1.y - self.punto2.y)
    def area(self):
        return self.base() * self.altura()

A = Punto(2, 3) ; B = Punto(5, 5) ; C = Punto(-3, -1) ; D = Punto(0, 0)
print(A.string()) ; print(B.string()) ; print(C.string()); print(D.string())
print(A.cuadrante()) ; print(B.cuadrante()) ; print(C.cuadrante()) ; print(D.cuadrante())
print(A.vector(B).string()) ; print(B.vector(A).string())
print(A.distancia(B)) ; print(B.distancia(A))
if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
    print("A")
elif B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
    print("B")
else:
    print("C")

