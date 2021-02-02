import pytest
import requests
import json

customers_url = "http://simondfranklininshur.pythonanywhere.com/customers"
user = "adminuser"
password = "adminpassword"
customer1 = {"email": "customer1@inshur.com", "username": "customer1" }
customer2 = {"email": "customer2@inshur.com", "username": "customer2" }
customer3 = {"email": "customer3@inshur.com", "username": "customer3" }
customer4 = {"email": "customer4@inshur.com", "username": "customer4" }
customer5 = {"email": "customer5@inshur.com", "username": "customer5" }
customer6 = {"email": "customer6@inshur.com", "username": "customer6" }


def test_retrieve_all_customers():
    request = requests.get(customers_url, auth=(user, password))
    response = request.json()
    assert response["customers"][0] == customer1
    assert response["customers"][1] == customer2
    assert response["customers"][2] == customer3
    assert response["customers"][3] == customer4
    assert response["customers"][4] == customer5
    assert response["customers"][5] == customer6

# def test_retrieve_all_customers():
#     # TODO: uncomment test and fix assertion so that customers can be generated, not stated as variables.
#     # currently the assertion is failing as the dicts are not equal.
#     request = requests.get(customers_url, auth=(user, password))
#     response = request.json()
#     expected_customers = {}
#     expected_customers["customers"] = {}
#     customers = []
#     for i in range (1,7):
#         id = "customer{}".format(i)
#         customer_dict = {"email": "{}@inhsur.com".format(id), "username": id}
#         customers.append(customer_dict)
#     expected_customers["customers"] = customers
#     assert response == expected_customers
