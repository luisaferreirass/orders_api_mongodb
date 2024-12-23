from pymongo import MongoClient


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            "admin", 
            "password",
            "localhost",
            "27017"
        )
        # Nesses abres e fechas colocamos o username, password, host e porta
        # authSource=admin -> vamos entrar no mongo com permissões de admin
        self.__database_name = "rocket_db"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_connection(self):
        return self.__db_connection

db_connection_handler = DBConnectionHandler()