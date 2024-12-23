import time

import pytest
from page_class_file import Googlepage
from data_file import *

@pytest.mark.usefixtures("get_driver")

class TestGooglesearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = Googlepage(self.driver)

    def test_search_data_on_google(self):
        #self.gp = Googlepage(self.driver)
        self.gp.launch_google_page()
        self.gp.enter_value_to_search(search_data)
        self.gp.click_search_button()
        time.sleep(5)

