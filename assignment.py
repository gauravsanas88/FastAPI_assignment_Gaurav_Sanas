# ///
# Assignment
 
# Postgres Server
# username = doadmin
# password = AVNS_ZAUb1Xd5Glnl9r2OMBU
# host = panorah-do-user-17039258-0.h.db.ondigitalocean.com
# port = 25060
# database = defaultdb
# sslmode = require
# Scenario
# Create 2 tables
 
# DocType
# a. Name
# b. Fields (Links to DocField)
 
# DocField
# a. Fieldname
# b. FieldLabel
# c. FieldType
# d. Parent (DocType)
# ///

from fastapi import FastAPI
from sql_alchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Sessionmaker
from sqlalchemy import Cloumn, String
from db.sesson import engine

app = FastAPI()

db_url = 'postgresql://doadmin:AVNS_ZAUb1Xd5Glnl9r2OMBU@panorah-do-user-17039258-0.h.db.ondigitalocean.com:25060/defaultdb'

create_engine(db_url)

session = Sessionmaker(autocommit=True, autoflush=True)
Base = declarative_base()

class DocType(Base):
    __tablename__ = "DocType"
    name = Cloumn(String)
    fields = Cloumn(String, primary_key=True)

class DocField(Base):
    __tablename__ = "DocField"
    Fieldname = Cloumn(String)
    FieldLabel = Cloumn(String)
    FieldType = Cloumn(String)
    Parent = Cloumn(String, foreign_key=DocType.fields)

Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
