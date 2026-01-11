from fastapi import FastAPI , HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base 
from typing import List
import models, schemas, crud
Base.metadata.create_all(bind=engine)  # create tables

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#endpoints
#create endpoint to get an employees
@app.post("/employees/", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


#endpoint to read all employees
@app.get("/employees/", response_model=List[schemas.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db=db)

#endpoint to get employee by id
@app.get("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#endpoint to update employee
@app.put("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db=db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#endpoint to delete employee
@app.delete("/employees/{employee_id}", response_model=dict) #returning a message
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {'detail': 'Employee deleted successfully'}