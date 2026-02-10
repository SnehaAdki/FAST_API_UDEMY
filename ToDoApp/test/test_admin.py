from starlette import status
from routers.admin import get_db,get_current_user
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_users(test_todos):
    response = client.get("/admin/all_todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            'complete': False,
            'description': 'Need to  Code Everyday!..',
            'id': 1,
            'owner_id': 1,
            'priority': 5,
            'title': 'Test to Code!..',
        }
    ]

def test_delete_any_todo(test_todos):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # to hit the db & find
    db = TestingSessionLocal()
    result_data = db.query(Todos).filter(Todos.id == 1)
    assert result_data.count() == 0


def test_delete_any_todo_not_persent(test_todos):
    response = client.delete("/todo/199")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Not found'}

    # to hit the db & find
    db = TestingSessionLocal()
    result_data = db.query(Todos).filter(Todos.id == 199).first()
    assert result_data is None