import time

import pytest

from Deepesh.PytestFramework.AutomationFramework.modules.ui.dummy_website.dummy_website_page_class import DummyWebsite
from Deepesh.PytestFramework.AutomationFramework.resources.ui.dummy_website.dummy_website_data import json_file_path, \
    dummy_website_url
from Deepesh.PytestFramework.AutomationFramework.utilities.utilities_tools import Utils


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)
        self.util = Utils
        self.json_data = self.util.read_json_content(json_file_path)

    @pytest.mark.smoke
    def test_enter_user_details(self, request):
        self.dw.log.info("_"*50)
        self.dw.log.info(f"Test name: {request.node.name}")
        self.dw.launch_dummy_website(dummy_website_url)
        self.dw.enter_first_name(self.json_data['user_data']['first_name'])
        self.dw.enter_last_name(self.json_data['user_data']['last_name'])

    @pytest.mark.sanity
    def test_enter_dob_user_section(self, request):
        self.dw.log.info("_"*50)
        self.dw.log.info(f"Test name: {request.node.name}")
        self.dw.launch_dummy_website(dummy_website_url)
        self.dw.enter_dob(self.json_data['user_data']['dob'])
        self.dw.select_male_female(self.json_data['user_data']['male_female'])
        self.dw.select_number_of_passenger(self.json_data['user_data']['additional_pass'])
        time.sleep(5)
