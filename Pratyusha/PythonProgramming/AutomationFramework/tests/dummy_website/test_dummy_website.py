import time

import pytest
from modules.dummy_website.dummy_website_page_class import DummyWebsite
from resource.dummy_website.dummy_website_data import *
from utilities.utilities_tools import Utils

@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)
        self.util = Utils
        self.json_data = self.util.read_json_content(json_file_path)


    def test_book_dummy_ticket(self):
        self.dw.launch_dummy_website(dummy_website_url)
        self.dw.enter_firstname(self.json_data['user_data']['first_name'])
        self.dw.enter_lastname(self.json_data['user_data']['last_name'])
        self.dw.enter_dob(self.json_data['user_data']['dob'])
        self.dw.select_male_female(self.json_data['user_data']['male_female'])
        self.dw.select_number_of_passenger(self.json_data['user_data']['additional_pass'])
        time.sleep(5)
