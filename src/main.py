from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "CI/CD Pipeline works!"}

@app.get("/calculate")
def calculate(a: int, b: int):
    return {"result": a + b}

def bad_code_test( ):
    a=   5
    b =10
    return a+ b