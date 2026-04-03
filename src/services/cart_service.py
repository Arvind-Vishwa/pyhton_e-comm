from src.repositories.cart_repositories import *


def get_or_create_cart(db, user_id):
    cart = get_cart_by_user(db, user_id)

    if not cart:
        cart = create_cart(db, user_id)

    return cart

def add_to_cart(db, user_id, product_id, quantity):
    cart = get_or_create_cart(db, user_id)

    items = cart.get("items", [])

    for item in items:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            break
    else:
        items.append({
            "product_id": product_id,
            "quantity": quantity
        })

    update_cart(db, cart["_id"], {"items": items})

    return {"message": "Item added", "items": items}

def remove_from_cart(db, user_id, product_id):
    cart = get_or_create_cart(db, user_id)

    items = [
        item for item in cart["items"]
        if item["product_id"] != product_id
    ]

    update_cart(db, cart["_id"], {"items": items})

    return {"message": "Item removed"}

def update_cart_item(db, user_id, product_id, quantity):
    cart = get_or_create_cart(db, user_id)

    items = cart["items"]

    for item in items:
        if item["product_id"] == product_id:
            if quantity <= 0:
                items.remove(item)
            else:
                item["quantity"] = quantity
            break

    update_cart(db, cart["_id"], {"items": items})

    return {"message": "Cart updated", "items": items}

def get_user_cart(db, user_id):
    cart = get_or_create_cart(db, user_id)

    cart["_id"] = str(cart["_id"])  # serialize

    return cart

