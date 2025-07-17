from config.db import get_db
from bson.objectid import ObjectId

db = get_db()
clientes = db["clientes"]

def crear_cliente(data):
    return clientes.insert_one(data).inserted_id

def obtener_clientes():
    return list(clientes.find())

def actualizar_cliente(cliente_id, data):
    return clientes.update_one({"_id": ObjectId(cliente_id)}, {"$set": data})

def eliminar_cliente(cliente_id):
    return clientes.delete_one({"_id": ObjectId(cliente_id)})
