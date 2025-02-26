from fastapi import HTTPException
from storeApi.models.rag import QueryRequest, QueryResponse
from storeApi.services.rag.rag import create_rag_model


async def query_rag_model(request: QueryRequest):
    try:
        result = create_rag_model(request.query)

        response = QueryResponse(
            answer=result["result"],
            source_documents=[doc.page_content for doc in result["source_documents"]]
        )
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
