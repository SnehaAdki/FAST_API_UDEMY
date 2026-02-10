
from routers.user import get_db,get_current_user
from .utils import *
from starlette import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_user(test_user):
    response = client.get("/users/get_user")
    assert response.status_code ==  status.HTTP_200_OK
    assert response.json()['username'] == 'Sn_Vj12'
    assert response.json()['email'] == 'abc@12345'
    assert response.json()['last_name'] == 'Adki'
    assert response.json()['role'] == 'Data Enginer'
    assert response.json()['first_name'] == 'Sneha_Vj'
    assert response.json()['id'] == 1
    assert response.json()['is_active'] == True
    assert response.json()['phone_number'] == '1234'



def test_update_phone_number(test_user):
    response = client.put("/users/update_phone_number/11-234")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    updated_rec = db.query(User).filter(User.id == 1).first()
    assert updated_rec.phone_number == '11-234'



def test_update_password(test_user):
    response = client.put("/users/password",json={"password":"123","new_password":"1235"})
    assert response.status_code == status.HTTP_200_OK

    db = TestingSessionLocal()
    updated_rec = db.query(User).filter(User.id == 1).first()
    current_update_password = updated_rec.hashed_password
    assert bycrypt_context.verify("1235", current_update_password)


def test_update_invalid_password(test_user):
    response = client.put("/users/password",json={"password":"1234444","new_password":"1235"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()['detail'] == "Current Password Incorrect"


    db = TestingSessionLocal()
    updated_rec = db.query(User).filter(User.id == 1).first()
    current_update_password = updated_rec.hashed_password
    assert bycrypt_context.verify("123", current_update_password)
