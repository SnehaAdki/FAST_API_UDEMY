# Assignment
#
# Here is your opportunity to keep learning!
#
# 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

from fastapi import  FastAPI


Books = [
    {"id":1,"Title": "Java Program", "Author": "Sneha", "Category": "Study"},
    {"id":2,"Title": "C Program", "Author": "Sheetal", "Category": "Study"},
    {"id":3,"Title": "C++ Program", "Author": "Siddheshwar", "Category": "Study"},
    {"id":4,"Title": "DSA Program", "Author": "Prakash", "Category": "Study"},
    {"id":5,"Title": "SQL Program", "Author": "Sonali", "Category": "Study"}
]

app = FastAPI()

@app.get("/")
async def get_books():
    return {
        "message": "Books Details",
        "data" : Books
    }


@app.get("/{book_id}")
async def get_books(book_id: int):
    for book in Books:
        if book["id"] == book_id:
            return {
                "message": "Book Details",
                "data":book}
    return {"message": "Book not found"}