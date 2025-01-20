import time

import pytest
from modules.google.google_page_class import Google_Page
from resource.google.google_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = Google_Page(self.driver)


    def test_search_data_on_google(self):
        self.gp.launch_google_page(google_url)
        self.gp.enter_value_to_search(search_data)
        self.gp.click_search_button()
        time.sleep(5)