
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from storeApi.services.rag.llm import llm_together
from storeApi.services.rag.retrieverPinecone import retrieve_pinecone

def create_rag_model(query_text):

    retriever = retrieve_pinecone(query_text)

    llm = llm_together()
 
    prompt_template = """
    You are an assistant that answers questions based on the provided context.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Please provide a detailed and accurate answer based on the given context:
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    response = rag_chain.invoke({"query": query_text})

    return response

# # Example usage
# if __name__ == "__main__":
#     query = "What is machine learning?"
#     result = create_rag_model(query)
#     print("Answer:", result["result"])
#     print("\nSource Documents:")
#     for i, doc in enumerate(result["source_documents"]):
#         print(f"Document {i+1}:\n{doc.page_content}\n")