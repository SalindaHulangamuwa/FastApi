from pydantic import BaseModel, EmailStr

class RegisterInput(BaseModel):
    username: str
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
