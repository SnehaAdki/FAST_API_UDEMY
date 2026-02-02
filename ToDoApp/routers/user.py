# Assignment
#
# Here is your opportunity to keep learning!
#
# 1. Create a new route called Users.
#
# 2. Then create 2 new API Endpoints
#
# get_user: this endpoint should return all information about the user that is currently logged in.
#
# change_password: this endpoint should allow a user to change their current password.


from email.policy import default

from fastapi import Depends, APIRouter, HTTPException, Path
from models import Todos
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from models import User
from pydantic import BaseModel ,Field
from passlib.context import  CryptContext

from .auth import get_current_user


router = APIRouter()

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


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
bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserVerification(BaseModel):
    password: str = Field(min_length=3,max_length=10)
    new_password: str = Field(min_length=4)


@router.get("/get_user",status_code=status.HTTP_200_OK)
async  def get_user_details(user: user_dependency, db: db_dependency ):
    if user is None:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized")
    user_details = db.query(User).filter(User.id == user.get('id')).first()
    return user_details


@router.put("/password",status_code=status.HTTP_200_OK)
async def update_user_password(user: user_dependency,
                               db: db_dependency ,
                               new_password_req: UserVerification):
    if user is None:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized")
    user_details = db.query(User).filter(User.id == user.get('id')).first()
    breakpoint()
    if bycrypt_context.verify(new_password_req.password,user_details.hashed_password):
        new_pass = bycrypt_context.hash(new_password_req.new_password)
        user_details.hashed_password = new_pass
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK,detail="Password Changed")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Current Password Incorrect")