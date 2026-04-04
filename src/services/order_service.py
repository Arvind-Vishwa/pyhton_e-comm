from bson import ObjectId, errors
from fastapi import HTTPException

def create_order_from_cart(db, user_id):
    # Fetch user's cart
    cart = db.carts.find_one({"user_id": user_id})
    if not cart or not cart.get("items"):
        raise HTTPException(status_code=400, detail="Cart is empty")

    order_items = []
    total_price = 0

    for item in cart["items"]:
        product_identifier = item["product_id"]  # Could be _id or SKU/code

        product = None

        # 1️⃣ Try as ObjectId
        if isinstance(product_identifier, str) and ObjectId.is_valid(product_identifier):
            product = db.products.find_one({"_id": ObjectId(product_identifier)})

        # 2️⃣ Fallback: try as SKU/code field
        if not product:
            product = db.products.find_one({"code": product_identifier})

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product not found: {product_identifier}"
            )

        price = product.get("price", 0)
        order_items.append({
            "product_id": str(product["_id"]),
            "quantity": item.get("quantity", 1),
            "price": price
        })
        total_price += price * item.get("quantity", 1)

    if not order_items:
        raise HTTPException(status_code=400, detail="No valid products found in cart")

    # Create order
    order_data = {
        "user_id": user_id,
        "items": order_items,
        "total_price": total_price
    }
    order = db.orders.insert_one(order_data)

    # Clear cart
    db.carts.update_one({"_id": cart["_id"]}, {"$set": {"items": []}})

    return {
        "order_id": str(order.inserted_id),
        "total_price": total_price
    }