import tkinter as tk
from tkinter import messagebox
from ad import InterfazAdmin
from tra import InterfazTrabajador

def login():
    aliasl =nombreU.get()
    clave = contraseña.get()

    def InterfazAdmin():
        app = InterfazAdmin()  
        app.mainloop()

    def InterfazTrabajador():
        app = InterfazTrabajador() 
        app.mainloop()



    if aliasl == "admin" and clave == "123":
        messagebox.showinfo("Bien entre", "Bienvenido!")
       
        InterfazAdmin()
    elif aliasl == "worker" and clave == "123":
        messagebox.showinfo("bien entre", "Bienvenido!")
        
        InterfazTrabajador()
    else:
        messagebox.showerror("3 a 0", "Incorrecto brother")



root = tk.Tk()
root.title("LOGIN")

nombrel = tk.Label(root, text="Usuario:")
nombrel.grid(row=0, column=0, padx=10, pady=10)

nombreU = tk.Entry(root)
nombreU.grid(row=0, column=1, padx=10, pady=10)


contraseñal = tk.Label(root, text="Clave:")
contraseñal.grid(row=1, column=0, padx=10, pady=10)

contraseña = tk.Entry(root, show="*")
contraseña.grid(row=1, column=1, padx=10, pady=10)

boton = tk.Button(root, text="Ingresar", command=login)
boton.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
