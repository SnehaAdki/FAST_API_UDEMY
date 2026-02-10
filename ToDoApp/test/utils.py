from sqlalchemy import create_engine,text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from database import Base
from main import app
from fastapi.testclient import TestClient
import pytest
from models import Todos,User
from routers.auth import  bycrypt_context

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_db.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args= {"check_same_thread" : False},
    poolclass = StaticPool)


TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False,  bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username":'Sneha',"id":1 , "role":'admin'}


client = TestClient(app)

@pytest.fixture
def test_todos():
    todo = Todos(
        title = "Test to Code!..",
        description = "Need to  Code Everyday!..",
        priority = 5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM Todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = User(
            email='abc@12345',
            first_name='Sneha_Vj',
            last_name='Adki',
            is_active=True,
            phone_number='1234',
            role='Data Enginer',
            username='Sn_Vj12',
            hashed_password=bycrypt_context.hash('123')
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()