import matplotlib.pyplot as plt


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
print("El punto A es " + A.string()) ; print("El punto B es " + B.string()) ; print("El punto C es " + C.string()); print("El punto D es " + D.string())
print("El punto A está en el " + A.cuadrante()) ; print("El punto B está en el " + B.cuadrante()) ; print("El punto C está en el " + C.cuadrante()) ; print("El punto D está en el " + D.cuadrante())
print("El vector AB es "+A.vector(B).string()) ; print("El vector BA es " + B.vector(A).string())
print(f"La distancia entre A y B es {A.distancia(B)}") ; print(f"La distancia entre B y A es {B.distancia(A)}")
if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
    print("El punto A se encuentra más lejos del origen")
elif B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
    print("El punto B se encuentra más lejos del origen")
else:
    print("El punto C se encuentra más lejos del origen")
rectangulo = Rectangulo(A, B)
print(f"La altura del rectángulo es {rectangulo.altura()}") ; print(f"La base del rectángulo es {rectangulo.base()}") ; print(f"El área del rectángulo es {rectangulo.area()}")

class Graficos:
    def grafico():
        x = [A.x, B.x, C.x, D.x] ; y = [A.y, B.y, C.y, D.y] # Lista de coordenadas
        plt.plot(x, y, "ro") ; plt.axis([-10, 10, -10, 10])
        plt.title("Puntos") ; plt.xlabel("Eje x") ; plt.ylabel("Eje y") ; plt.grid() #Pone cuadrículas al gráfico
        plt.show()
Graficos.grafico()