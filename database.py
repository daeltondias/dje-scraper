import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]

def salvar_publicacoes(dados):
    for item in dados:
        item['reu'] = "Instituto Nacional do Seguro Social - INSS"
        item['status'] = "nova"
        item['createdAt'] = datetime.utcnow()
    if dados:
        collection.insert_many(dados)

