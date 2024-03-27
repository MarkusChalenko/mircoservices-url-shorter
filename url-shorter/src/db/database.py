from core.config import app_settings
from pymongo.mongo_client import MongoClient

client = MongoClient(app_settings.db_uri)

db = client[app_settings.db_name]

collection_name = db["shorted_url_collection"]
