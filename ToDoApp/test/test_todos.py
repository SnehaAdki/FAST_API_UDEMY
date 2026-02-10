from starlette import status
from routers.todos import get_db,get_current_user
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticated(test_todos):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "title": "Test to Code!..",
            "description" : "Need to  Code Everyday!..",
            "priority" : 5,
            "complete" : False,
            "id" : 1,
            "owner_id" : 1}
        ]


def test_read_one_authenticated(test_todos):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
            "title": "Test to Code!..",
            "description" : "Need to  Code Everyday!..",
            "priority" : 5,
            "complete" : False,
            "id" : 1,
            "owner_id" : 1}


def test_read_one_invalid__authenticated(test_todos):
    response = client.get("/todo/10")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Record not found'}

def test_create_todo(test_todos):
    request_data =  {
            "title": "Learn DSA..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : False}
    response = client.post("/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    response = client.get("/todo/2")
    assert response.json() == {
            "title": "Learn DSA..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : False,
            "id" : 2,
            "owner_id" : 1}

def test_create_authorized_todo(test_todos):
    request_data =  {
            "title": "Learn DSA..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : False}
    response = client.post("/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    #to hit the db & find
    db = TestingSessionLocal()
    result_data_result_in_db = db.query(Todos).filter(Todos.title == "Learn DSA..").first()
    assert request_data.get('title') == result_data_result_in_db.title
    assert request_data.get('description') == result_data_result_in_db.description
    assert request_data.get('priority') == result_data_result_in_db.priority
    assert request_data.get('complete') == result_data_result_in_db.complete


    # to query & find it
    response = client.get("/todo/2")
    assert response.json() == {
            "title": "Learn DSA..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : False,
            "id" : 2,
            "owner_id" : 1}


def test_update_todo(test_todos):
    request_data =  {
            "title": "Learn DSA Advance..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : True}
    response = client.put("/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    #to hit the db & find
    db = TestingSessionLocal()
    result_data_result_in_db = db.query(Todos).filter(Todos.title == "Learn DSA Advance..").first()
    assert request_data.get('title') == result_data_result_in_db.title
    assert request_data.get('description') == result_data_result_in_db.description
    assert request_data.get('priority') == result_data_result_in_db.priority
    assert request_data.get('complete') == result_data_result_in_db.complete


    # to query & find it
    response = client.get("/todo/1")
    assert response.json() == {
            "title": "Learn DSA Advance..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : True,
            "id" : 1,
            "owner_id" : 1}


def test_invalid_update_todo(test_todos):
    request_data =  {
            "title": "Learn DSA Advance..",
            "description" : "Need to study daily!..",
            "priority" : 5,
            "complete" : True}
    response = client.put("/todo/1999", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    #to hit the db & find
    db = TestingSessionLocal()
    result_data_result_in_db = db.query(Todos).filter(Todos.title == "Learn DSA Advance..").first()
    assert result_data_result_in_db is None

    # to query & find it
    response = client.get("/todo/1999")
    assert response.json() == {'detail': 'Record not found'}

def test_delete_todo(test_todos):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    #to hit the db & find
    db = TestingSessionLocal()
    result_data_result_in_db = db.query(Todos).filter(Todos.id == 1).first()
    assert result_data_result_in_db is None

    # to query & find it
    response = client.get("/todo/1")
    assert  result_data_result_in_db is None

def test_delete_invalid_todo(test_todos):
    response = client.delete("/todo/199")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # to hit the db & find
    db = TestingSessionLocal()
    result_data_result_in_db = db.query(Todos).filter(Todos.id == 199).first()
    assert result_data_result_in_db is None

    # to query & find it
    response = client.get("/todo/199")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Record not found'}