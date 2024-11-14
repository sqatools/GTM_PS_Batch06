import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = json.loads(file.read())
        return data

data = read_json_data("test_data.json")
print(data)
print(data['browser'])
print(data['URL'])
