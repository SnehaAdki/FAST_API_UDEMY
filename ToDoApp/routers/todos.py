from fastapi import Depends, APIRouter, HTTPException, Path, Request , status
from ..models import Todos
from ..database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel ,Field
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .auth import get_current_user

templates = Jinja2Templates(directory='ToDoApp/templates')

router = APIRouter(
    prefix='/todos',
    tags=['todos']
)


class ToDoRequest(BaseModel):
    title: str = Field(min_length=3)
    description : str = Field(min_length=3,max_length=100 )
    priority : int = Field (gt= 0 ,lt=6)
    complete: bool 


def get_db():
    db = sessionLocal()
    try: 
        yield db
    # except Exception as ex:
    #     raise HTTPException(status_code=status.WS_1011_INTERNAL_ERROR , detail='Connection Error')
    finally:
        # print("Closing the connection")
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]
user_dependency = Annotated[Session , Depends(get_current_user)]


def render_to_login():
    redirect_repsonse = RedirectResponse(url = "/auth/login-page",status_code=status.HTTP_302_FOUND)
    redirect_repsonse.delete_cookie(key="access_token")
    return redirect_repsonse

### Pages ###
@router.get("/todo-page")
async def render_todo_page(request : Request,db:db_dependency):
    try:
        user = await get_current_user(request.cookies.get('access_token'))
        if user is None:
            return render_to_login()
        todos = db.query(Todos).filter(Todos.owner_id == user.get("id")).all()
        print(user.get("id"))
        return templates.TemplateResponse("todo.html",{"request" : request,"todos":todos, "user":user})

    except Exception as ex:
        print("-------- Exception is ---------")
        print(ex)
        return render_to_login()

@router.get("/edit-todo-page/{todo_id}")
async def render_edit_todo_page(request : Request, db:db_dependency,todo_id:int ):
    try:
        user = await get_current_user(request.cookies.get('access_token'))
        if user is None:
            return render_to_login()
        todo = db.query(Todos).filter(Todos.id == todo_id).first()
        return templates.TemplateResponse("edit-todo.html",{"request" : request,"todo":todo, "user":user})

    except Exception as ex:
        print("-------- Exception is ---------")
        print(ex)
        return render_to_login()


@router.get("/add-todo-page")
async def render_add_todo_page(request : Request):
    try:
        print(request)
        user = await get_current_user(request.cookies.get('access_token'))
        if user is None:
            return render_to_login()
        # todo = db.query(Todos).filter(Todos.owner_id == user.get("id"))
        return templates.TemplateResponse("add-todo.html",{"request" : request, "user":user})

    except Exception as ex:
        print("-------- Exception is ---------")
        print(ex)
        return render_to_login()



### Endpoint ###


# get all record from dbs
@router.get("/",status_code=status.HTTP_200_OK)
async def read_data(user:user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()


# get all record from dbs where priority
@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_data(user:user_dependency, db: db_dependency , todo_id:int = Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    else:
        raise HTTPException(status_code=404,detail="Record not found")



# create a record in the db
@router.post('/todo',status_code=status.HTTP_201_CREATED)
async def crete_todo(user: user_dependency,
                     db:db_dependency ,
                     todo_request : ToDoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Authentication Failed")
    todo_model = Todos(**todo_request.model_dump(), owner_id = int(user.get('id')))
    db.add(todo_model)
    db.commit()


# update a record in the db
@router.put('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency ,
                      user: user_dependency,
                      new_todo_request : ToDoRequest,
                      todo_id:int = Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is  None:
        raise HTTPException(status_code=404, detail='Not found')
    todo_model.description = new_todo_request.description
    todo_model.complete = new_todo_request.complete
    todo_model.priority = new_todo_request.priority
    todo_model.title = new_todo_request.title
    db.add(todo_model)
    db.commit()



# delete a record in the db
@router.delete('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,
                    db:db_dependency ,
                      todo_id:int = Path(gt = 0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        db.query(Todos).filter(Todos.id == todo_id) \
            .filter(Todos.owner_id == user.get('id')).delete()
        db.commit()
    else:
        raise HTTPException(status_code=404, detail = 'Not found')

