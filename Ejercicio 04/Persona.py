class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        return f"Nombre: {self.nombre}, CI: {self.carnet}, Edad: {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        return super().mostrar() + f", Matricula: {self.matricula}, Carrera: {self.carrera}"

class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        return super().mostrar() + f", Antiguedad: {self.antiguedad}, Sueldo: {self.sueldo}"

if __name__ == "__main__":

    #Instanciar
    e1 = Estudiante("Ana", 123, 20, 1001, "Sistemas")
    e2 = Estudiante("Luis", 456, 25, 1002, "Industrial")

    d1 = Docente("Carlos", 789, 25, 10, 5000)

    # Mostrar
    print(e1.mostrar())
    print(e2.mostrar())
    print(d1.mostrar())

    #Verificar misma edad
    if e1.edad == d1.edad:
        print("El estudiante con la misma edad es:", e1.nombre)

    elif e2.edad == d1.edad:
        print("El estudiante con la misma edad es:", e2.nombre)

    #Verificar misma carrera
    if e1.carrera == e2.carrera:
        print("Están en la misma carrera")
    else:
        print("No estan en la misma carrera")
