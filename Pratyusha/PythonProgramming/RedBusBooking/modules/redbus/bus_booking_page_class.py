from base.selenium_base_code import SeleniumBase
from .bus_booking_page_locators import *

class RedBusWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def launch_redbus_website(self, url):
        self.driver.get(url)

    def enter_value_to_source(self, source_city):
        self.click_element(source_loc)
        self.send_keys_to_element(source_loc_input, source_city)
