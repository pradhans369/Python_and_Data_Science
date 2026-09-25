import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
uri = os.getenv("URI")


# 2. Connect to MongoDB Atlas Cloud
client = MongoClient(uri)

# 3. Create/Access a Database named 'my_store'
db = client["my_store"]

# 4. Create/Access a Collection (table) named 'products'
products_collection = db["products"]

# -------------------------------------------------------------
# EXAMPLE 1: Insert a SINGLE document (insert_one)
# -------------------------------------------------------------
sample_product = {
    "item": "Laptop",
    "brand": "Dell",
    "price": 55000,
    "in_stock": True,
    "tags": ["electronics", "computers"]
}

result = products_collection.insert_one(sample_product)
print(f"✅ Inserted 1 item with ID: {result.inserted_id}")


# -------------------------------------------------------------
# EXAMPLE 2: Insert MULTIPLE documents at once (insert_many)
# -------------------------------------------------------------
many_products = [
    {
        "item": "Wireless Mouse",
        "brand": "Logitech",
        "price": 1200,
        "in_stock": True,
        "specs": {"dpi": 1600, "wireless": True}
    },
    {
        "item": "Mechanical Keyboard",
        "brand": "Keychron",
        "price": 6500,
        "in_stock": False,
        "tags": ["gaming", "accessories"]
    }
]

result_many = products_collection.insert_many(many_products)
print(f"✅ Inserted {len(result_many.inserted_ids)} items successfully!")


# -------------------------------------------------------------
# EXAMPLE 3: Read back the data from the cloud!
# -------------------------------------------------------------
print("\n--- Data currently in your Cloud Database: ---")
for doc in products_collection.find():
    print(doc)
