from curses import echo
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import mysql.connector
from mysql.connector import Error


conn = 'mysql+pymysql://root:my20Adm!n22@localhost:3306/fastapidb'

engine = create_engine(conn, echo=True)

Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    usrfullname= Column(String(25))
    usrname = Column(String(25))
    usrpwd = Column(String(225))

    def __repr__(self) -> str:
        return f"User [Name: {self.usrfullname}, Username: {self.usrname}]"


class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    tkusrid = Column(Integer, ForeignKey("user.id"))
    tktoken = Column(String(225))
    tkdate = Column(DateTime, default=datetime.datetime.utcnow())


    def __repr__(self) -> str:
        return f"User [Token: {self.tktoken}]"



Base.metadata.create_all(engine)