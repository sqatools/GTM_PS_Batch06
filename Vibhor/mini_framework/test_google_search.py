import time

import pytest
from page_class_file import GooglePage
from data_file import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)

    def test_search_data_on_google(self):
        self.gp.launch_google_page()
        self.gp.enter_value_to_search(search_data)
        self.gp.click_search_button()
        time.sleep(5)
