from fastapi import APIRouter, Depends
from storeApi.models.user import RegisterInput
from storeApi.api.authApi import register_user,login_user
from storeApi.models.user import TokenResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register/")
async def register_user_endpoint(user: RegisterInput):
    return register_user(user)

@router.post("/login/", response_model=TokenResponse)
async def login_user_endpoint(form_data: OAuth2PasswordRequestForm = Depends()):
    return  login_user(form_data)

