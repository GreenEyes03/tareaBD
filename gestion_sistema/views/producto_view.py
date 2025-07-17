import tkinter as tk
from tkinter import messagebox
from controllers.producto_controller import crear_producto, obtener_productos

def mostrar_vista_producto(root):
    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Nombre").grid(row=0, column=0)
    nombre = tk.Entry(frame)
    nombre.grid(row=0, column=1)

    tk.Label(frame, text="Descripción").grid(row=1, column=0)
    descripcion = tk.Entry(frame)
    descripcion.grid(row=1, column=1)

    tk.Label(frame, text="Precio").grid(row=2, column=0)
    precio = tk.Entry(frame)
    precio.grid(row=2, column=1)

    tk.Label(frame, text="Stock").grid(row=3, column=0)
    stock = tk.Entry(frame)
    stock.grid(row=3, column=1)

    def guardar():
        data = {
            "nombre": nombre.get(),
            "descripcion": descripcion.get(),
            "precio": float(precio.get()),
            "stock": int(stock.get())
        }
        crear_producto(data)
        messagebox.showinfo("Éxito", "Producto guardado")

    tk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=1)

    # Mostrar productos existentes
    lista = tk.Listbox(frame, width=50)
    lista.grid(row=5, column=0, columnspan=2)

    for producto in obtener_productos():
        lista.insert(tk.END, f"{producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")

    return frame
