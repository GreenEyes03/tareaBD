from config.db import get_db
from bson.objectid import ObjectId

db = get_db()
productos = db["productos"]

def crear_producto(data):
    return productos.insert_one(data).inserted_id

def obtener_productos():
    return list(productos.find())

def actualizar_producto(producto_id, data):
    return productos.update_one({"_id": ObjectId(producto_id)}, {"$set": data})

def eliminar_producto(producto_id):
    return productos.delete_one({"_id": ObjectId(producto_id)})
