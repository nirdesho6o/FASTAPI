from fastapi import FastAPI

app=FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/party")
def party():
    return {"message": "Let's party!"}