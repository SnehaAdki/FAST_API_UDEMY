from datetime import timedelta,datetime  ,timezone
from fastapi import APIRouter , Depends, HTTPException
from pydantic import BaseModel
from models import User
from database import sessionLocal
from typing import Annotated
from starlette import status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import  CryptContext
from jose import jwt , JWTError

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

SECRET_KEY = 'a long string'
ALGORITHM = 'HS256'

bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username : str
    email : str
    first_name : str
    last_name : str
    password : str
    role : str
    phone_number : str

class Token(BaseModel):
    access_token: str
    token_type: str

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


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bycrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id:str,role : str,expires_delta: timedelta):
    encode = {
        'sub' : username,
        'id': user_id,
        'role': role
    }
    expires = datetime.now(timezone.utc) + expires_delta

    encode.update({'exp' : expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username : str = payload.get('sub')
        user_id : str = payload.get('id')
        user_role : str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate username or password")
        return {"username":username,"id":user_id , "role":user_role}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate username or password")

@router.post("/",status_code=status.HTTP_201_CREATED)
async def crea_user(db: db_dependency , create_user: CreateUserRequest):
    create_user_mode = User(
        email = create_user.email,
        username = create_user.username,
        first_name = create_user.first_name,
        last_name = create_user.last_name,
        hashed_password = bycrypt_context.hash(create_user.password),
        role = create_user.role,
        is_active = True,
        phone_number = create_user.phone_number
    )
    db.add(create_user_mode)
    db.commit()

@router.post("/token",status_code=status.HTTP_200_OK , response_model=Token)
async  def login_for_access_toke(form_data: Annotated[OAuth2PasswordRequestForm, Depends()] , db:db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate username or password")
    token = create_access_token(user.username,user.id,user.role,timedelta(minutes=20))
    return  {
        'access_token': token,
        'token_type': 'bearer'
    }

