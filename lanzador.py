from examen import Punto
from examen import Rectangulo

def iniciador():
    print("Bienvenido al simulador de la geometría plana")
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
