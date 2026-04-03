from src.core.database import db
from bson import ObjectId

# Create product
def create_product(data):
    # Convert Pydantic model → JSON-safe dict
    product_data = data.model_dump(mode="json")

    result = db.products.insert_one(product_data)
    return str(result.inserted_id)


# Get all products (search + filter + sort + pagination)
def get_products(search=None, category=None, sort=None, page=1, limit=10):
    query = {}

    if search:
        query["title"] = {"$regex": search, "$options": "i"}

    if category:
        query["category"] = category

    skip = (page - 1) * limit

    cursor = db.products.find(query)

    # Sorting
    if sort == "asc":
        cursor = cursor.sort("price", 1)
    elif sort == "desc":
        cursor = cursor.sort("price", -1)

    products = list(cursor.skip(skip).limit(limit))

    # Convert ObjectId to string
    for p in products:
        p["_id"] = str(p["_id"])

    return products


# Get single product
def get_product(product_id):
    product = db.products.find_one({"_id": ObjectId(product_id)})

    if not product:
        return None

    product["_id"] = str(product["_id"])
    return product


# Update product
def update_product(product_id, data):
    update_data = {k: v for k, v in data.dict().items() if v is not None}

    db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )

    return get_product(product_id)


# Delete product
def delete_product(product_id):
    result = db.products.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count > 0