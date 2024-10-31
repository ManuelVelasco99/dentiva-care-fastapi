from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class ConsultingRoomAddress(BaseModel):
    city: Optional[str] = None
    postalCode: Optional[str] = None
    province: Optional[str] = None
    street: Optional[str] = None
    number: Optional[int] = None
    apartment: Optional[str] = None
    status: bool
    _id: Optional[str] = None

class UserSchema(BaseModel):
    firstName: str
    lastName: str
    dni: str 
    cuil: str 
    email: EmailStr
    telephone: str
    consultingRoomAddress: Optional[ConsultingRoomAddress] = None
    profilePictureName: Optional[str] = ""
    files: List[str] = []
    activated: bool = False
    status: bool = True
    password: str

    class Config:
        allow_population_by_field_name = True  # Allows model to populate with field names
        use_enum_values = True
        schema_extra = {
            "example": {
                "firstName": "Juanita",
                "lastName": "McLaughlin",
                "dni": "54123518",
                "cuil": "15-582-932-2047",
                "email": "Jeanie.Wuckert59@example.net",
                "telephone": "632-798-0562",
                "consultingRoomAddress": {
                    "city": "Staceyland",
                    "postalCode": "TT",
                    "province": "Florine Parkways",
                    "street": "Odell Crest",
                    "number": "278",  # Ensure number is provided as a string
                    "apartment": "693",
                    "status": True,
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
