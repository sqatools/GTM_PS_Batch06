import time

import pytest
from modules.dummy_website.dummy_website_page_class import DummyWebsite
from resource.dummy_website.dummy_website_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)


    def test_book_dummy_ticket(self):
        self.dw.launch_dummy_website(dummy_website_url)
        self.dw.enter_firstname(first_name)
        self.dw.enter_lastname(last_name)
        time.sleep(5)
