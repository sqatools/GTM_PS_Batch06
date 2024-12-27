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
    def create_unique_log_folder():
        unique_folder_name = Utils.get_unique_name()
        cwd = os.getcwd()
        log_folder_path = os.path.join(cwd, "logs")
        new_folder_path = os.path.join(log_folder_path, unique_folder_name)
        if not os.path.isdir(new_folder_path):
            os.mkdir(new_folder_path)

        return new_folder_path


# if __name__ == '__main__':
#
#     obj = Utils()
#     print(obj.get_unique_name())


