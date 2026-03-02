class Anime:

    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []

    def agregarEpisodio(self, episodio):
        self.__episodios.append(episodio)

    def __str__(self):
        return f"Anime: {self.nombre}, Genero: {self.genero}, Episodios: {self.__nroEpisodios}"
    
class Televisor:

    def __init__(self, marca="", resolucion=0, tipo=""):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"Televisor: {self.__marca}, Resolucion: {self.__resolucion}, Tipo: {self.__tipo}"

class Instrumento:

    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo

    def getMaterial(self):
        return self.__material

    def getTipo(self):
        return self.__tipo

    def setMaterial(self, material):
        self.__material = material

    def setTipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre}, Material: {self.__material}, Tipo: {self.__tipo}"

if __name__ == "__main__":

    anime1 = Anime("Naruto", "Accion", 220)
    anime2 = Anime("One Piece", "Aventura", 1000)

    tv1 = Televisor("Samsung", 55, "OLED")
    tv2 = Televisor("LG", 50, "IPS")

    inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
    inst2 = Instrumento("Flauta", "Metal", "Aire")

    print(anime1)
    print(anime2)
    print(tv1)
    print(tv2)
    print(inst1)
    print(inst2)