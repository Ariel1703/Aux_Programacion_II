class Aula:

    def __init__(self, nombreAula, piso):
        self.nombreAula = nombreAula
        self.piso = piso
        self.estudiantes = []

    def agregarEstudiante(self, nombre, nota):
        self.estudiantes.append([nombre, nota])

    # i) mostrar datos
    def mostrar(self):
        print("Aula:", self.nombreAula)
        print("Piso:", self.piso)

        for e in self.estudiantes:
            print("Estudiante:", e[0], "Nota:", e[1])

    # ii) aprobado o reprobado
    def mostrarEstado(self):

        for e in self.estudiantes:

            if e[1] >= 51:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

            print(e[0], "-", estado)


a1 = Aula("Aula 101", 1)

a1.agregarEstudiante("Luis", 40)
a1.agregarEstudiante("Aracely", 89)

a1.mostrar()

print("Estado de estudiantes")
a1.mostrarEstado()