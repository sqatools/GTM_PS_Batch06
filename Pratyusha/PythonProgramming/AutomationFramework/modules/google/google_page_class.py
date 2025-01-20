from .google_page_locator import *
from base.selenium_base import SeleniumBase


class Google_Page(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_google_page(self, url):
        self.driver.get(url)

    def enter_value_to_search(self, search_value):
        self.send_keys_to_element(search_field_locator, search_value)

    def click_search_button(self):
        self.click_element(search_button_loc)
