from model.user import User
from sqlalchemy.orm.exc import NoResultFound
#from validate_email import validate_email
import hashlib


class UserRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def getAllUsers(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(User).all()
                return data
            except Exception as ex:
                db.session.rollback()
                raise ex


    def getUser(self, ulogin, upwd):
        
        with self.__ConnectionHandler() as db:
            try:
                hashedPassword = hashlib.sha256(upwd.encode()).hexdigest()
                data = db.session.query(User).filter(
                    User.usrname == ulogin).filter(User.usrpwd == hashedPassword).one()
                return data
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex


    def registerUser(self, uname, ulogin, upwd):
        res = self.getUser(ulogin,upwd)

        if (res == None):
            #is_verified = self.validation(uname, uemail, upwd)
            hashedPassword = hashlib.sha256(upwd.encode()).hexdigest()
            with self.__ConnectionHandler() as db:
                try:
                    dbins = User(usrfullname=uname, usrname=ulogin, usrpwd=hashedPassword)
                    db.session.add(dbins)
                    db.session.commit()
                    return 1
                except Exception as ex:
                    db.session.rollback()
                    raise ex
        else:
            return 2