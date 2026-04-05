import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "CI/CD Pipeline works!"}

def test_calculate():
    response = client.get("/calculate?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}