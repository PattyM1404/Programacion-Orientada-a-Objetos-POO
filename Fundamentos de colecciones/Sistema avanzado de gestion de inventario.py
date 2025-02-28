import pickle

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto
    
    def to_dict(self):
        # Convierte el producto a un diccionario para facilitar su manejo
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

# Clase que gestiona el inventario de productos
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos por su ID
    
    def agregar_producto(self, producto):
        # Agrega un nuevo producto al inventario
        self.productos[producto.id_producto] = producto
    
    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario por su ID
        if id_producto in self.productos:
            del self.productos[id_producto]
    
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto en el inventario
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
    
    def buscar_producto(self, nombre):
        # Busca productos por nombre y devuelve una lista de coincidencias
        return [p.to_dict() for p in self.productos.values() if p.nombre == nombre]
    
    def mostrar_productos(self):
        # Devuelve una lista con todos los productos en el inventario
        return [p.to_dict() for p in self.productos.values()]
    
    def guardar_en_archivo(self, archivo):
        # Guarda el inventario en un archivo utilizando serialización con Pickle
        with open(archivo, "wb") as f:
            pickle.dump(self.productos, f)
    
    def cargar_desde_archivo(self, archivo):
        # Carga el inventario desde un archivo serializado
        try:
            with open(archivo, "rb") as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            self.productos = {}  # Si el archivo no existe, inicializa un inventario vacío

# Función que proporciona un menú interactivo para gestionar el inventario
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.dat")  # Carga datos al iniciar
    
    while True:
        print("\nMenú de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Solicita datos y añade un producto nuevo
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            # Solicita el ID y elimina un producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            # Permite actualizar cantidad o precio de un producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no cambia): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            # Busca productos por nombre
            nombre = input("Nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            # Muestra todos los productos en el inventario
            print(inventario.mostrar_productos())
        elif opcion == "6":
            # Guarda el inventario y sale del programa
            inventario.guardar_en_archivo("inventario.dat")
            break
        else:
            print("Opción no válida.")

# Ejecuta el programa si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
