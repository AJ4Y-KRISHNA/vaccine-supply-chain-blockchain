from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://localhost:27017/")
db = client["vaccinechain"]
users_collection = db["users"]

def create_user(username, password, role):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users_collection.insert_one({
        "username": username,
        "password": hashed,
        "role": role
    })

def get_user(username):
    return users_collection.find_one({"username": username})

def verify_user(username, password):
    user = get_user(username)

    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return user
    return None