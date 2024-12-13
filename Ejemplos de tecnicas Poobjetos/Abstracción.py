from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# Clase derivada 1
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

# Clase derivada 2
class Pato(Animal):
    def hacer_sonido(self):
        return "cuac cuac"

# Clase derivada 3
class Gato(Animal):
    def hacer_sonido(self):
        return "miau miau"

# Uso de la abstracción
def imprimir_sonidos(animal):
    print(animal.hacer_sonido())

perro = Perro()
pato = Pato()
gato = Gato()

imprimir_sonidos(perro)  # Salida: Guau guau
imprimir_sonidos(pato)   # Salida: cuac cuac
imprimir_sonidos(gato)   # Salida: miau miau
