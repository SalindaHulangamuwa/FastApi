from pydantic import BaseModel, Field

class Query(BaseModel):
    query: str = Field(..., description="The query to search for.")