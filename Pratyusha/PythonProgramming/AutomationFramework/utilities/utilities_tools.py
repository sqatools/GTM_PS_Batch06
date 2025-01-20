import json

class Utils:
    def read_json_content(self, filename):
        with open(filename, "r") as file:
            data = file.read()
            dict_data = json.loads(data)
            return dict_data