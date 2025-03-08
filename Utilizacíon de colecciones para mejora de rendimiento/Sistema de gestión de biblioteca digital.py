class Libro:
    # Representa un libro con título, autor, categoría e ISBN
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __repr__(self):
        return f"{self.titulo} - {self.autor} ({self.categoria}, ISBN: {self.isbn})"

class Usuario:
    # Representa un usuario de la biblioteca con un nombre y un ID único
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para almacenar los libros prestados por el usuario
    
    def __repr__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

class Biblioteca:
    # Gestiona los libros, usuarios y préstamos en la biblioteca
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
    
    def agregar_libro(self, libro):
        # Agrega un libro al diccionario de libros disponibles
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")
    
    def eliminar_libro(self, isbn):
        # Elimina un libro de la biblioteca si está registrado
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")
    
    def registrar_usuario(self, usuario):
        # Registra un usuario en la biblioteca
        self.usuarios[usuario.user_id] = usuario
        print(f"Usuario registrado: {usuario}")
    
    def dar_baja_usuario(self, user_id):
        # Elimina un usuario de la biblioteca si está registrado
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("Usuario no encontrado.")
    
    def prestar_libro(self, user_id, isbn):
        # Permite prestar un libro a un usuario si ambos existen en la biblioteca
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # Remueve el libro de la biblioteca
            usuario.libros_prestados.append(libro)  # Lo añade a la lista de préstamos del usuario
            print(f"Libro {libro.titulo} prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")
    
    def devolver_libro(self, user_id, isbn):
        # Permite devolver un libro prestado a la biblioteca
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)  # Lo elimina de la lista de préstamos
                    self.libros[isbn] = libro  # Lo devuelve a la biblioteca
                    print(f"Libro {libro.titulo} devuelto por {usuario.nombre}.")
                    return
            print("Libro no encontrado en los préstamos del usuario.")
        else:
            print("Usuario no encontrado.")
    
    def buscar_libro(self, criterio):
        # Busca libros en la biblioteca según título, autor o categoría
        resultados = [libro for libro in self.libros.values() 
                      if criterio.lower() in libro.titulo.lower() 
                      or criterio.lower() in libro.autor.lower() 
                      or criterio.lower() in libro.categoria.lower()]
        return resultados if resultados else "No se encontraron libros."
    
    def listar_libros_prestados(self, user_id):
        # Lista los libros que un usuario tiene actualmente prestados
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            return usuario.libros_prestados if usuario.libros_prestados else "No tiene libros prestados."
        else:
            return "Usuario no encontrado."

# Ejemplo de uso
biblioteca = Biblioteca()

# Creación de libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "123456")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "789101")

# Creación de usuario
usuario1 = Usuario("Patricia Matute", 1)

# Registro de libros y usuario en la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

# Préstamo de un libro al usuario
biblioteca.prestar_libro(1, "123456")
print(biblioteca.listar_libros_prestados(1))

# Devolución del libro a la biblioteca
biblioteca.devolver_libro(1, "123456")
print(biblioteca.listar_libros_prestados(1))
