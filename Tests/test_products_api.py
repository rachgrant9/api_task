import pytest
import requests

products_url = "http://simondfranklininshur.pythonanywhere.com/products"
individual_product_url = "http://simondfranklininshur.pythonanywhere.com/product/"

def test_retrieve_products():
    request = requests.get(products_url)
    response_body = request.json()
    assert response_body["products"][0]["productName"] == "Taxi Product"
    assert response_body["products"][1]["productName"] == "Courier Product"

def test_individual_products():
    taxi_url = (individual_product_url + "1234")
    request = requests.get(taxi_url)
    response = request.json()
    assert response["productName"] == "Taxi"
    assert response["productVersion"] == 1.0

def test_nonexistent_product():
    nonexistent_url = (individual_product_url + "2222")
    request = requests.get(nonexistent_url)
    response = request.json()
    assert response["errorMessage"] == "product 2222 not found"

