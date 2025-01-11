# Programa: Cálculo de áreas
# Función: Calcula el área de un triángulo o un rectángulo según la opción seleccionada.

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float).
    :param altura: Altura del triángulo (float).
    :return: Área del triángulo (float).
    """
    return 0.5 * base * altura

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo dado su largo y ancho.
    :param largo: Largo del rectángulo (float).
    :param ancho: Ancho del rectángulo (float).
    :return: Área del rectángulo (float).
    """
    return largo * ancho

# Menú principal para el usuario
print("Seleccione la figura para calcular el área:")
print("1. Triángulo")
print("2. Rectángulo")
opcion_seleccionada = int(input("Ingrese 1 o 2: "))

# Condicional para calcular según la figura seleccionada
if opcion_seleccionada == 1:
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print(f"El área del triángulo es: {area_triangulo:.2f}")
elif opcion_seleccionada == 2:
    largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)
    print(f"El área del rectángulo es: {area_rectangulo:.2f}")
else:
    print("Opción no válida. Intente de nuevo.")
