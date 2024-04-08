from pymongo import MongoClient

client=MongoClient('mongodb+srv://amitabhmishra2002:HdrvshmXn7ZzLfmE@cluster0.7mahv0o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db=client.library_db

collection_name = db['book_collection']