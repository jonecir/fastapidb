from configs.base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
import datetime

class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    tkusrid = Column(Integer, ForeignKey("user.id"))
    tktoken = Column(String(225))
    tkdate = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self) -> str:
        return f"User [Token: {self.tktoken}]"
