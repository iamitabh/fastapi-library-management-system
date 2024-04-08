from pydantic import BaseModel
from typing import Optional

class Author(BaseModel):
    city: str
    country: str

class Book(BaseModel):
    id: Optional[int]=None 
    name: str
    publised_at: int
    author: Author