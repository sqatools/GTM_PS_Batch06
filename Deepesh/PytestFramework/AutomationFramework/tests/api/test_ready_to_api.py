import pytest
import json
from modules.api.ready_to_use_api.ready_to_use_api_module import ReadyToUseAPI
from resources.api.api_data import *


class TestReadyToUseApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.rt_api = ReadyToUseAPI()

    def test_get_all_objects_verify_the_account(self, request):
        self.rt_api.log.info(f"test name: {request.node.name}")
        response, status_code = self.rt_api.get_list_of_all_objects()
        assert len(response) == 13
        assert status_code == 200

    def test_get_list_objects_by_ids(self, request):
        self.rt_api.log.info(f"test name: {request.node.name}")
        response, status_code = self.rt_api.get_list_of_objects_by_ids(objects_id_list)
        assert len(response) == len(objects_id_list)
        assert status_code == 200

    def test_get_single_object(self, request):
        self.rt_api.log.info(f"test name: {request.node.name}")
        response, status_code = self.rt_api.get_single_object(single_object)
        assert len(response) == 3
        assert status_code == 200

    def test_add_object_and_verify(self, request):
        self.rt_api.log.info(f"test name: {request.node.name}")
        request_data = json.dumps(add_object_data)
        response, status_code = self.rt_api.add_object(request_data=request_data, headers=headers)
        assert len(response) == 4
        assert add_object_data['name'] == response['name']
        assert status_code == 200

    def test_get_users_details_with_token(self, request):
        self.rt_api.log.info(f"test name: {request.node.name}")
        response, status_code = self.rt_api.get_users_detail_with_token(headers=headers_with_token)
        assert len(response) == 10
        assert status_code == 200
