import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utilities.utilities_tools import Utils
from resources.session_data import *


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.log = logging.getLogger(__name__)
        self.util = Utils()

    def get_element(self, locator,
                    wait_condition=ec.element_to_be_clickable):
        try:
            self.log.debug(f"Finding the element with locator: {locator}")
            element = self.wait.until(wait_condition(locator))
            return element
        except Exception as e:
            self.log.info(e)
            filename = f"element_not_found_{self.util.get_unique_name()}.png"
            file_path = os.path.join(log_folder_path, filename)
            self.log.warning(f"screenshot captured: {file_path}")
            self.driver.save_screenshot(file_path)
            raise

    def click_element(self, locator):

        element = self.get_element(locator)
        if element:
            self.log.critical(f"clicking on the element: {locator}")
            element.click()
        else:
            self.log.info(f"element not found with locator: {element} | {locator}")

    def send_keys_to_element(self, locator, value):
        element = self.get_element(locator)
        if element:
            self.log.error(f"sending text: {value},  to the element: {locator}")
            element.send_keys(value)
        else:
            self.log.info(f"element not found with locator: {element} | {locator}")

    def get_text(self, locator):
        element = self.get_element(locator)
        if element:
            self.log.info(f"getting text from the element: {locator}")
            return element.text
        else:
            self.log.info(f"element not found with locator: {element} | {locator}")

    def select_value_from_dropdown(self, locator, value):
        self.log.info(f"selecting value: {value} from dropdown: {locator}")
        element = self.get_element(locator)
        if element:
            select = Select(element)
            select.select_by_visible_text(value)
        else:
            self.log.info(f"element not found with locator: {element} | {locator}")
