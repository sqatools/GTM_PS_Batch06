
import time

import pytest
from dummy_website_page_class import DummyWebsite
from data_file import *


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    a = 1
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_search_data_on_google(self):
        self.dw.launch_dummy_website(dummy_website_url)
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)
        time.sleep(5)
