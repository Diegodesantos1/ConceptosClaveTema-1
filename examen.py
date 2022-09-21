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
class Graficos:
    def grafico():
        x = [A.x, B.x, C.x, D.x] ; y = [A.y, B.y, C.y, D.y] # Lista de coordenadas
        plt.plot(x, y, "ro") ; plt.axis([-10, 10, -10, 10])
        plt.title("Puntos") ; plt.xlabel("Eje x") ; plt.ylabel("Eje y") ; plt.grid() #Pone cuadrículas al gráfico
        plt.savefig("Images/puntos.jpeg"); plt.show() 
Graficos.grafico()