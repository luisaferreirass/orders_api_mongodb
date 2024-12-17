from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection):
        self.__collection_name = "orders"
        #Estamos deixando claro que a coleção que estamos interagindo no Mongo é a "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        # A partir da conexão, vamos pegar uma coleção que tem exatamente o nome que colocamos
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, dict_filter: dict) -> list[dict]:
        # O filtro é um dicionário em que vamos colocar as propriedades que queremos
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(dict_filter)
        return data
    
    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)

        return response
    
    def select_many_with_properties(self, doc_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, # filtro de busca
            {"_id": 0, "cupom": 0} # opções de retorno, para não vim deixamos como 0
        )

        return data

    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"address": { "$exists": True }})
        # Estamos verificando quais são os dicts que possuem address

        return response
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data
