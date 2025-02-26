from langchain_together import TogetherEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()


def embed_documents(documents):
    together_api_key = os.getenv("TOGETHER_API_KEY")
    embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval", together_api_key=together_api_key)
    print("Embedding documents...")
    return embeddings.embed_documents(documents)
