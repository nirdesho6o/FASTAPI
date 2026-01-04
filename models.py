from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int
    department: str
    is_full_time: bool = True  # default value
    salary: float | None = None  # optional field