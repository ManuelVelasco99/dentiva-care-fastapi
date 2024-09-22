from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId

class ConsultingRoomAddress(BaseModel):
    status: bool
    _id: Optional[str] = None

class UserSchema(BaseModel):
    firstName: str
    lastName: str
    dni: str
    cuil: str
    email: EmailStr
    telephone: str
    consultingRoomAddress: ConsultingRoomAddress
    profilePictureName: Optional[str] = ""
    files: List[str] = []
    activated: bool = False
    status: bool = True
    password: str

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Juanita",
                "lastName": "McLaughlin",
                "dni": "54123518",
                "cuil": "15-582-932-2047",
                "email": "Jeanie.Wuckert59@example.net",
                "telephone": "632-798-0562",
                "consultingRoomAddress": {
                    "status": False,
                    "_id": "6568d8f94ecbe72632307800"
                },
                "profilePictureName": "",
                "files": [],
                "activated": False,
                "status": True,
                "password": "hashed_password"
            }
        }

class UserInCreate(UserSchema):
    password: str  # Hashed in the logic, not saved directly
