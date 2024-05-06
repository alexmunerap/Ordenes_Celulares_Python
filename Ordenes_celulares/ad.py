import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import psycopg2
import json

class InterfazAdmin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jefe")
        self.geometry("800x600")

        self.modelol = tk.Label(self, text="Modelo del equipo:")
        self.modelol.grid(row=0, column=0, padx=10, pady=10)
        self.modelo= tk.Entry(self)
        self.modelo.grid(row=0, column=1, padx=10, pady=10)

        self.diagnosticol = tk.Label(self, text="Diagnostico del equipo:")
        self.diagnosticol.grid(row=1, column=0, padx=10, pady=10)
        self.diagnostico = tk.Entry(self)
        self.diagnostico.grid(row=1, column=1, padx=10, pady=10)

        self.nombre_clientel = tk.Label(self, text="Nombre del cliente:")
        self.nombre_clientel.grid(row=2, column=0, padx=10, pady=10)
        self.nombre_cliente = tk.Entry(self)
        self.nombre_cliente.grid(row=2, column=1, padx=10, pady=10)

        self.cedula_clientel = tk.Label(self, text="Cedula del cliente:")
        self.cedula_clientel.grid(row=3, column=0, padx=10, pady=10)
        self.cedula_cliente = tk.Entry(self)
        self.cedula_cliente.grid(row=3, column=1, padx=10, pady=10)

        self.fechal = tk.Label(self, text="Cedula del cliente:")
        self.fechal.grid(row=4, column=0, padx=10, pady=10)
        self.fecha = tk.Entry(self)
        self.fecha.grid(row=4, column=1, padx=10, pady=10)

       
        self.crearordenboton = tk.Button(self, text="Crear Orden", command=self.crear_orden)
        self.crearordenboton.grid(row=5, column=0, columnspan=2, pady=10)

   
        self.verordenboton = tk.Button(self, text="Ver Ordenes", command=self.ver_orden)
        self.verordenboton.grid(row=6, column=0, columnspan=2, pady=10)

 
        self.eliminarordenboton = tk.Button(self, text="Eliminar Ordenes", command=self.eliminar_orden)
        self.eliminarordenboton.grid(row=7, column=0, columnspan=2, pady=10)

    def crear_orden(self):
        try:
            conn = psycopg2.connect(dbname="db-ordenes", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tareas (modelo, diagnostico, nombre, cedula, fecha) VALUES (%s, %s, %s, %s, %s)", (self.modelo.get(), self.diagnostico.get(), self.nombre_cliente.get(), self.cedula_cliente.get(), self.fecha.get()))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yeah", "Tarea creada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al crear la orden: {e}")

    def ver_orden(self):
        try:
            conn = psycopg2.connect(dbname="db-ordenes", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ordenes")
            ordenes = cursor.fetchall()
            cursor.close()
            conn.close()

            self.ordeneslista = ttk.Treeview(self, columns=("modelo", "diagnostico, nombre, cedula, fecha"), show="headings")
            self.ordeneslista.heading("modelo", text="modelo")
            self.ordeneslista.heading("diagnostico", text="diagnostico")
            self.ordeneslista.heading("nombre", text="nombre")
            self.ordeneslista.heading("cedula", text="cedula")
            self.ordeneslista.heading("fecha", text="fecha")
            self.ordeneslista.grid(row=5, column=0, columnspan=2, pady=10)

            for orden in ordenes:
                self.ordeneslista.insert("", "end", values=orden)

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al ver las ordenes: {e}")

    def eliminar_orden(self):
        try:
            
            seleccionItemes = self.ordeneslista.selection()
            if not seleccionItemes:
                messagebox.showerror("Error", "Debe seleccionar una orden para eliminar")
                return

           
            seleccionItemes = seleccionItemes[0]

            modelo = self.ordeneslista.item(seleccionItemes, "values")[0]

            conn = psycopg2.connect(dbname="db-ordenes", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ordenes WHERE modelo = %s", (modelo,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yuhuu", "orden eliminada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al eliminar la orden: {e}")



if __name__ == "__main__":
    app = InterfazAdmin()
    app.mainloop()
