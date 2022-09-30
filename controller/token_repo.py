from model.token import Token
from sqlalchemy.orm.exc import NoResultFound
#from validate_email import validate_email
import hashlib


class TokenRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler


    def getAllUserTokens(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Token).all()
                return data
            except Exception as ex:
                db.session.rollback()
                raise ex

    def getToken(self, token):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Token).filter(Token.tktoken == token).one()
                return data
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex


    def getUserToken(self, userid):
        
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Token).filter(
                    Token.tkusrid == userid).one()
                return data
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex


    def createToken(self, userid, token):
        with self.__ConnectionHandler() as db:
            try:
                dbins = Token(tkusrid=userid, tktoken=token)
                db.session.add(dbins)
                db.session.commit()
                return 1
            except Exception as ex:
                db.session.rollback()
                raise ex


    def saveNewToken(self, userid, token):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Token).filter(
                    Token.tkusrid == userid).update({'tktoken': token})
                db.session.commit()
                return 1
            except Exception as ex:
                db.session.rollback()
                raise ex