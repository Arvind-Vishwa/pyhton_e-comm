from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import hashlib

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    hashed = hashlib.sha256(password.encode('utf-8')).digest()  # ⚠️ use digest()
    return pwd_context.hash(hashed)

def verify_password(plain, hashed):
    plain_hashed = hashlib.sha256(plain.encode('utf-8')).digest()
    return pwd_context.verify(plain_hashed, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)