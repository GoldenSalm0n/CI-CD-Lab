from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "CI/CD Pipeline works!"}

@app.get("/calculate")
def calculate(a: int, b: int):
    return {"result": a + b}

def test_linter():
    """Тестова функція з правильним форматуванням."""
    x = 10
    y = 20
    return x + y