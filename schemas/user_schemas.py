from pydantic import BaseModel
class UserCreate(BaseModel):
    name:str
    mail:str

class userUpdate(UserCreate):
    id:int
class UserResponse(userUpdate):
    pass