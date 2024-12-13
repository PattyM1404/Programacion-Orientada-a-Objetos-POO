class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Método público para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Método público para establecer un nuevo nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método público para obtener la edad
    def get_edad(self):
        return self.__edad

    # Método público para establecer una nueva edad
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:  # Validación simple
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

# Uso de la clase Persona
persona = Persona("Jean", 30)

# Accediendo a los datos a través de métodos públicos
print(persona.get_nombre())  # Salida: Jean
print(persona.get_edad())    # Salida: 30

# Modificando los datos utilizando métodos públicos
persona.set_nombre("Paul")
persona.set_edad(35)

print(persona.get_nombre())  # Salida: Paul
print(persona.get_edad())    # Salida: 35

# Intentando asignar una edad inválida
persona.set_edad(-5)         # Salida: La edad debe ser un número positivo.
