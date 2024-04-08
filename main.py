from fastapi import FastAPI
from routes.route import router 

app = FastAPI()

from pymongo.mongo_client import MongoClient
url="mongodb+srv://amitabhmishra2002:HdrvshmXn7ZzLfmE@cluster0.7mahv0o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url)
try:
    client.admin.command('ping')
    print('Pinged your deployment. You successfully connected to MongoDB!')
except Exception as e:
    print(e)

app.include_router(router)