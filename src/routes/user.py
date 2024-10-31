from fastapi import APIRouter, Depends, HTTPException, status
from src.models.user import UserInCreate, UserSchema
from src.auth.hashing import get_password_hash, verify_password
from src.auth.jwt import create_access_token
from src.db import user_collection
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from typing import List

router = APIRouter()

@router.post("/register", response_model=UserSchema)
async def register_user(user: UserInCreate):
    user_dict = user.model_dump()
    user_dict["password"] = get_password_hash(user.password)
    user_dict["activated"] = False
    try:
        await user_collection.insert_one(user_dict)
        return user_dict
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )

@router.post("/login")
async def login_user(username: str, password: str):
    user = await user_collection.find_one({"email": username})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/", response_model=List[UserSchema])
async def get_all_users():
    users = await user_collection.find().to_list(length=None)
    return users
