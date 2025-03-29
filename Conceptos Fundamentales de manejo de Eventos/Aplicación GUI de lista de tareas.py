import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    """Agrega una nueva tarea a la lista si la entrada no está vacía."""
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Agregar tarea al Listbox
        entrada_tarea.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada():
    """Marca la tarea seleccionada como completada cambiando su estilo."""
    try:
        indice = lista_tareas.curselection()[0]  # Obtener índice de la tarea seleccionada
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"✔ {tarea}")  # Agregar marca de completado
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

def agregar_con_enter(event):
    """Permite agregar una tarea presionando Enter."""
    agregar_tarea()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_con_enter)  # Asociar tecla Enter a la función

# Botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
