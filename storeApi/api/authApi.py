from fastapi import HTTPException,status,Depends
from storeApi.models.user import RegisterInput
from storeApi.services.token_utils import get_password_hash
from storeApi.db.userDb import user_db
from storeApi.services.token_utils import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from storeApi.services.token_utils import authenticate_user
from datetime import timedelta


ACCESS_TOKEN_EXPIRE_MINUTES = 300

def register_user(user: RegisterInput):
    
    for existing_user in user_db.values():
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already registered")
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    user_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }

    return {"message": "User registered successfully"}

                  
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
                