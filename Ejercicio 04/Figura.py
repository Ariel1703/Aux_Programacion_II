from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtenerArea(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado -> Lado: {self.lado}, Color: {self.color}, Area: {self.obtenerArea()}"

class Triangulo(Figura):
    def __init__(self, l1, l2, l3, color):
        super().__init__(color)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def obtenerArea(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

    def __str__(self):
        return f"Triangulo -> Lados: {self.l1},{self.l2},{self.l3}, Color: {self.color}, Area: {self.obtenerArea()}"

class Redondo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self):
        return math.pi * self.radio ** 2

    def __str__(self):
        return f"Redondo -> Radio: {self.radio}, Color: {self.color}, Area: {self.obtenerArea()}"

if __name__ == "__main__":

    #Instanciar 2 de cada uno
    c1 = Cuadrado(4, "rojo")
    c2 = Cuadrado(6, "azul")

    t1 = Triangulo(3, 4, 5, "verde")
    t2 = Triangulo(5, 5, 6, "amarillo")

    r1 = Redondo(3, "negro")
    r2 = Redondo(5, "blanco")

    # Mostrar
    print(c1)
    print(c2)
    print(t1)
    print(t2)
    print(r1)
    print(r2)

    # d) Comparar
    if c1.obtenerArea() > t1.obtenerArea():
        print("Mayor area:", c1.color)
    else:
        print("Mayor area:", t1.color)
