from pinecone import ServerlessSpec
from storeApi.db.pineconeDb import get_pinecone_collection
import time


def indexing (index_name):

    index_name = index_name 
    pc = get_pinecone_collection()

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
        
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)
    
    index = pc.Index(index_name)

    return index
    