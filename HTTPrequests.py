from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
#Testing /products Endpoint
def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # You can add more assertions here to check the structure and data of the response
#Testing /category/{category_id}/avg-price Endpoint
def test_read_avg_price():
    category_id = 2  # Assuming category_id 2 is valid in your database
    response = client.get(f"/category/{category_id}/avg-price")
    assert response.status_code == 200
    data = response.json()
    assert "category_name" in data
    assert "average_price" in data
    assert isinstance(data["average_price"], float)
    # Add more assertions as necessary
