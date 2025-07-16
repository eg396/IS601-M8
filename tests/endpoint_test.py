## endpoint_test.py
## IS 601, Module 8
## Evan Garvey

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text  # or assert response.json() == {"message": "Hello World"}

def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtract():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply():
    response = client.post("/multiply", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide():
    response = client.post("/divide", json={"a": 20, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero!"}