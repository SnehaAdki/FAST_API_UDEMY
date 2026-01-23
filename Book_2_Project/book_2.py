



from typing import Optional
from fastapi import FastAPI, Query, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id : int
    title : str
    author: str
    description : str
    rating : int
    published_date : int

    def __init__(self,id:int,title:str,author:str,description:str,rating:int, published_date:int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date  = published_date




class BookRequest(BaseModel):
    id : Optional[int] = Field(description= 'id is not needed on create',default=None)
    # title: str = Field(min_length=3,max_length=7 , default="A new Title")
    title: str = Field(min_length=3,max_length=7 )
    author: str = Field(min_length=1)
    description: str = Field(min_length=1 , max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date : int = Field(gt=1999 , lt = 2031)

    model_config = {
        "json_schema_extra" : {
            "example": {
                "title": " A new Book",
                "author": "Author Name",
                "description":"A new description of the book",
                "rating": 5,
                "published_date" :2012
            }
        }
    }



BOOKS = [
    Book(id=1,title="Computer Science Book",author="coding with ruby",description="Nice Book",rating=5,published_date =2012),
    Book(id=2,title="Fast API",author="coding with ruby",description="Great Book",rating=5,published_date =2013),
    Book(id=3,title="Master Endpoints",author="coding with ruby",description="Awesome Book",rating=5,published_date =2012),
    Book(id=4,title="HP1",author="Author 1",description="Book Description",rating=2,published_date =2012),
    Book(id=5,title="HP2",author="Author 2",description="Book Description",rating=3,published_date =2013),
    Book(id=6,title="HP3",author="Author 3",description="Book Description",rating=1,published_date =2014),
]


# get all books
@app.get("/books" , status_code= status.HTTP_200_OK) 
async def real_all_books():
    return {"books":BOOKS}

#get book based on rating via query param
@app.get("/books/")
async def get_book_by_rating(rating : int = Query(gt=0,lt=6)):
    books_rating = []
    for book in BOOKS:
        if book.rating == rating:
            books_rating.append(book)

    return {
        "message" : "Found with rating are",
        "data" : books_rating
    }



#get book w.r.t id via path param
@app.get("/books/{book_id}" , status_code=status.HTTP_200_OK)
async def get_book_id(book_id : int= Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return {
                "message" : "Found Book",
                "data" : book
            }
    raise HTTPException(status_code= 404 , detail="Cannot Find Book",)
    

# creating the book
@app.post("/create_books" , status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(new_book)

    BOOKS.append(find_book_id(new_book))
    return new_book

def find_book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id +1
    return book 



# update a piece of data
@app.put("/book" , status_code= status.HTTP_204_NO_CONTENT)
async def update_book(new_value : BookRequest):
    book_changed = False
    for i in range(0,len(BOOKS)):
        if BOOKS[i].id == new_value.id:
            book_changed = True
            BOOKS[i] =new_value
            
    if  not book_changed:
        raise HTTPException(status_code= 404 , detail=f"Cannot Find Book {new_value.id}",)

    #this weill never we retruned becz status code says that it should rtn nothing     
    # return {
    #     "message" : "Found updated",
    #     "data" : new_value
    # }
   


#deleet the book 
@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return {
                "message" : "Book Deleted"
            }
    raise HTTPException(status_code= 404 , detail=f"Cannot Find Book {book_id}",)


#assignment
# Assignment

# Here is your opportunity to keep learning!

# Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.

# Enhance each Book to now have a published_date

# Then create a new GET Request method to filter by published_date

# Solution in next video
#get book based on publichsed Date via query param

# @app.get("/books/" ,status_code=status.HTTP_201_CREATED)
# async def get_book_by_publish_date(rating: Optional[int] = Query(gt=0,lt=6,default=None), published_date: Optional[int] = Query(gt=1999,lt=2031,default=None)):
#     filtered_book = []
#     if rating is not None:
#         filtered_book  = [ book for book in BOOKS if book.rating == rating]
    
#     elif published_date is not None:
#         filtered_book = [ book for book in BOOKS if book.published_date == published_date]
    
#     else:
#         raise HTTPException(status_code= 404 , detail=f"Incorrect Filtered ",)

#     return {
#         "message" : f"Found with given {rating} {published_date} are",
#         "data" : filtered_book
#     }



