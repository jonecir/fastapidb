from configs.base import Base
from sqlalchemy import create_engine, Column, Integer, String


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    usrfullname= Column(String(25))
    usrname = Column(String(25))
    usrpwd = Column(String(225))

    def __repr__(self) -> str:
        return f"User [Name: {self.usrfullname}, Login: {self.usrname}]"

