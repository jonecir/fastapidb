from fastapi import FastAPI
#from view import view

from configs.dbconn import DBConnectionHandler
from controller.user_repo import UserRepository
from controller.token_repo import TokenRepository

from secrets import token_hex

repou = UserRepository(DBConnectionHandler)
repot = TokenRepository(DBConnectionHandler)

app = FastAPI()

@app.post('/adduser')
def adduser(uname:str, ulogin:str, upwd: str):
    result = repou.registerUser(uname, ulogin, upwd)
    if (result == 1):
        return "User has been registered!"
    else:
        return 'User already exists!'
