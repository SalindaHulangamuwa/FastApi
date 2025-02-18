from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class SummaryResponse(BaseModel):
    id: int
    title: str
    content: str
