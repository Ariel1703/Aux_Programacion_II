class Bus:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.precio_pasaje = 1.50

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
        else:
            print("No hay suficientes asientos")

    def cobrar_pasaje(self):
        total = self.pasajeros * self.precio_pasaje
        return total

    def asientos_disponibles(self):
        return self.capacidad - self.pasajeros

bus1 = Bus(30)

bus1.subir_pasajeros(10)

print("Pasajeros:", bus1.pasajeros)
print("Total cobrado:", bus1.cobrar_pasaje())
print("Asientos disponibles:", bus1.asientos_disponibles())