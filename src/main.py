from fastapi import FastAPI
from src.api import auth_routes
from src.core.dependencies import get_current_user
from fastapi import Depends

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def home():
    return {"message": "API running"}


@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return {
        "message": "Protected route working",
        "user": str(user["_id"])
    }