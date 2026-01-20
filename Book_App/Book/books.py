
from FastAPI.Book_App.Book import router  # Import app from __init__.py

from fastapi.params import Body
# from Modules.book_module import  Book
# app.include_router(router)  # Include the app in your app

Books = [
            {"Title":"Java Program","Author":"Sneha","Category":"Study"},
            {"Title": "C Program", "Author": "Sheetal","Category":"Study"},
            {"Title": "C++ Program", "Author": "Siddheshwar","Category":"Study"},
            {"Title": "DSA Program", "Author": "Prakash","Category":"Study"},
            {"Title": "SQL Program", "Author": "Sonali","Category":"Study"},
            {"Title": "Python Program", "Author": "Shweta","Category":"Study"},
            {"Title": "Scala Program", "Author": "Vijay","Category":"Study"},
            {"Title": "Math Know", "Author": "Sonali","Category":"Math"},
            {"Title": "Algebra", "Author": "Sneha","Category":"Math"},
            {"Title": "Gemotry", "Author": "Julie","Category":"Math"},
            {"Title": "Know History", "Author": "Shubham","Category":"History"},
            {"Title": "W W 1", "Author": "Sanket","Category":"History"},
            {"Title": "W W 2", "Author": "Sneha", "Category": "History"},
        ]


# to get app books
# http://127.0.0.1:8000/books/all

@router.get("/all")
def read_all_books():
    return Books


# to get the books via title
#path param
# http://127.0.0.1:8000/books/W%20W%202
@router.get("/{book_title}")
async def read_book(book_title:str):
    for book in Books:
        if book.get("Title").casefold() == book_title.casefold():
            return {
                "status": True,
                "code": 200,
                "data": book
            }
    return {"Error":"Book not found"}



# to get books that has category
# query param of category
# http://127.0.0.1:8000/books?category=math

@router.get("")
async def get_books_by_category(category:str):
    books_to_return = []
    for book in Books:
        if book.get("Category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# to get all books via category & author
# combination of query param  & path param
# book_author is path param
# category is query param
# http://127.0.0.1:8000/books/Sneha
@router.get("/{book_author}/")
async def get_books_by_author_category(book_author:str , category:str):
    books_to_return = []
    for book in Books:
        if book.get("Category").casefold() == category.casefold() and book.get("Author").casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return

#to create a new record

@router.post("/")
# http://127.0.0.1:8000/books/
# body {}
async def create_book(new_book = Body()):
    Books.append(new_book)
    return new_book


#to update the existing record
# http://127.0.0.1:8000/books/update_book
# body {}
@router.put("/update_book")
async def update_book(updated_rec = Body()):
    for index in range(0,len(Books)):
        if Books[index].get('Title').casefold() == updated_rec.get('Title').casefold():
            Books[index] = updated_rec
            return {
                "updated_rec" : updated_rec,
                "message" : "Book updated"
            }
    return {
        "message": " Book not Found"
    }


# to delete a book
# query param type of deletion
# http://127.0.0.1:8000/books/del_book?book_title=Java%20Program
@router.delete("/del_book")
async def delete_book(book_title:str):
    for book in Books:
        if book.get("Title").casefold() == book_title.casefold():
            Books.remove(book)
            return {
                "message": "Book deleted"
            }
    return {
        "message": "Book not found"
    }
