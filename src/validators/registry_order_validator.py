from cerberus import Validator

def registry_order_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": { "type": "string", "required": True},
                "address": { "type": "string", "required": True},
                "cupom": { "type": "boolean", "required": True},
                "itens": { 
                    "type": "list", 
                    "schema": {
                        "type": "dict",
                        "schema": { 
                            "item": { "type": "string", "required": True },
                        "quantidade": { "type": "integer", "required": True } 
                        }
                    }
                }
            }
        }
    }) # Vamos colocar aqui td a estrutura que eu quero

    response = body_validator.validate(body)

    if response is False:
        raise Exception(body_validator.errors)
