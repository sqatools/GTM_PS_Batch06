import json

class Utils:
    @staticmethod
    def read_json_content(filename):
        with open(filename, "r") as file:
            data = file.read()
            dict_data = json.loads(data)
            return dict_data