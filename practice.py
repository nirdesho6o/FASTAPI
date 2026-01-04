from fastapi import FastAPI,HTTPException
from models import Employee
from typing import List

employees_db: List[Employee] = []

app=FastAPI()

#1. Read all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():   
    return employees_db

#2. Read a specific employee by id
@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    for emp in employees_db:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

