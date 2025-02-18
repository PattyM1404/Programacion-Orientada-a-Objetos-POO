import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Inicializa el inventario cargando los datos desde un archivo.
        Si el archivo no existe, se crea un inventario vacío.
        """
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los datos del inventario desde un archivo JSON.
        Maneja errores en caso de que el archivo no exista o esté corrupto.
        """
        if not os.path.exists(self.archivo):
            return {}
        try:
            with open(self.archivo, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al leer el archivo de inventario. Se inicializará un inventario vacío.")
            return {}
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo de inventario.")
            return {}

    def guardar_inventario(self):
        """
        Guarda los datos del inventario en un archivo JSON.
        Maneja errores en caso de que no haya permisos de escritura.
        """
        try:
            with open(self.archivo, "w") as file:
                json.dump(self.productos, file, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, nombre, cantidad, precio):
        """
        Agrega un nuevo producto al inventario.
        Si el producto ya existe, muestra un mensaje de advertencia.
        """
        if nombre in self.productos:
            print("El producto ya existe. Use la opción de actualizar.")
        else:
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
            self.guardar_inventario()
            print(f"Producto {nombre} agregado exitosamente.")

    def actualizar_producto(self, nombre, cantidad, precio):
        """
        Actualiza la cantidad y el precio de un producto existente.
        Si el producto no existe, muestra un mensaje de error.
        """
        if nombre in self.productos:
            self.productos[nombre]["cantidad"] = cantidad
            self.productos[nombre]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto {nombre} actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario.
        Si el producto no existe, muestra un mensaje de error.
        """
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto {nombre} eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        Si el inventario está vacío, muestra un mensaje.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for nombre, detalles in self.productos.items():
                print(f"- {nombre}: {detalles['cantidad']} unidades, ${detalles['precio']} cada una")

# Menú interactivo
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
