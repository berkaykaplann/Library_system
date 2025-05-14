import json
import os
from models.user import User
from utils.helpers import load_data, save_data

DATA_FILE = "data/database.json"

class UserService:
    @staticmethod
    def add_user(name, email, user_type="member"):
        data = load_data()
        new_user = User(name, email, user_type)
        data["users"].append(new_user.to_dict())
        save_data(data)
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        data = load_data()
        for user in data["users"]:
            if user["id"] == user_id:
                return User.from_dict(user)
        return None
