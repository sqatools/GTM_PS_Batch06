common_url = "https://api.restful-api.dev/objects"
objects_id_list = [3, 5, 7, 9]
single_object = 10
add_object_data = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

headers = {
        'Content-Type': 'application/json'
    }


users_api_url = "https://gorest.co.in/public/v2/users"
access_token = "2c23a02b621b71b08c567fab7d5a82459005026b8e4f14ac936f4d3e3b99e9e7"
headers_with_token = {'Authorization': f"Bearer {access_token}"}

