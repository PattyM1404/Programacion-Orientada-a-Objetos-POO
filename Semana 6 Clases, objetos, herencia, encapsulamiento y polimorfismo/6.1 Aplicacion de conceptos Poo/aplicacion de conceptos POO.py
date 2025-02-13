# Ejemplo de Programación Orientada a Objetos (POO) en Python

# Clase base que representa un empleado
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre  # Atributo público
        self._salario_base = salario_base  # Atributo protegido para demostrar encapsulación

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario Base: {self._salario_base}"

    def calcular_salario(self):
        # Método base que puede ser sobrescrito por clases derivadas
        return self._salario_base


# Clase derivada que representa un gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono  # Atributo adicional para la clase derivada

    # Sobrescritura del método calcular_salario para incluir el bono
    def calcular_salario(self):
        return self._salario_base + self.bono


# Clase derivada que representa un vendedor
class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comision):
        super().__init__(nombre, salario_base)
        self.comision = comision

    # Sobrescritura del método calcular_salario para incluir la comisión
    def calcular_salario(self):
        return self._salario_base + self.comision


# Función que demuestra polimorfismo
# Acepta cualquier objeto que sea una instancia de Empleado o sus derivadas
def mostrar_salario_empleado(empleado):
    print(empleado.mostrar_informacion())
    print(f"Salario Total: {empleado.calcular_salario()}\n")


# Crear instancias de las clases
empleado1 = Empleado("Ana", 3000)
gerente1 = Gerente("Carlos", 5000, 2000)
vendedor1 = Vendedor("Laura", 2500, 1500)

# Uso del polimorfismo para mostrar la información de los empleados
empleados = [empleado1, gerente1, vendedor1]
for empleado in empleados:
    mostrar_salario_empleado(empleado)