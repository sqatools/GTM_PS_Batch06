import json
import os
from datetime import datetime

class Utils:
    @staticmethod
    def read_json_content(filename):
        with open(filename, "r") as file:
            data = file.read()
            dict_data = json.loads(data)
            return dict_data


    @staticmethod
    def get_unique_name():
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    @staticmethod
    def update_logs_filename(filepath, update_path):
        os.rename(filepath, update_path)


# if __name__ == '__main__':
#
#     obj = Utils()
#     print(obj.get_unique_name())


