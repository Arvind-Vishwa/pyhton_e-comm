from fastapi import APIRouter, HTTPException
from src.schemas.user_schema import UserSignup, UserLogin
from src.services.auth_service import create_user, login_user

router = APIRouter()

@router.post("/signup")
def signup(user: UserSignup):
    try:
        user_id = create_user(user)
        return {"message": "User created", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(user: UserLogin):
    try:
        token = login_user(user)
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))