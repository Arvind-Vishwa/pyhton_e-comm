from bson import ObjectId


def get_cart_by_user(db, user_id):
    return db.carts.find_one({"user_id": user_id})


def create_cart(db, user_id):
    cart = {
        "user_id": user_id,
        "items": []
    }
    result = db.carts.insert_one(cart)
    cart["_id"] = result.inserted_id
    return cart


def update_cart(db, cart_id, cart_data):
    db.carts.update_one(
        {"_id": ObjectId(cart_id)},
        {"$set": cart_data}
    )