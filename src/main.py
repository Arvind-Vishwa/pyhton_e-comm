from fastapi import FastAPI
from src.api import auth_routes
from src.core.dependencies import get_current_user
from fastapi import Depends
from src.api import product_routes
from src.api import cart_routes
from src.api import order_routes
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
    


app.include_router(product_routes.router, prefix="/products", tags=["Products"])


app.include_router(cart_routes.router)



app.include_router(order_routes.router)