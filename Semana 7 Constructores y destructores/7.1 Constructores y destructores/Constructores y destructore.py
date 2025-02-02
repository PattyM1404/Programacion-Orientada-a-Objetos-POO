class ArchivoTemporal:
    def __init__(self, nombre, contenido):
        """
        Constructor: Inicializa un archivo temporal con un nombre y contenido.
        """
        self.nombre = nombre
        self.contenido = contenido
        print(f"Creando archivo: {self.nombre}")
        self.crear_archivo()

    def crear_archivo(self):
        """
        Método que crea un archivo temporal y escribe contenido en él.
        """
        with open(self.nombre, 'w') as archivo:
            archivo.write(self.contenido)
        print(f"Archivo {self.nombre} creado con éxito.")

    def __del__(self):
        """
        Destructor: Elimina el archivo temporal al destruir la instancia.
        """
        import os
        if os.path.exists(self.nombre):
            os.remove(self.nombre)
            print(f"Archivo {self.nombre} eliminado.")
        else:
            print(f"El archivo {self.nombre} ya no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    archivo = ArchivoTemporal("temporal.txt", "Este es un archivo temporal.")
    print("Trabajando con el archivo...")
    # Una vez que el objeto "archivo" salga del alcance, se activará el destructor.