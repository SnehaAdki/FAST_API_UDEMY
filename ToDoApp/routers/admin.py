from email.policy import default

from fastapi import Depends, APIRouter, HTTPException, Path
from models import Todos
from database import sessionLocal,engine
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from sqlalchemy.sql import text
from typing import Union
from sqlalchemy.sql import Selectable
from sqlalchemy.engine import Connection, Engine
import pandas as pd
from pydantic import BaseModel ,Field


from .auth import get_current_user


router = APIRouter()

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

def get_engine_connection():
    db_connection = None
    try:
        db = engine
        db_connection = db.connect()
        yield db_connection
    # except Exception as ex:
    #     raise HTTPException(status_code=status.WS_1011_INTERNAL_ERROR , detail='Connection Error')
    finally:
        # print("Closing the connection")
        db_connection.close()


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
engine_connection = Annotated[Session , Depends(get_engine_connection)]

def get_detials(selectable: Union[Selectable, str], connection: Union[Connection, Engine]) -> pd.DataFrame:
    return pd.read_sql(selectable,connection)

# via connection_engine dependency
@router.get("/all_todos_all_users",status_code=status.HTTP_200_OK)
async def read_all_todos_all_users(user:user_dependency, db_engine: engine_connection ):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail="Authentication Failed")
    query = text("""select * from todos""")
    val =  get_detials(selectable=query, connection=db_engine)
    return  val.to_dict(orient='records')


# via db sessionmaker dependency
@router.get("/all_todos",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency, db: db_dependency ):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail="Authentication Failed")
    return db.query(Todos).all()


@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todos(user:user_dependency, db: db_dependency , todo_id:int = Path(gt = 0)):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Not found')
    # db.delete(todo_model)
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
