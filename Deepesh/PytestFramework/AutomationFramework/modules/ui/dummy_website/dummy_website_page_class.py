from Deepesh.PytestFramework.AutomationFramework.base.selenium_base import SeleniumBase
from .dummy_website_page_locator import *


class DummyWebsite(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def launch_dummy_website(self, url):
        self.log.info(f"Launching dummy ticket website: {url}")
        self.driver.get(url)

    def enter_first_name(self, first_name):
        self.log.info(f"enter first name: {first_name}")
        self.send_keys_to_element(first_name_loc, first_name)

    def enter_last_name(self, last_name):
        self.log.info(f"enter last name: {last_name}")
        self.send_keys_to_element(last_name_loc, last_name)

    def enter_dob(self, dob):
        self.log.info(f"select date of birth name: {dob}")
        self.send_keys_to_element(dob_calender, dob)

    def select_male_female(self, value):
        self.log.info(f"select male female radio option: {value}")
        if value.lower() == 'male':

            self.click_element(male_radio_btn)
        elif value.lower() == 'female':
            self.click_element(female_radio_btn)

    def select_number_of_passenger(self, no_pass):
        self.log.info(f"select number of passenger: {no_pass}")
        self.select_value_from_dropdown(add_more_pass_dd, no_pass)
