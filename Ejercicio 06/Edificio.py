class Mueble:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

class Habitacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.muebles = []  # composicion

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)

    def cantidad_muebles(self):
        return len(self.muebles)

class Departamento:
    def __init__(self, nroPuerta, nroPiso):
        self.nroPuerta = nroPuerta
        self.nroPiso = nroPiso
        self.habitaciones = []  # composicion

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def cantidad_habitaciones(self):
        return len(self.habitaciones)

    def cantidad_muebles(self):
        total = 0
        for h in self.habitaciones:
            total += h.cantidad_muebles()
        return total

    def agregar_mueble(self, mueble):
        # agrega a la primera habitacion (simplificacion)
        if self.habitaciones:
            self.habitaciones[0].agregar_mueble(mueble)

class Parqueo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.autos = []

    def agregar_auto(self, auto):
        if len(self.autos) < self.capacidad:
            self.autos.append(auto)
            print("Auto agregado correctamente")
        else:
            print("No hay capacidad disponible")

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []
        self.parqueo = None  # agregacion

    def agregar_departamento(self, dep):
        self.departamentos.append(dep)

    def agregar_parqueo(self, parqueo):
        self.parqueo = parqueo

    # b. departamento con mas habitaciones en piso X
    def dep_mas_habitaciones(self, piso):
        candidatos = [d for d in self.departamentos if d.nroPiso == piso]
        if not candidatos:
            return None
        return max(candidatos, key=lambda d: d.cantidad_habitaciones())

    # d. departamento con mas muebles
    def dep_mas_muebles(self):
        if not self.departamentos:
            return None
        return max(self.departamentos, key=lambda d: d.cantidad_muebles())

    # e. habitacion con mas muebles en piso X
    def habitacion_mas_muebles(self, piso):
        max_hab = None
        max_muebles = -1

        for d in self.departamentos:
            if d.nroPiso == piso:
                for h in d.habitaciones:
                    if h.cantidad_muebles() > max_muebles:
                        max_muebles = h.cantidad_muebles()
                        max_hab = h
        return max_hab

    # f. eliminar departamentos con numero primo de habitaciones
    def eliminar_departamentos_primos(self):
        def es_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        self.departamentos = [
            d for d in self.departamentos
            if not es_primo(d.cantidad_habitaciones())
        ]
# main
ed = Edificio("Torres UMSA")
parq = Parqueo(2)
ed.agregar_parqueo(parq)

# Crear departamentos
d1 = Departamento(1, 1)
d2 = Departamento(2, 1)
d3 = Departamento(3, 2)

# Habitaciones
h1 = Habitacion("Sala", 20)
h2 = Habitacion("Cuarto", 15)
h3 = Habitacion("Cocina", 10)

# Agregar habitaciones
d1.agregar_habitacion(h1)
d1.agregar_habitacion(h2)

d2.agregar_habitacion(h3)

d3.agregar_habitacion(Habitacion("Suite", 30))

# Agregar muebles
m1 = Mueble("Sofa", "Cuero")
m2 = Mueble("Mesa", "Madera")

h1.agregar_mueble(m1)
h1.agregar_mueble(m2)

# Agregar departamentos al edificio
ed.agregar_departamento(d1)
ed.agregar_departamento(d2)
ed.agregar_departamento(d3)

dep = ed.dep_mas_habitaciones(1)
print("Dep con más habitaciones piso 1:", dep.nroPuerta if dep else "Ninguno")

d1.agregar_mueble(Mueble("Silla", "Plastico"))

dep = ed.dep_mas_muebles()
print("Dep con más muebles:", dep.nroPuerta)

hab = ed.habitacion_mas_muebles(1)
print("Habitación con más muebles:", hab.nombre if hab else "Ninguna")

ed.eliminar_departamentos_primos()
print("Departamentos restantes:", len(ed.departamentos))

parq.agregar_auto("Auto1")
parq.agregar_auto("Auto2")
parq.agregar_auto("Auto3") 