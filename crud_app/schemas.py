#defines pydantic schemas for user and item data validation
from pydantic import BaseModel,EmailStr
from pydantic import ConfigDict
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    department: Optional[str] = None
    model_config = ConfigDict(from_attributes=True) #this is to enable orm mode in pydantic v2
    
# defining separate classes for create, update, and output operations gives flexibility
class EmployeeCreate(EmployeeBase):
    email:Optional[EmailStr] = None

class EmployeeUpdate(EmployeeBase):
    email:Optional[EmailStr] = None
    age: Optional[int] = None
    department: Optional[str] = None

class EmployeeOut(EmployeeBase):  # to send data back to client
    id: int
    age: Optional[int] = None
    department: Optional[str] = None

    # # orm mode allows compatibility with ORM objects converting to json
    # class Config:
    #     orm_mode = True <---this is no longer supported in v2
