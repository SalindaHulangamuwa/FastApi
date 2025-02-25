from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

def get_atlas_collection(db_name="langchain_db", collection_name="test"):

    load_dotenv()
    atlas_connection_string = os.getenv("MONGODB_URI")
    print(atlas_connection_string)
    client = MongoClient(atlas_connection_string,server_api=ServerApi('1'))
    print("Connected to MongoDB Atlas")
    return client[db_name][collection_name]

if __name__ == "__main__":
    get_atlas_collection()
