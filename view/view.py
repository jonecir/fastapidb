from configs.dbconn import DBConnectionHandler
from controller.user_repo import UserRepository
from controller.token_repo import TokenRepository

repou = UserRepository(DBConnectionHandler)
repot = TokenRepository(DBConnectionHandler)

print(repou,repot)