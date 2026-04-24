class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueno = nombreDueno


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueno)
        self.cazaRatones = cazaRatones
        self.tomaLeche = tomaLeche


class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregarPerro(self, perro):
        self.perros.append(perro)

    def agregarGato(self, gato):
        self.gatos.append(gato)

    #b Ordenar perros
    def ordenarPerros(self):
        self.perros.sort(key=lambda p: (p.edad, p.nombreDueno, p.nombre))

    #c Ordenar gatos
    def ordenarGatos(self):
        self.gatos.sort(key=lambda g: (
            not g.tomaLeche,   # primero los que toman leche
            -g.edad,           # edad descendente
            g.nombre
        ))

    #d Verificar dueños con 2 o mas animales
    def verificarDuenos(self):
        contador = {}
        for a in self.perros + self.gatos:
            contador[a.nombreDueno] = contador.get(a.nombreDueno, 0) + 1

        for dueno, cant in contador.items():
            if cant >= 2:
                print(f"{dueno} tiene {cant} animales")


#a INSTANCIAR 2 CENTROS con minimo 2 perros y 2 gatos
cv1 = CentroVeterinario("Vet1")
cv2 = CentroVeterinario("Vet2")

# Centro 1
cv1.agregarPerro(Perro("Firulais", 5, "Juan", True, True))
cv1.agregarPerro(Perro("Max", 3, "Juan", False, True))
cv1.agregarGato(Gato("Michi", 2, "Ana", True, True))
cv1.agregarGato(Gato("Pelusa", 4, "Ana", False, False))

# Centro 2
cv2.agregarPerro(Perro("Rocky", 2, "Luis", True, False))
cv2.agregarPerro(Perro("Toby", 6, "Carlos", False, True))
cv2.agregarGato(Gato("Nina", 1, "Luis", True, True))
cv2.agregarGato(Gato("Luna", 3, "Maria", False, True))

# Ejecutar metodos
cv1.ordenarPerros()   # (b)
cv1.ordenarGatos()    # (c)
cv1.verificarDuenos() # (d)