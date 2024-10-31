from fastapi import APIRouter, HTTPException, status
from src.models.user import UserInCreate, UserSchema
from src.auth.hashing import get_password_hash
from src.db import user_collection
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

@router.get("/", response_model=List[UserSchema])
async def get_all_users():
    users = await user_collection.find().to_list(length=None)
    return users
