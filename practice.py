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

# 3. Add a new employee
@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    for emp in employees_db:
        if emp.id == employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees_db.append(employee)
    return employee 

# 4. Update an existing employee
@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees_db):
        if emp.id == employee_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# 5. Delete an employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, emp in enumerate(employees_db):
        if emp.id == employee_id:
            del employees_db[index]
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")