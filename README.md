# 📦 Orders API MongoDB

## 📝 Sobre o projeto

API REST para gerenciamento de pedidos desenvolvida com **Python** e **MongoDB**. O projeto implementa operações CRUD completas utilizando banco de dados NoSQL, demonstrando a flexibilidade e escalabilidade do MongoDB para aplicações modernas.

Ideal para aprendizado de:
- Bancos de dados NoSQL (MongoDB)
- APIs RESTful com Python
- PyMongo - Driver oficial do MongoDB
- Operações CRUD em documentos
- Modelagem de dados orientada a documentos
- Testes automatizados com Pytest
- Boas práticas de código com Pylint

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **MongoDB** - Banco de dados NoSQL
- **PyMongo 4.10.1** - Driver oficial do MongoDB para Python
- **DNSPython 2.7.0** - Suporte para conexões MongoDB Atlas
- **Pytest 8.3.3** - Framework de testes
- **Pylint 3.3.1** - Análise estática de código
- **isort 5.13.2** - Organização de imports

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- MongoDB instalado localmente ou conta no MongoDB Atlas
- pip (gerenciador de pacotes Python)

### Configuração do MongoDB

**Opção 1: MongoDB Local**
```bash
# Instale o MongoDB Community Edition
# Inicie o serviço MongoDB
mongod
```

**Opção 2: MongoDB Atlas (Cloud)**
1. Crie uma conta em [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crie um cluster gratuito
3. Obtenha a string de conexão

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/orders_api_mongodb.git
cd orders_api_mongodb
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure a conexão com o MongoDB:
```python
# Configure a URI de conexão no seu arquivo de configuração
MONGO_URI = "mongodb://localhost:27017/"  # Local
# ou
MONGO_URI = "mongodb+srv://user:password@cluster.mongodb.net/"  # Atlas
```

### Executando a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

### Executando os testes
```bash
pytest
```

ou para ver mais detalhes:
```bash
pytest -v
```

### Análise de código
```bash
# Verificar qualidade do código
pylint *.py

# Organizar imports
isort .
```

## 🎯 Funcionalidades

- ➕ **Criar** novos pedidos
- 📋 **Listar** todos os pedidos
- 🔍 **Buscar** pedido específico por ID
- ✏️ **Atualizar** informações de pedidos
- 🗑️ **Deletar** pedidos
- 🔎 **Filtrar** pedidos por status, cliente, data, etc.
- 📊 **Agregações** para análise de dados

## 🛠️ Modelo de dados

### Order (Pedido)
```json
{
  "_id": "ObjectId",
  "order_number": "ORD-001",
  "customer": {
    "name": "João Silva",
    "email": "joao@example.com",
    "phone": "+55 84 99999-9999"
  },
  "items": [
    {
      "product_name": "Produto A",
      "quantity": 2,
      "unit_price": 50.00,
      "total": 100.00
    }
  ],
  "total_amount": 100.00,
  "status": "pending",
  "created_at": "2024-02-04T10:30:00Z",
  "updated_at": "2024-02-04T10:30:00Z"
}
```

### Campos principais

| Campo | Tipo | Descrição |
|-------|------|-----------|
| _id | ObjectId | Identificador único do MongoDB |
| order_number | String | Número do pedido |
| customer | Object | Dados do cliente |
| items | Array | Lista de itens do pedido |
| total_amount | Number | Valor total do pedido |
| status | String | Status do pedido (pending, processing, shipped, delivered, cancelled) |
| created_at | DateTime | Data de criação |
| updated_at | DateTime | Data de atualização |

## 📸 Endpoints da API

### Pedidos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/orders` | Lista todos os pedidos |
| GET | `/orders/<id>` | Busca um pedido específico |
| POST | `/orders` | Cria um novo pedido |
| PUT | `/orders/<id>` | Atualiza um pedido existente |
| PATCH | `/orders/<id>` | Atualização parcial de um pedido |
| DELETE | `/orders/<id>` | Deleta um pedido |
| GET | `/orders/status/<status>` | Filtra pedidos por status |

## 💡 Exemplos de uso

### Criar um pedido
```bash
POST /orders
Content-Type: application/json

{
  "order_number": "ORD-001",
  "customer": {
    "name": "João Silva",
    "email": "joao@example.com",
    "phone": "+55 84 99999-9999"
  },
  "items": [
    {
      "product_name": "Notebook",
      "quantity": 1,
      "unit_price": 3000.00,
      "total": 3000.00
    },
    {
      "product_name": "Mouse",
      "quantity": 2,
      "unit_price": 50.00,
      "total": 100.00
    }
  ],
  "total_amount": 3100.00,
  "status": "pending"
}
```

**Resposta:**
```json
{
  "message": "Pedido criado com sucesso",
  "order_id": "65c0a1b2c3d4e5f6a7b8c9d0"
}
```

### Listar todos os pedidos
```bash
GET /orders
```

**Resposta:**
```json
{
  "orders": [
    {
      "_id": "65c0a1b2c3d4e5f6a7b8c9d0",
      "order_number": "ORD-001",
      "customer": {
        "name": "João Silva",
        "email": "joao@example.com"
      },
      "total_amount": 3100.00,
      "status": "pending",
      "created_at": "2024-02-04T10:30:00Z"
    }
  ],
  "total": 1
}
```

### Buscar pedido por ID
```bash
GET /orders/65c0a1b2c3d4e5f6a7b8c9d0
```

### Atualizar status do pedido
```bash
PATCH /orders/65c0a1b2c3d4e5f6a7b8c9d0
Content-Type: application/json

{
  "status": "shipped"
}
```

**Resposta:**
```json
{
  "message": "Pedido atualizado com sucesso"
}
```

### Filtrar pedidos por status
```bash
GET /orders/status/pending
```

### Deletar um pedido
```bash
DELETE /orders/65c0a1b2c3d4e5f6a7b8c9d0
```

**Resposta:**
```json
{
  "message": "Pedido deletado com sucesso"
}
```

## 🗄️ Vantagens do MongoDB

- **Schema Flexível**: Documentos podem ter estruturas diferentes
- **Escalabilidade Horizontal**: Fácil distribuição de dados
- **Performance**: Queries rápidas com indexação eficiente
- **Documentos JSON**: Estrutura natural para APIs REST
- **Agregações Poderosas**: Pipeline de agregação para análises complexas
- **Embedded Documents**: Relacionamentos mais eficientes

## 📊 Exemplos de Agregações
```python
# Total de vendas por status
db.orders.aggregate([
    {
        "$group": {
            "_id": "$status",
            "total": {"$sum": "$total_amount"},
            "count": {"$sum": 1}
        }
    }
])

# Produtos mais vendidos
db.orders.aggregate([
    {"$unwind": "$items"},
    {
        "$group": {
            "_id": "$items.product_name",
            "total_quantity": {"$sum": "$items.quantity"},
            "total_revenue": {"$sum": "$items.total"}
        }
    },
    {"$sort": {"total_quantity": -1}}
])
```

## 🧪 Testes

O projeto inclui testes automatizados com Pytest cobrindo:
- Criação de pedidos
- Listagem e busca
- Atualização de dados
- Deleção de pedidos
- Validações de dados
- Casos de erro

## 📝 Boas Práticas Implementadas

- **Pylint**: Análise estática de código para qualidade
- **isort**: Imports organizados e padronizados
- **Pytest**: Testes automatizados abrangentes
- **Validação de dados**: Verificação de entrada
- **Tratamento de erros**: Respostas claras para erros
- **Documentação**: Código bem documentado

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
