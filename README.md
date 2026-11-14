# 📦 Orders API MongoDB

## 📝 About the project

REST API for order management built with **Python** and **MongoDB**. The project implements full CRUD operations using a NoSQL database, showcasing MongoDB's flexibility and scalability for modern applications.

Great for learning:
- NoSQL databases (MongoDB)
- RESTful APIs with Python
- PyMongo - The official MongoDB driver
- CRUD operations on documents
- Document-oriented data modeling
- Automated testing with Pytest
- Clean code practices with Pylint

## 🚀 Technologies used

- **Python 3.x**
- **MongoDB** - NoSQL database
- **PyMongo 4.10.1** - Official MongoDB driver for Python
- **DNSPython 2.7.0** - Support for MongoDB Atlas connections
- **Pytest 8.3.3** - Testing framework
- **Pylint 3.3.1** - Static code analysis
- **isort 5.13.2** - Import sorting

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- MongoDB installed locally or a MongoDB Atlas account
- pip (Python package manager)

### MongoDB Setup

**Option 1: Local MongoDB**
```bash
# Install MongoDB Community Edition
# Start the MongoDB service
mongod
```

**Option 2: MongoDB Atlas (Cloud)**
1. Create an account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Get the connection string

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/orders_api_mongodb.git
cd orders_api_mongodb
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

5. Configure the MongoDB connection:
```python
# Set the connection URI in your configuration file
MONGO_URI = "mongodb://localhost:27017/"  # Local
# or
MONGO_URI = "mongodb+srv://user:password@cluster.mongodb.net/"  # Atlas
```

### Running the application
```bash
python app.py
```

The API will be available at: `http://localhost:5000`

### Running the tests
```bash
pytest
```

or, for more details:
```bash
pytest -v
```

### Code analysis
```bash
# Check code quality
pylint *.py

# Sort imports
isort .
```

## 🎯 Features

- ➕ **Create** new orders
- 📋 **List** all orders
- 🔍 **Find** a specific order by ID
- ✏️ **Update** order information
- 🗑️ **Delete** orders
- 🔎 **Filter** orders by status, customer, date, etc.
- 📊 **Aggregations** for data analysis

## 🛠️ Data model

### Order
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
      "product_name": "Product A",
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

### Main fields

| Field | Type | Description |
|-------|------|-----------|
| _id | ObjectId | MongoDB unique identifier |
| order_number | String | Order number |
| customer | Object | Customer data |
| items | Array | List of order items |
| total_amount | Number | Order total |
| status | String | Order status (pending, processing, shipped, delivered, cancelled) |
| created_at | DateTime | Creation date |
| updated_at | DateTime | Last update date |

## 📸 API Endpoints

### Orders

| Method | Endpoint | Description |
|--------|----------|-----------|
| GET | `/orders` | Lists all orders |
| GET | `/orders/<id>` | Retrieves a specific order |
| POST | `/orders` | Creates a new order |
| PUT | `/orders/<id>` | Updates an existing order |
| PATCH | `/orders/<id>` | Partially updates an order |
| DELETE | `/orders/<id>` | Deletes an order |
| GET | `/orders/status/<status>` | Filters orders by status |

## 💡 Usage examples

### Create an order
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

**Response:**
```json
{
  "message": "Pedido criado com sucesso",
  "order_id": "65c0a1b2c3d4e5f6a7b8c9d0"
}
```

### List all orders
```bash
GET /orders
```

**Response:**
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

### Find an order by ID
```bash
GET /orders/65c0a1b2c3d4e5f6a7b8c9d0
```

### Update order status
```bash
PATCH /orders/65c0a1b2c3d4e5f6a7b8c9d0
Content-Type: application/json

{
  "status": "shipped"
}
```

**Response:**
```json
{
  "message": "Pedido atualizado com sucesso"
}
```

### Filter orders by status
```bash
GET /orders/status/pending
```

### Delete an order
```bash
DELETE /orders/65c0a1b2c3d4e5f6a7b8c9d0
```

**Response:**
```json
{
  "message": "Pedido deletado com sucesso"
}
```

## 🗄️ Advantages of MongoDB

- **Flexible Schema**: Documents can have different structures
- **Horizontal Scalability**: Easy data distribution
- **Performance**: Fast queries with efficient indexing
- **JSON Documents**: A natural structure for REST APIs
- **Powerful Aggregations**: Aggregation pipeline for complex analysis
- **Embedded Documents**: More efficient relationships

## 📊 Aggregation Examples
```python
# Total sales by status
db.orders.aggregate([
    {
        "$group": {
            "_id": "$status",
            "total": {"$sum": "$total_amount"},
            "count": {"$sum": 1}
        }
    }
])

# Best-selling products
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

## 🧪 Tests

The project includes automated tests with Pytest covering:
- Order creation
- Listing and lookup
- Data updates
- Order deletion
- Data validation
- Error cases

## 📝 Best Practices Implemented

- **Pylint**: Static code analysis for quality
- **isort**: Organized, standardized imports
- **Pytest**: Comprehensive automated tests
- **Data validation**: Input checks
- **Error handling**: Clear error responses
- **Documentation**: Well-documented code

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
