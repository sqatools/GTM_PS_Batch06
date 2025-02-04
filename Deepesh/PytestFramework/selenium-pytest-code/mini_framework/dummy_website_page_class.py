from selenium_code_file import SeleniumBase
from dummy_website_page_locator import *

class DummyWebsite(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def launch_dummy_website(self, url):
        self.driver.get(url)

    def enter_first_name(self, first_name):
        self.send_keys_to_element(first_name_loc, first_name)

    def enter_last_name(self, last_name):
        self.send_keys_to_element(last_name_loc, last_name)

