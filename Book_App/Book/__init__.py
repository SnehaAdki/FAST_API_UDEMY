from fastapi import APIRouter

router = APIRouter(prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found"}})

from FastAPI.Book_App.Book import books