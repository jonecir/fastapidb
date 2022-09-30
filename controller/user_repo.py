from model.user import User
from sqlalchemy.orm.exc import NoResultFound
#from validate_email import validate_email
import hashlib


class UserRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(User).all()
                return data
            except Exception as ex:
                db.session.rollback()
                raise ex