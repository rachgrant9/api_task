import pytest
import requests
products_url = "http://simondfranklininshur.pythonanywhere.com/products"

def test_retrieve_products():
    request = requests.get(products_url)
    response_body = request.json()
    assert response_body["products"][0]["productName"] == "Taxi Product"
    assert response_body["products"][1]["productName"] == "Courier Product"



