from ast import pattern
from pydantic import BaseModel,Field,StrictInt
from typing import Optional
class Employee(BaseModel):  
    id: int=Field(...,gt=0)
    name: str=Field(...,min_length=2,max_length=30)
    age: int=Field(...,gt=18,lt=70)
    department: str=Field(...,min_length=2,max_length=50)
    is_full_time: bool = Field(default=True)  # default value
    salary: Optional[StrictInt] = Field(default=None)  # optional field
    email: Optional[str] = Field(default=None, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')  # optional with regex validation