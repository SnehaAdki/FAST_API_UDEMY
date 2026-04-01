from fastapi import FastAPI , Request, status
from .models import Base
from .database import engine
from .routers import todos,auth,admin,user
# from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)
# templates = Jinja2Templates(directory="ToDoApp/templates")

app.mount("/static", StaticFiles(directory="ToDoApp/static"), name="static")
@app.get("/")
def test(request: Request):
    return  RedirectResponse(url='/todos/todo-page',status_code=status.HTTP_302_FOUND)

@app.get("/healthy")
def heal_check():
    return {'status': 'Healthy'}


app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)