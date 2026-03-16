class Videojuego:

    def __init__(self, nombre="", plataforma="", jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores

    # Sobrecarga del método
    def agregarJugadores(self, cantidad=None):

        if cantidad is None:
            self.jugadores += 1
        else:
            self.jugadores += cantidad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Jugadores:", self.jugadores)
        print("-------------------")


v1 = Videojuego("FIFA", "PlayStation", 2)
v2 = Videojuego("Minecraft", "PC")

v1.agregarJugadores()
v2.agregarJugadores(3)

v1.mostrar()
v2.mostrar()