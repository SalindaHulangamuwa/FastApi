from pymongo import MongoClient
from dotenv import load_dotenv
import os

def get_atlas_collection(db_name="langchain_db", collection_name="test"):

    load_dotenv()
    atlas_connection_string = os.getenv("MONGODB_URI")
    client = MongoClient(atlas_connection_string)
    print("Connected to MongoDB Atlas")
    return client[db_name][collection_name]
