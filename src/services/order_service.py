from bson import ObjectId


def create_order_from_cart(db, user_id):
    cart = db.carts.find_one({"user_id": user_id})

    if not cart or not cart.get("items"):
        raise Exception("Cart is empty")

    order_items = []
    total_price = 0

    for item in cart["items"]:
        product = db.products.find_one({
            "_id": ObjectId(item["product_id"])
        })

        if not product:
            continue

        price = product["price"]

        order_items.append({
            "product_id": item["product_id"],
            "quantity": item["quantity"],
            "price": price
        })

        total_price += price * item["quantity"]

    order_data = {
        "user_id": user_id,
        "items": order_items,
        "total_price": total_price
    }

    # Create order
    order = db.orders.insert_one(order_data)

    # Clear cart
    db.carts.update_one(
        {"_id": cart["_id"]},
        {"$set": {"items": []}}
    )

    return {
        "order_id": str(order.inserted_id),
        "total_price": total_price
    }
    
def get_user_orders(db, user_id):
    orders = list(db.orders.find({"user_id": user_id}))

    for order in orders:
        order["_id"] = str(order["_id"])

    return orders