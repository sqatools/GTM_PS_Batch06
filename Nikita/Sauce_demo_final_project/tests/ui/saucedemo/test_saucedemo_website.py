import time
import pytest

from Nikita.Sauce_demo_final_project.modules.ui.saucedemo.saucedemo_website_page_class import SauceDemoWebsite
from Nikita.Sauce_demo_final_project.resources.ui.saucedemo.saucedemo_website_data import json_file_path, url
from Nikita.Sauce_demo_final_project.utilities.utilities_tools import Utils


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = SauceDemoWebsite(self.driver)
        self.util = Utils
        self.json_data = self.util.read_json_content(json_file_path)

    @pytest.mark.negative
    def test_login_invalid(self, request):
        self.dw.log.info(f"Test name: {request.node.name}")
        self.dw.launch_website(url)
        time.sleep(1)
        self.dw.enter_username(self.json_data['invalid_login_data']['username'])
        time.sleep(1)
        self.dw.enter_password(self.json_data['invalid_login_data']['password'])
        time.sleep(1)
        self.dw.click_login()
        time.sleep(2)

    @pytest.mark.positive
    def test_login_success(self, request):
        self.dw.log.info(f"Test name: {request.node.name}")
        self.dw.launch_website(url)
        time.sleep(1)
        self.dw.enter_username(self.json_data['valid_login_data']['username'])
        time.sleep(1)
        self.dw.enter_password(self.json_data['valid_login_data']['password'])
        time.sleep(1)
        self.dw.click_login()
        time.sleep(2)

    @pytest.mark.positive
    def test_add_to_cart(self):
        self.dw.add_to_cart_1()
        self.dw.add_to_cart_2()
        time.sleep(2)

    @pytest.mark.positive
    def test_verify_cart_count(self):
        cart_count = self.dw.get_cart_count()
        assert cart_count == 2, f"Expected cart count 2, but got {cart_count}"

    @pytest.mark.positive
    def test_go_to_checkout(self):
        self.dw.click_cart()
        self.dw.click_checkout()
        time.sleep(2)

    @pytest.mark.positive
    def test_checkout_details(self):
        self.dw.enter_first_name(self.json_data['user_data']['firstname'])
        self.dw.enter_last_name(self.json_data['user_data']['lastname'])
        self.dw.enter_zip_code(self.json_data['user_data']['zipcode'])
        time.sleep(2)
        self.dw.click_checkout_continue()
        self.dw.click_checkout_finish()
        time.sleep(2)

    @pytest.mark.positive
    def test_order_confirmation(self):
        order_page_text = self.dw.get_order_page_text()
        assert order_page_text == 'Thank you for your order!', f"Expected text Thank you for your order!, but got {order_page_text}"

    @pytest.mark.positive
    def test_logout(self):
        self.dw.click_burger_menu()
        self.dw.click_logout()
        time.sleep(2)