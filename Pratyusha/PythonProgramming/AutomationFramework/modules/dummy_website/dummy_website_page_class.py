from  base.selenium_base import SeleniumBase
from .dummy_website_page_locators import *

class DummyWebsite(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def launch_dummy_website(self, url):
        self.driver.get(url)

    def enter_firstname(self, first_name):
        self.send_keys_to_element(first_name_loc, first_name)

    def enter_lastname(self, last_name):
        self.send_keys_to_element(last_name_loc, last_name)

    def enter_dob(self, dob):
        self.send_keys_to_element(dob_calendar, dob)

    def select_male_female(self, value):
        if value.lower() == 'male':
            self.click_element(male_radio_button)
        elif value.lower() == 'female':
            self.click_element(female_radio_button)

    def select_number_of_passenger(self, no_of_pass):
        self.select_value_from_dropdown(add_more_pass_dd, no_of_pass)


