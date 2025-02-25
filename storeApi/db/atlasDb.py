# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
# from dotenv import load_dotenv
# import os

# def get_atlas_collection(db_name="langchain_db", collection_name="test"):

#     load_dotenv()
#     atlas_connection_string = os.getenv("MONGODB_URI")
#     print(atlas_connection_string)
#     client = MongoClient(atlas_connection_string,server_api=ServerApi('1'))
#     print("Connected to MongoDB Atlas")
#     return client[db_name][collection_name]

# # if __name__ == "__main__":
# #     get_atlas_collection()


from pymongo import MongoClient
def create_db_and_insert_documents(uri):
    client = MongoClient(uri)
    
    try:
        
        database = client["sample_fruit"]
        
        collection = database["fruits"]
        
        collection.insert_many([
            { "_id": 1, "name": "apples", "qty": 5, "rating": 3, "color": "red", "type": ["fuji", "honeycrisp"] },
            { "_id": 2, "name": "bananas", "qty": 7, "rating": 4, "color": "yellow", "type": ["cavendish"] },
            { "_id": 3, "name": "oranges", "qty": 6, "rating": 2, "type": ["naval", "mandarin"] },
            { "_id": 4, "name": "pineapple", "qty": 3, "rating": 5, "color": "yellow" },
        ])
        
        print("Documents inserted successfully.")
        
    except Exception as e:
        print("Error inserting documents: ", e)
    
    finally:

        client.close()

if  __name__ == "__main__":
    uri = "mongodb+srv://2020e054:Sal31223951@cluster0.dpl28.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    create_db_and_insert_documents(uri)