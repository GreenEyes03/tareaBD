class Pedido:
    def __init__(self, cliente_id, productos, estado):
        self.cliente_id = cliente_id
        self.productos = productos  # Lista de diccionarios: [{producto_id, cantidad}]
        self.estado = estado

    def to_dict(self):
        return {
            "cliente_id": self.cliente_id,
            "productos": self.productos,
            "estado": self.estado
        }
