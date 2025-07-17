import tkinter as tk
from tkinter import messagebox
from controllers.cliente_controller import crear_cliente, obtener_clientes

def mostrar_vista_cliente(root):
    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Nombre").grid(row=0, column=0)
    nombre = tk.Entry(frame)
    nombre.grid(row=0, column=1)

    tk.Label(frame, text="Correo").grid(row=1, column=0)
    correo = tk.Entry(frame)
    correo.grid(row=1, column=1)

    tk.Label(frame, text="Teléfono").grid(row=2, column=0)
    telefono = tk.Entry(frame)
    telefono.grid(row=2, column=1)

    def guardar():
        data = {
            "nombre": nombre.get(),
            "correo": correo.get(),
            "telefono": telefono.get()
        }
        crear_cliente(data)
        messagebox.showinfo("Éxito", "Cliente guardado")

    tk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=1)

    # Mostrar lista de clientes
    lista = tk.Listbox(frame, width=50)
    lista.grid(row=4, column=0, columnspan=2)

    for cliente in obtener_clientes():
        lista.insert(tk.END, f"{cliente['nombre']} - {cliente['correo']}")

    return frame
