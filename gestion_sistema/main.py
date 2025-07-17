import tkinter as tk
from views.cliente_view import mostrar_vista_cliente
from views.producto_view import mostrar_vista_producto
from views.pedido_view import mostrar_vista_pedido

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión de Clientes, Productos y Pedidos")
    root.geometry("800x600")  # Tamaño inicial de ventana

    menu = tk.Menu(root)
    root.config(menu=menu)

    def limpiar():
        for widget in root.winfo_children():
            if not isinstance(widget, tk.Menu):  # No borra el menú
                widget.destroy()

    def mostrar_clientes():
        limpiar()
        mostrar_vista_cliente(root)

    def mostrar_productos():
        limpiar()
        mostrar_vista_producto(root)

    def mostrar_pedidos():
        limpiar()
        mostrar_vista_pedido(root)

    menu.add_command(label="Clientes", command=mostrar_clientes)
    menu.add_command(label="Productos", command=mostrar_productos)
    menu.add_command(label="Pedidos", command=mostrar_pedidos)
    mostrar_clientes()

    root.mainloop()

if __name__ == "__main__":
    main()
