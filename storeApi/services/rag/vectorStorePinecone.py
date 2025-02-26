from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from storeApi.services.rag.indexingPinecone import indexing

def vector_store_pinecone():
    index_name = "store-api"
    index = indexing(index_name)
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    return vector_store


if __name__ == "__main__":
    vector_store_pinecone()