
from starlette import status
from routers.auth import get_db,authenticate_user,create_access_token,SECRET_KEY,ALGORITHM,get_current_user
from .utils import *
from datetime import timedelta
from jose import jwt
import pytest
from fastapi import  HTTPException

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    response = authenticate_user(test_user.username, '123',db)
    assert response.username == test_user.username
    assert response.first_name == test_user.first_name
    assert response.last_name == test_user.last_name
    assert response.is_active == test_user.is_active
    assert response.role == test_user.role

def test_non_existent_user(test_user):
    db = TestingSessionLocal()
    response = authenticate_user(test_user.username, '12345555',db)
    assert response is False

    response = authenticate_user('wrong username', 'wrong password', db)
    assert response is False


def test_create_access_token(test_user):
    expires_delta = timedelta(minutes=1)



    token = create_access_token(test_user.username,test_user.id,test_user.role,expires_delta)
    decoded_token = jwt.decode(token, SECRET_KEY,
                               algorithms=[ALGORITHM],
                               options={'verify_signature': False})
    assert  decoded_token['sub'] == test_user.username
    assert decoded_token['id'] == test_user.id
    assert decoded_token['role'] == test_user.role


@pytest.mark.asyncio
async def test_get_current_user_valid(test_user):
    encode = {
        'sub': 'testuser',
        'id': 1,
        'role':'admin'
    }
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token)
    assert user == {'username': 'testuser', 'id': 1, 'role':'admin'}

@pytest.mark.asyncio
async def test_get_current_user_payload_missing(test_user):
    encode = {
        'role': 'user'
    }
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token)

    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate username or password'

