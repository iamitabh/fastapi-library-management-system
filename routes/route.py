from fastapi import APIRouter
from models.books import Book
from config.database import collection_name
from fastapi import HTTPException
from pymongo import ReturnDocument
import pymongo
from typing import Optional


router = APIRouter()

@router.get('/books')
async def get_books(country: Optional[str] = None, published_at: Optional[int] = None):

    query = {}

    if country is not None:
        query["author.country"] = country

    if published_at is not None:
        query["publised_at"] = {"$gt": published_at}

    if not query:
        books_cursor = collection_name.find()
    else:
        print(query)
        books_cursor = collection_name.find(query)

    books = [book for book in books_cursor]
    for book in books:
        book['_id'] = str(book['_id'])
    return books


@router.get('/books/{id}')
async def get_specific_book(id: int):
    specific_book = collection_name.find_one({'id': id})
    if specific_book is not None:
        specific_book['_id'] = str(specific_book['_id'])
        return specific_book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.post('/books')
async def post_book(book: Book):
    book_dic = book.model_dump()

    #In order to get the lastly added document
    last_created_document = collection_name.find_one(sort=[('_id', pymongo.DESCENDING)])

    #Now, extract the 'id' of the lastly created document and add 1 to it
    num_documents = last_created_document['id'] + 1
    book_dic['id'] = num_documents
    collection_name.insert_one(book_dic)
    return str(book_dic['id'])

@router.put('/books/{id}')
#Don't include the 'id' key-value in the request-body
async def update_book(id: int, book: Book):
    book_dict = book.model_dump()
    book_dict.pop('id')
    
    updated_book = collection_name.find_one_and_update(
        {'id': id},
        {'$set': book_dict},
        return_document=ReturnDocument.AFTER
    )

    if updated_book:
        updated_book['_id'] = str(updated_book['_id'])
        return updated_book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.delete('/books/{id}')
async def delete_book(id: int):
    collection_name.find_one_and_delete({"id": id})