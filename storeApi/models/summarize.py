from pydantic import BaseModel
from typing import Optional

class TextInput(BaseModel):
    text: Optional[str] = None  

