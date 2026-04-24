class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)

    #c Buscar libro por nombre
    def buscarLibro(self, nombre):
        for l in self.libros:
            if l.nombre == nombre:
                print(f"Libro encontrado: {l.nombre}, {l.autor}, {l.anio}")
                return
        print("Libro no encontrado")

    def cantidadLibros(self):
        return len(self.libros)


#b Instanciar 2 bibliotecas y agregar libros
b1 = Biblioteca("Central")
b2 = Biblioteca("Zona Sur")

b1.agregarLibro(Libro("Python", "Juan", 2020))
b1.agregarLibro(Libro("Java", "Luis", 2018))

b2.agregarLibro(Libro("C++", "Ana", 2015))
b2.agregarLibro(Libro("JS", "Pedro", 2021))
b2.agregarLibro(Libro("SQL", "Maria", 2019))

b1.buscarLibro("Python")

#d Mostrar biblioteca con más libros
if b1.cantidadLibros() > b2.cantidadLibros():
    print("Mayor:", b1.nombre)
elif b2.cantidadLibros() > b1.cantidadLibros():
    print("Mayor:", b2.nombre)
else:
    print("Ambas tienen la misma cantidad")