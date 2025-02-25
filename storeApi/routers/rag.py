from fastapi import APIRouter
from storeApi.services.retrieve import get_query_results
from dotenv import load_dotenv
from storeApi.models.query import Query
from langchain_community.llms import Together
import os


load_dotenv()
router=APIRouter()


@router.post("/query/")
async def query_rag(query: Query):

    context_docs = get_query_results(query)
    context_string = " ".join([doc["text"] for doc in context_docs])

    # Construct prompt for the LLM
    prompt = f"""Use the following pieces of context to answer the question at the end.
        {context_string}
        Question: {query}
    """
    together_api_key = os.getenv("TOGETHER_API_KEY")
    
    llm = Together(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1", 
        together_api_key=together_api_key,  
        temperature=0.3, 
        max_tokens=500,  
    )

    output = llm.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    return {"response": output.choices[0].message.content}