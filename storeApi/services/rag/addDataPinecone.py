from storeApi.services.loadData import load_documents
from storeApi.services.rag.vectorStorePinecone import vector_store_pinecone
from storeApi.services.rag.splitDocument import split_documents


def load_data_pinecone():
    vector_store = vector_store_pinecone()
    data=load_documents()
    documents=split_documents(data)
    uuids = [str(i) for i in range(len(documents))]
    vector_store.add_documents(documents,ids=uuids)
    return vector_store


if __name__=="__main__":
    load_data_pinecone()


