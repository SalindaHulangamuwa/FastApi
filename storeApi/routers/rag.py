from fastapi import APIRouter
from storeApi.models.query import Query
from storeApi.services.rag import rag_model

router=APIRouter()

@router.post("/query/")
async def query_rag_endpoint(query: Query):
    response=rag_model(query)
    return response

