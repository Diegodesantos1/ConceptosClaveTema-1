<h1 align="center">Conceptos Clave Tema 1</h1>


En este [repositorio](https://github.com/Diegodesantos1/ConceptosClaveTema-1) queda resuelto la prueba de Conceptos Clave Tema 1

***

El código empleado para resolverlo es el siguiente:
```python
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
        plt.title('Eje de Coordenadas', loc = "center", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'}) ; plt.xlabel("Eje x") ; plt.ylabel("Eje y") ; plt.grid() #Pone cuadrículas al gráfico
        plt.axhline(y = 0, color = 'black', linestyle = '-') ; plt.axvline(x = 0, color = 'black', linestyle = '-') ; plt.savefig("Images/puntos.jpeg"); plt.show()
```

EL código del lanzador es:
```python
from examen import Punto
from examen import Rectangulo
import matplotlib as plt

def iniciador():
    print("Bienvenido al simulador de la geometría plana, introduce las coordenadas")
    x1 = int(input("Coordenada x del punto 1: ")) ; y1 = int(input("Coordenada y del punto 1: "))
    x2 = int(input("Coordenada x del punto 2: ")) ; y2 = int(input("Coordenada y del punto 2: "))
    x3 = int(input("Coordenada x del punto 3: ")) ; y3 = int(input("Coordenada y del punto 3: "))
    x4 = int(input("Coordenada x del punto 4: ")) ; y4 = int(input("Coordenada y del punto 4: "))
    A = Punto(x1, y1) ; B = Punto(x2, y2) ; C = Punto(x3, y3) ; D = Punto(x4, y4)
    print("El punto A es " + A.string()) ; print("El punto B es " + B.string()) ; print("El punto C es " + C.string()); print("El punto D es " + D.string())
    print("El punto A está en el " + A.cuadrante()) ; print("El punto B está en el " + B.cuadrante()) ; print("El punto C está en el " + C.cuadrante()) ; print("El punto D está en el " + D.cuadrante())
    print("El vector AB es "+A.vector(B).string()) ; print("El vector BA es " + B.vector(A).string())
    print(f"La distancia entre A y B es {A.distancia(B)} unidades") ; print(f"La distancia entre B y A es {B.distancia(A)} unidades")
    if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
        print("El punto A se encuentra más lejos del origen")
    elif B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
        print("El punto B se encuentra más lejos del origen")
    else:
        print("El punto C se encuentra más lejos del origen")
    rectangulo = Rectangulo(A, B)
    print(f"La altura del rectángulo es {rectangulo.altura()}") ; print(f"La base del rectángulo es {rectangulo.base()}") ; print(f"El área del rectángulo es {rectangulo.area()} unidades cuadradas")
```

![image](https://user-images.githubusercontent.com/91721855/191558526-0e7d9a91-18cb-4e63-8abb-06de420bd5de.png)

