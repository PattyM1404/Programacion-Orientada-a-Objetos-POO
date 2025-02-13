class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio por unidad del producto
    
    def __str__(self):
        # Representación en cadena del producto
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    # Clase que representa el inventario de la tienda
    def __init__(self):
        self.productos = []  # Lista que almacenará los productos
    
    def añadir_producto(self, producto):
        # Método para añadir un producto al inventario
        # Verifica que el ID del producto sea único antes de agregarlo
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")
    
    def eliminar_producto(self, id_producto):
        # Método para eliminar un producto del inventario por su ID
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía.")
    
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Método para actualizar la cantidad o el precio de un producto
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad  # Actualiza la cantidad si se proporciona
                if precio is not None:
                    p.precio = precio  # Actualiza el precio si se proporciona
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")
    
    def buscar_producto(self, nombre):
        # Método para buscar productos por nombre (pueden haber nombres similares)
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados
    
    def mostrar_inventario(self):
        # Método para mostrar todos los productos en el inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


def menu():
    # Función que maneja el menú interactivo en la consola
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Opción para añadir un nuevo producto
            id_producto = input("Ingrese ID único del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))
        
        elif opcion == "2":
            # Opción para eliminar un producto por su ID
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        
        elif opcion == "3":
            # Opción para actualizar cantidad o precio de un producto
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        
        elif opcion == "4":
            # Opción para buscar un producto por su nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron productos.")
        
        elif opcion == "5":
            # Opción para mostrar todos los productos del inventario
            inventario.mostrar_inventario()
        
        elif opcion == "6":
            # Opción para salir del programa
            print("Saliendo del programa...")
            break
        else:
            # Mensaje de error si la opción no es válida
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    # Punto de entrada del programa
    menu()
