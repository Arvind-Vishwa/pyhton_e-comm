## mini-Ecommerce-
  This project is an e-commerce backend built with FastAPI. It allows users to register, manage a shopping cart, and place orders. The backend integrates with MongoDB for data storage and includes JWT-based authentication for secure endpoints
### Folder Structure
```
└── 📁src
    └── 📁__pycache__
        ├── main.cpython-311.pyc
    └── 📁api
        └── 📁__pycache__
            ├── auth_routes.cpython-311.pyc
            ├── cart_routes.cpython-311.pyc
            ├── order_routes.cpython-311.pyc
            ├── product_routes.cpython-311.pyc
        ├── auth_routes.py
        ├── cart_routes.py
        ├── order_routes.py
        ├── product_routes.py
    └── 📁core
        └── 📁__pycache__
            ├── database.cpython-311.pyc
            ├── dependencies.cpython-311.pyc
            ├── security.cpython-311.pyc
        ├── database.py
        ├── dependencies.py
        ├── security.py
    └── 📁models
        └── 📁__pycache__
            ├── user_model.cpython-311.pyc
        ├── cart_model.py
        ├── user_model.py
    └── 📁repositories
        └── 📁__pycache__
            ├── cart_repositories.cpython-311.pyc
        ├── cart_repositories.py
        ├── order_repository.py
    └── 📁schemas
        └── 📁__pycache__
            ├── cart_schema.cpython-311.pyc
            ├── product_schema.cpython-311.pyc
            ├── user_schema.cpython-311.pyc
        ├── cart_schema.py
        ├── order_schema.py
        ├── product_schema.py
        ├── user_schema.py
    └── 📁services
        └── 📁__pycache__
            ├── auth_service.cpython-311.pyc
            ├── cart_service.cpython-311.pyc
            ├── order_service.cpython-311.pyc
            ├── product_service.cpython-311.pyc
        ├── auth_service.py
        ├── cart_service.py
        ├── order_service.py
        ├── product_service.py
    └── 📁utils
    └── main.py
```

### Tech Stack
* Backend Framework: FastAPI
* Database: MongoDB
* Authentication: JWT Tokens
* Python Packages:
  * pydantic – data validation
  * fastapi – API framework
  *   pymongo – MongoDB integration
  * bson – ObjectId handling
  *   passlib – password hashing

### Schema
### *`User collection`*
#### 
    {
        "_id": "ObjectId",
        "username": "string",
        "email": "string",
        "password": "hashed string",
        
    }

### *`Carts`*
####
    {
    "_id": "ObjectId",
    "user_id": "string or ObjectId", 
    "items": [
        {
        "product_id": "string",  
        "quantity": "int"
        }
        ]
    }

### *`orders`*
#### 
        {
    "_id": "ObjectId",
    "user_id": 
    "items": [
        {
        "product_id": "string",  
        "quantity": "int",
        "price": "float"
        }
    ],
    "total_price": "float",
    
    }

### API Endpoints
### Auth

* *`post`*-*`http://127.0.0.1:8000/auth/signup`*
* *`post`*-*`http://127.0.0.1:8000/auth/login`*
* *`get`*-*`http://127.0.0.1:8000/profile`*

### Product
* *`post`*-*`http://127.0.0.1:8000/products`*
* *`get`*-*`http://127.0.0.1:8000/products/:id`*
* *`delete`*-*`http://127.0.0.1:8000/products/:id
`*
### Cart
* *`post`*-*`http://127.0.0.1:8000/cart/add`*
* *`put`*-*`http://127.0.0.1:8000/cart/update`*
* *`delete`*-*`http://127.0.0.1:8000/cart/remove/:id`*
* *`get`*-*`http://127.0.0.1:8000/cart
`*
### order
* *`get`*-*`http://127.0.0.1:8000/orders`*
* *`post`*-*`http://127.0.0.1:8000/orders/checkout`*

### Setup instructions
####    
1. Clone repo
##### 
    git clone https://github.com/Arvind-Vishwa/python_e-comm.git
    

1. Create virtual environmen
#####
    python -m venv venv
    venv\Scripts\activate # window
    source venv/bin/activate # mac

1. Install dependecies
##### 
    pip install -r requirements.txt
   
1. env file
#####
     MONGO_URI="mongodb://localhost:27017/ecommerce"
     SECRET_KEY="your_jwt_secret_key"
1. Run the Server
####
    uvicorn src.main:app --reload

##### Note --  Always bear a authorization token
    