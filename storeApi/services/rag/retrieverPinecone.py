from storeApi.services.rag.vectorStorePinecone import vector_store_pinecone

def retrieve_pinecone(query):
    vector_store=vector_store_pinecone()
    retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.5},
)
    retriever.invoke(query)
    return retriever