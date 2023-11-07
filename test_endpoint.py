from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_home():
    res = client.get("/")
    assert res.status_code == 201
    assert res.headers["Content-Type"] == "application/json"
    assert res.json() == {"Hello": "World"}
