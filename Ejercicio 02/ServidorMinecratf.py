class ServidorMinecraft:

    def __init__(self):
        self.jugadores = {}

    def agregar_jugador(self, nombre, diamantes):
        if len(self.jugadores) < 10:
            self.jugadores[nombre] = diamantes
        else:
            print("Servidor lleno")

    def stacks_diamantes(self):
        for jugador, diamantes in self.jugadores.items():
            stacks = diamantes // 64
            print(jugador, "tiene", stacks, "stack(s)")

    def jugador_mas_diamantes(self):
        jugador = max(self.jugadores, key=self.jugadores.get)
        print("Jugador con más diamantes:", jugador)

    def total_diamantes(self):
        total = sum(self.jugadores.values())
        print("Total de diamantes:", total)

server = ServidorMinecraft()

server.agregar_jugador("Pedro", 120)
server.agregar_jugador("Maria", 70)
server.agregar_jugador("Vegetita", 200)

server.stacks_diamantes()
server.jugador_mas_diamantes()
server.total_diamantes()