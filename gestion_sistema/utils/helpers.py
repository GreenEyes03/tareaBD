from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://<IP_WINDOWS_SERVER>:27017/")
    db = client["sistema_gestion"]
    return db
