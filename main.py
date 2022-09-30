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

@app.post('/login')
def login(ulogin:str, upwd: str):
    user = repou.getUser(ulogin, upwd)
    if (user == None):
        return "User not found!"
    
    while True:
        token = token_hex(75)
        tokenExists = repot.getToken(token)

        if (tokenExists == None):
            userHasToken = repot.getUserToken(user.id)

            if (userHasToken == None):
                res = repot.createToken(user.id,token)
            else:
                res = repot.saveNewToken(user.id, token)

            break

    return token