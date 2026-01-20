from fastapi import FastAPI
from FastAPI.Book_App.Book import router

app = FastAPI()
app.include_router(router)
