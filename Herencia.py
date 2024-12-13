class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Este animal hace un sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} el perro dice Guau"

Firulais = Perro("Firulais")
