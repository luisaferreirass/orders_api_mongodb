import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_connection()

@pytest.mark.skip(reason= "interação com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {
        "alguma": "coisa",
        "valor": 5
    }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason= "interação com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_list_of_docs = [{
        "alguma": "coisa",
        "valor": 5
    }, {
        "outra": "coisa",
        "valor": 3
    }]
    orders_repository.insert_list_of_documents(my_list_of_docs)

@pytest.mark.skip(reason= "interação com o banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    # O response está apontando para todos os elementos q selecionamos no db

    print(response)

    for doc in response:
        print(doc)
        print()
        print(doc["itens"])

@pytest.mark.skip(reason= "interação com o banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    # O response está apontando para todos os elementos q selecionamos no db

    print(response)

@pytest.mark.skip(reason= "interação com o banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print(response)

    for doc in response:
        print(doc)
        print()
        print(doc["itens"])

@pytest.mark.skip(reason= "interação com o banco")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    # O response está apontando para todos os elementos q  no db (cursor)

    print(response)

    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason= "interação com o banco")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True,
                  "itens.doce": {"$exists": True}}
                # Semelhante a uma busca AND em sql
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()
    # Podemos usar o select_many c diferentes filtros

@pytest.mark.skip(reason= "interação com o banco")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [{ "address": {"$exists": True}},
        { "itens.doce.tipo": "chocolate "}
        ]
    }
    # Uma lista de filtros que pode ser um ou pode ser o outro
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()
    # Podemos usar o select_many c diferentes filtros

@pytest.mark.skip(reason= "interação com o banco")
def test_select_by_object_id():
    object_id = "66946242f2c205dcb32056ce"
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_by_object_id(object_id)
    print(response)