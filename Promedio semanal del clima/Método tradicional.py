# Programa para calcular el promedio semanal del clima usando programación tradicional

def ingresar_temperaturas():
    """Función para ingresar temperaturas diarias."""
    temperaturas = []
    print("Ingresa las temperaturas diarias (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    """Función principal."""
    # Ingresar datos
    temperaturas = ingresar_temperaturas()
    
    # Calcular promedio
    promedio = calcular_promedio(temperaturas)
    
    # Mostrar resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
