import time

import pytest
from goibibo_page_class import GoibiboWebsite
from data_file import *

@pytest.mark.usefixtures("get_driver")
class TestGoibiboWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gib = GoibiboWebsite(self.driver)


    def test_flight_booking(self):
        self.gib.launch_goibibo_website(goibibo_url)
        self.gib.close_signup_popup()
        self.gib.enter_value_to_fromcity(from_city)
        time.sleep(5)
