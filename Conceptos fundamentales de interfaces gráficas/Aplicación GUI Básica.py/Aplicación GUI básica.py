import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()  # Obtener el texto ingresado
    if dato:
        lista_datos.insert(tk.END, dato)  # Insertar el dato en la lista
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")  # Mostrar advertencia si el campo está vacío

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Definir el tamaño de la ventana

# Crear componentes GUI
label_titulo = tk.Label(ventana, text="Ingrese un dato:")  # Etiqueta descriptiva
label_titulo.pack(pady=5)  # Agregar la etiqueta con espaciado

entrada_texto = tk.Entry(ventana, width=40)  # Campo de entrada de texto
entrada_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)  # Botón para agregar datos
boton_agregar.pack(pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10)  # Lista para mostrar datos
lista_datos.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)  # Botón para limpiar la lista
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()  # Iniciar el bucle de eventos de Tkinter

