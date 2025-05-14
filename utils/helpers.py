import json
import os

DATA_FILE = os.path.join("data", "database.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "books": [], "transactions": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_max_id(data_list):
    try:
        return max(int(item["id"]) for item in data_list)
    except (ValueError, KeyError):
        return 0

def update_counters(data):
    from models.user import User
    from models.book import Book
    from models.transaction import Transaction

    User.id_counter = get_max_id(data.get("users", [])) + 1
    Book.id_counter = get_max_id(data.get("books", [])) + 1
    Transaction.id_counter = get_max_id(data.get("transactions", [])) + 1
