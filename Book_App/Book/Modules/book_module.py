from pydantic import BaseModel

class Book(BaseModel):
    Title: str
    Author: str
    Category :str