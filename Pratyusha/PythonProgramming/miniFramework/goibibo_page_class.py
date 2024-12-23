from selenium_code_file import SeleniumBase
from goibibo_page_locators import *


class GoibiboWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)


    def launch_goibibo_website(self, url):
        self.driver.get(url)

    def close_signup_popup(self):
        self.click_element(signup_popup_loc)

    def enter_value_to_fromcity(self, from_city):
        self.click_element(from_city_loc)
        self.send_keys_to_element(from_city_loc_input, from_city)
