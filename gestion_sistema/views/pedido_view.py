import tkinter as tk
from tkinter import messagebox
from controllers.pedido_controller import crear_pedido, obtener_pedidos
from controllers.cliente_controller import obtener_clientes
from controllers.producto_controller import obtener_productos

def mostrar_vista_pedido(root):
    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Cliente").grid(row=0, column=0)
    clientes = obtener_clientes()
    cliente_var = tk.StringVar()
    cliente_menu = tk.OptionMenu(frame, cliente_var, *[str(c["_id"]) for c in clientes])
    cliente_menu.grid(row=0, column=1)

    tk.Label(frame, text="Producto").grid(row=1, column=0)
    productos = obtener_productos()
    producto_var = tk.StringVar()
    producto_menu = tk.OptionMenu(frame, producto_var, *[str(p["_id"]) for p in productos])
    producto_menu.grid(row=1, column=1)

    tk.Label(frame, text="Cantidad").grid(row=2, column=0)
    cantidad = tk.Entry(frame)
    cantidad.grid(row=2, column=1)

    tk.Label(frame, text="Estado").grid(row=3, column=0)
    estado = tk.Entry(frame)
    estado.insert(0, "pendiente")
    estado.grid(row=3, column=1)

    def guardar():
        producto = {
            "producto_id": producto_var.get(),
            "cantidad": int(cantidad.get())
        }
        data = {
            "cliente_id": cliente_var.get(),
            "productos": [producto],
            "estado": estado.get()
        }
        crear_pedido(data)
        messagebox.showinfo("Éxito", "Pedido creado")

    tk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=1)

    lista = tk.Listbox(frame, width=70)
    lista.grid(row=5, column=0, columnspan=2)

    for pedido in obtener_pedidos():
        lista.insert(tk.END, f"Pedido: {pedido['_id']} - Cliente: {pedido['cliente_id']} - Estado: {pedido['estado']}")

    return frame
