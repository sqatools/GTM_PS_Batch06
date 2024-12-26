import time

import pytest
from modules.google.google_page_class import GooglePage
from resources.google_page.google_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)

    def test_search_data_on_google(self, request):
        self.gp.log.info("_"*50)
        self.gp.log.info(f"Test name: {request.node.name}")
        self.gp.launch_google_page(google_url)
        self.gp.enter_value_to_search(search_data)
        self.gp.click_search_button()
        time.sleep(5)
