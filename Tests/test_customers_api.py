import pytest
import requests
import json

customers_url = "http://simondfranklininshur.pythonanywhere.com/customers"
user = "adminuser"
password = "adminpassword"
customer1 = {"email": "customer1@inshur.com", "username": "customer1" }


def test_retrieve_all_customers():
    request = requests.get(customers_url, auth=(user, password))
    response = request.json()
    expected_customers = {}
    expected_customers["customers"] = {}
    customers = []
    for i in range (1,7):
        id = "customer{}".format(i)
        customer_dict = {"email": "{}@inhsur.com".format(id), "username": id}
        customers.append(customer_dict)
    expected_customers["customers"] = customers
    assert response == expected_customers
