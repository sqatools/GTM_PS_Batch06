from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def get_element(self, locator,
                    wait_condition=ec.element_to_be_clickable):
        element = self.wait.until(wait_condition(locator))
        return element

    def get_elements(self, locator,
                    wait_condition=ec.visibility_of_all_elements_located):
        elements = self.wait.until(wait_condition(locator))
        return elements

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

    def move_to_element(self, locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()

    def check_element_is_enabled(self, locator):
        element = self.get_element(locator)
        element.is_enabled()

    def switch_to_iframe(self, iframe_locator):
        element = self.get_element(iframe_locator)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
