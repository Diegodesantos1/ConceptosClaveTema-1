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

