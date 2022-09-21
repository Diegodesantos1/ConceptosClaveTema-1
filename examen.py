class Punto:
    def __init__(self, x, y, coordenadax, coordenaday):
        self.x = x
        self.y = y
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday
    def crear_punto():
        coordenadax = int(input("Introduce la coordenada x: "))
        coordenaday = int(input("Introduce la coordenada y: "))
        if coordenadax != int:
            coordenadax = 0
        elif coordenaday != int:
            coordenaday = 0
        punto=(coordenadax, coordenaday)
        print(punto)
    

Punto.crear_punto()