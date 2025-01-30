from base.selenium_base import SeleniumBase
from .saucedemo_website_page_locator import *


class SauceDemoWebsite(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def launch_website(self, url):
        self.log.info(f"Launching website: {url}")
        self.driver.get(url)

    def enter_username(self, username):
        self.log.info(f"enter username: {username}")
        self.send_keys_to_element(username_loc, username)

    def enter_password(self, password):
        self.log.info(f"enter password: {password}")
        self.send_keys_to_element(password_loc, password)

    def click_login(self):
        self.click_element(login_loc)

    def add_to_cart_1(self):
        self.click_element(first_product_loc)

    def add_to_cart_2(self):
        self.click_element(second_product_loc)

    def get_cart_count(self):
        return int(self.get_text(cart_loc))

    def click_cart(self):
        self.click_element(cart_loc)

    def click_checkout(self):
        self.click_element(checkout_loc)

    def enter_first_name(self, first_name):
        self.send_keys_to_element(first_name_loc, first_name)

    def enter_last_name(self, last_name):
        self.send_keys_to_element(last_name_loc, last_name)

    def enter_zip_code(self, zip_code):
        self.send_keys_to_element(zip_code_loc, zip_code)

    def click_checkout_continue(self):
        self.click_element(checkout_continue_loc)

    def click_checkout_finish(self):
        self.click_element(checkout_finish_loc)

    def get_order_page_text(self):
        return self.get_text(confirmation_text_loc)

    def click_burger_menu(self):
        self.click_element(burger_menu_loc)

    def click_logout(self):
        self.click_element(logout_loc)