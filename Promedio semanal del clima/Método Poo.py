# Programa para calcular el promedio semanal del clima usando programación orientada a objetos

class ClimaSemanal:
    """Clase para manejar la información diaria del clima."""
    
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar temperaturas diarias."""
        print("Ingresa las temperaturas diarias (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    """Función principal."""
    # Crear objeto de la clase
    clima = ClimaSemanal()
    
    # Ingresar datos
    clima.ingresar_temperaturas()
    
    # Calcular promedio
    promedio = clima.calcular_promedio()
    
    # Mostrar resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
