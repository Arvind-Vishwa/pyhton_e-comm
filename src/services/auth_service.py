from src.core.database import db
from src.core.security import hash_password, verify_password, create_access_token
from src.models.user_model import user_helper

# Signup
def create_user(user_data):
    existing_user = db.users.find_one({"email": user_data.email})
    
    if existing_user:
        raise Exception("User already exists")

    hashed_pw = hash_password(user_data.password)

    new_user = {
        "email": user_data.email,
        "password": hashed_pw
    }

    result = db.users.insert_one(new_user)
    return str(result.inserted_id)

# Login
def login_user(user_data):
    user = db.users.find_one({"email": user_data.email})

    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(user_data.password, user["password"]):
        raise Exception("Invalid credentials")

    token = create_access_token({"user_id": str(user["_id"])})
    return token