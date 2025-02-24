from storeApi.services.loadData import load_documents
from storeApi.services.splitDocument import split_documents
from storeApi.services.embeddingDocument import embed_documents
from storeApi.db.atlasDb import get_atlas_collection

from dotenv import load_dotenv
import os
load_dotenv()

together_api_key = os.getenv("TOGETHER_API_KEY")

def vector_store():

    data=load_documents()
    docs=split_documents(data)

    docs_to_insert = [{"text": doc.page_content,"embedding": embed_documents(doc.page_content)} for doc in docs]

    print("Inserting documents into MongoDB Atlas...")
    collection = get_atlas_collection()
    result = collection.insert_many(docs_to_insert)
    print(f"Inserted {len(result.inserted_ids)} documents")



if __name__ == "__main__":
    vector_store()

    

