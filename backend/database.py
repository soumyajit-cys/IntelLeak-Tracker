from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

client = MongoClient(MONGO_URI)
db = client["darkweb_monitor"]

breach_collection = db["breach_data"]
keyword_collection = db["keywords"]
alert_collection = db["alerts"]