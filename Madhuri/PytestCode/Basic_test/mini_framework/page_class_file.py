
from data_file import*
from locator_file import*

class Googlepage:
    def __int__(self, driver):
        self.driver = driver

    def launch_google_page(self, url=google_url):
        self.driver.get(url)

    def enter_value_to_search(self, search_value ):
        self.driver.find_element(*search_filed_loactor).send_keys(search_value)

    def click_search_button(self):
        self.driver.find_element(*search_button_loactor).click()



