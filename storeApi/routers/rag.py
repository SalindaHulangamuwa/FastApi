from fastapi import APIRouter
from storeApi.models.rag import QueryRequest, QueryResponse
from storeApi.api.ragApi import query_rag_model

router=APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_rag_model_endpoint(request: QueryRequest):
        response = await query_rag_model(request)
        return response
    
