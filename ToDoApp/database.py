from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
# from sqlalchemy.ext.declarative import declarative_base

## sqlite connection
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

#postgress
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/TodoApplicationDatabase'

# mysql connection
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234@localhost:3306/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread' : False}) # used for the sqlite
# engine = create_engine(SQLALCHEMY_DATABASE_URL) used for the postgress
#engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False,autocommit = False, bind= engine)

Base = declarative_base()


