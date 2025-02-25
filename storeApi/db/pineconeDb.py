
from dotenv import load_dotenv
import os
from pinecone import Pinecone


def get_pinecone_collection():
    load_dotenv()
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pc=Pinecone(api_key=pinecone_api_key)
    return pc



