from config.db import get_db
from bson.objectid import ObjectId

db = get_db()
pedidos = db["pedidos"]

def crear_pedido(data):
    return pedidos.insert_one(data).inserted_id

def obtener_pedidos():
    return list(pedidos.find())

def actualizar_estado_pedido(pedido_id, nuevo_estado):
    return pedidos.update_one({"_id": ObjectId(pedido_id)}, {"$set": {"estado": nuevo_estado}})

def eliminar_pedido(pedido_id):
    return pedidos.delete_one({"_id": ObjectId(pedido_id)})
