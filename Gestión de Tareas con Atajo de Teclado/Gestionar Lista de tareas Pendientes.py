import tkinter as tk
from tkinter import messagebox  # Para mostrar mensajes de alerta

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")  # Tamaño de la ventana

# Lista para almacenar las tareas
# Cada tarea será un diccionario con:
# - texto: descripción de la tarea
# - completada: True o False
tareas = []

# Función que actualiza visualmente la lista de tareas
def actualizar_lista():
    lista_tareas.delete(0, tk.END)  # Borra la lista actual
    for tarea in tareas:
        if tarea["completada"]:
            # Mostrar en verde y con check si está completada
            lista_tareas.insert(tk.END, tarea["texto"] + " ✓")
            lista_tareas.itemconfig(tk.END, {'fg': 'green'})
        else:
            # Mostrar en negro si está pendiente
            lista_tareas.insert(tk.END, tarea["texto"])
            lista_tareas.itemconfig(tk.END, {'fg': 'black'})

# Añade una tarea a la lista
def añadir_tarea(event=None):
    tarea = entrada.get().strip()  # Obtener texto y eliminar espacios
    if tarea == "":
        # Mostrar advertencia si no escribieron nada
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")
    else:
        # Añadir tarea nueva
        tareas.append({"texto": tarea, "completada": False})
        entrada.delete(0, tk.END)  # Limpiar caja de texto
        actualizar_lista()  # Actualizar visualmente la lista

# Marca una tarea como completada
def completar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]  # Obtener tarea seleccionada
        if not tareas[seleccion]["completada"]:
            tareas[seleccion]["completada"] = True  # Marcar como completada
            actualizar_lista()
        else:
            messagebox.showinfo("Info", "La tarea ya está completada.")
    except IndexError:
        messagebox.showinfo("Info", "Seleccione una tarea para completar.")

# Elimina una tarea de la lista
def eliminar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]  # Obtener tarea seleccionada
        tareas.pop(seleccion)  # Eliminar tarea
        actualizar_lista()
    except IndexError:
        messagebox.showinfo("Info", "Seleccione una tarea para eliminar.")

# Cierra la aplicación
def salir(event=None):
    ventana.destroy()

# ---- INTERFAZ GRÁFICA ----

# Etiqueta para indicar al usuario
tk.Label(ventana, text="Ingrese su tarea:").pack(pady=10)

# Caja de texto donde el usuario escribe la tarea
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)
entrada.bind("<Return>", añadir_tarea)  # Permite presionar Enter para añadir tarea

# Lista donde se muestran las tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Botonera
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Botón para añadir tarea
tk.Button(frame_botones, text="Añadir", command=añadir_tarea).pack(side=tk.LEFT, padx=5)

# Botón para completar tarea
tk.Button(frame_botones, text="Completar", command=completar_tarea).pack(side=tk.LEFT, padx=5)

# Botón para eliminar tarea
tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea).pack(side=tk.LEFT, padx=5)

# ---- ATAJOS DE TECLADO ----
ventana.bind("<c>", completar_tarea)    # C para completar
ventana.bind("<d>", eliminar_tarea)     # D para eliminar
ventana.bind("<Delete>", eliminar_tarea) # Suprimir para eliminar
ventana.bind("<Escape>", salir)         # Escape para salir

# Ejecutar ventana principal
ventana.mainloop()
