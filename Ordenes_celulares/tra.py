import tkinter as tk
from tkinter import messagebox, Listbox
import psycopg2
import json

class InterfazTrabajador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajador")
        self.geometry("600x400")

        
        self.ordenes_label = tk.Label(self, text="Ordenes:")
        self.ordenes_label.pack(pady=10)

        
        self.ordenes_listbox = Listbox(self, height=10, width=50)
        self.ordenes_listbox.pack(pady=10)

        self.marcar_completado_button = tk.Button(self, text="Marcar como Completado", command=self.marcar_completado)
        self.marcar_completado_button.pack(pady=10)

    
        self.exportar_ordenes_button = tk.Button(self, text="Exportar orden", command=self.exportar_ordenes)
        self.exportar_ordenes_button.pack(pady=10)


        self.cargar_ordenes()

    def cargar_ordenes(self):
        try:
            conn = psycopg2.connect(dbname="db-", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT modelo, diagnostico,, nombre, cedula, fecha, completada FROM tareas")
            ordenes = cursor.fetchall()
            cursor.close()
            conn.close()

         
            self.ordenes_listbox.delete(0, tk.END) 
            for orden in ordenes:
                self.ordenes_listbox.insert(tk.END, f"{orden[0]} - {orden[1]}")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al cargar las ordenes de la paila: {e}")

    def marcar_completado(self):
        try:
            conn = psycopg2.connect(dbname="db-ordenes", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            
           
            modelo = "actualizar"  
            
            cursor.execute("UPDATE ordenes SET completada = TRUE WHERE nombre = %s", (modelo,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Yuhuuu", "Orden marcada como completada")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al marcar la orden como completada: {e}")

    def exportar_ordenes(self):
        try:
            conn = psycopg2.connect(dbname="db-ordenes", user="postgres", password="admin", host="localhost")
            cursor = conn.cursor()
            cursor.execute("SELECT modelo, diagnostico, nombre, cedula, fecha, completada FROM tareas")
            ordenes = cursor.fetchall()
            cursor.close()
            conn.close()

            ordenes_json = [{"orden": orden[0], "diagnostico": orden[1], "nombre": orden[2], "cedula": orden[3], "fecha": orden[4], "completada": orden[5]} for orden in ordenes]
            with open('tareas.json', 'w') as file:
                json.dump(ordenes_json, file)
            messagebox.showinfo("yeah", "Ordenes exportadas exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al exportar las ordenes: {e}")

if __name__ == "__main__":
    app = InterfazTrabajador()
    app.mainloop()
