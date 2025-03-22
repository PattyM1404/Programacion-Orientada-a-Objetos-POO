import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x500")
        
        # Frame para la selección de fecha
        self.frame_calendario = tk.Frame(root)
        self.frame_calendario.pack(pady=10)
        
        # Widget de calendario para selección de fecha
        self.calendario = Calendar(self.frame_calendario, selectmode='day', year=2025, month=3, day=22)
        self.calendario.pack()
        
        # Frame para entrada de datos
        self.frame_datos = tk.Frame(root)
        self.frame_datos.pack(pady=10)
        
        # Campo para la descripción del evento
        tk.Label(self.frame_datos, text="Descripción:").grid(row=0, column=0)
        self.descripcion = tk.Entry(self.frame_datos, width=30)
        self.descripcion.grid(row=0, column=1)
        
        # Botón para agregar evento
        self.btn_agregar = tk.Button(root, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(pady=5)
        
        # Frame para lista de eventos
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack()
        
        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()
        
        # Botón para eliminar evento seleccionado
        self.btn_eliminar = tk.Button(root, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.pack(pady=5)
        
    def agregar_evento(self):
        """Función para agregar un evento a la lista."""
        fecha = self.calendario.get_date()
        descripcion = self.descripcion.get()
        if descripcion:
            self.tree.insert("", "end", values=(fecha, descripcion))
            self.descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese una descripción para el evento.")
        
    def eliminar_evento(self):
        """Función para eliminar el evento seleccionado."""
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
