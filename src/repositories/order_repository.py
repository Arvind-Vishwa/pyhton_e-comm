from datetime import datetime


def create_order(db, order_data):
    order_data["created_at"] = datetime.utcnow()
    result = db.orders.insert_one(order_data)
    order_data["_id"] = result.inserted_id
    return order_data


def get_orders_by_user(db, user_id):
    return list(db.orders.find({"user_id": user_id}))