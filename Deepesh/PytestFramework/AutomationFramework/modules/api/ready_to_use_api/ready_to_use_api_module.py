from base.api_base import APIBase
from resources.api.api_data import *

class ReadyToUseAPI(APIBase):
    def get_list_of_all_objects(self):
        response, status_code = self.get_method(url=common_url)
        return response, status_code

    def get_list_of_objects_by_ids(self, id_list):
        common_url_new = common_url + "?"
        for id in id_list:
            common_url_new = common_url_new + f"id={id}&"
        response, status_code = self.get_method(url=common_url_new)
        return response, status_code

    def get_single_object(self, object_id):
        common_url_new = f"{common_url}/{object_id}"
        response, status_code = self.get_method(url=common_url_new)
        return response, status_code

    def add_object(self, request_data, headers):
        response, status_code = self.post_method(url=common_url, headers=headers, payload=request_data)
        return response, status_code

