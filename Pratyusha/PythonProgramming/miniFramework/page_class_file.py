from data_file import *
from locators_file import *

class Google_Page:
    def __init__(self, driver):
        self.driver = driver

    def launch_google_page(self, url=google_url):
        self.driver.get(url)

    def enter_value_to_search(self, search_value):
        self.driver.find_element(*search_field_locator).send_keys(search_value)

    def click_search_button(self):
        self.driver.find_element(*search_button_loc).click()
