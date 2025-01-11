# Clase para representar a un estudiante
class Student:
    def __init__(self, name, grade):
        """
        Inicializa un estudiante con su nombre y calificación.
        :param name: Nombre del estudiante.
        :param grade: Calificación del estudiante.
        """
        self.name = name
        self.grade = grade

    def display(self):
        """Muestra los datos del estudiante."""
        print(f"Nombre: {self.name}, Calificación: {self.grade}")


# Crear objetos de estudiantes
student1 = Student("Ana", 90)
student2 = Student("Carlos", 85)

# Mostrar los datos de los estudiantes
student1.display()
student2.display()
