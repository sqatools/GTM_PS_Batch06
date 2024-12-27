from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def get_element(self, locator,
                    wait_condition=ec.element_to_be_clickable):
        element = self.wait.until(wait_condition(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def send_keys_to_element(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def select_value_from_dropdown(self, locator, value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)
