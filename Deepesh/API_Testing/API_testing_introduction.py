# pip install requests
import requests
import json
from pprint import pprint


def get_all_data():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.json())


# get_all_data()

def add_objects():
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


# add_objects()

# ff808181932badb60194186f756846d6

def update_existing_details(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 200",
        "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "3 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


# update_existing_details('ff808181932badb60194186f756846d6')


def get_specific_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.json())


# get_specific_object("ff808181932badb60194186f756846d6")
# get_specific_object("ff808181932badb6019418764e9f46d8")

def delete_specific_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.json())


#delete_specific_object("ff808181932badb6019418764e9f46d8")
#get_specific_object("ff808181932badb6019418764e9f46d8")


def get_user_details_with_api_token():
    url = "https://gorest.co.in/public/v2/users"
    access_token = "2c23a02b621b71b08c567fab7d5a82459005026b8e4f14ac936f4d3e3b99e9e7"
    headers = {'Authorization': f"Bearer {access_token}"}
    response = requests.request("GET", url, headers=headers)
    pprint(response.json())
    print(response.status_code)

get_user_details_with_api_token()


#ETag : "etag-value"   (strong validation)
# ETag : W/"etag-value"  (weak validation)
