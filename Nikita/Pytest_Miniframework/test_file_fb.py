import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver")
class facebook:

    def test_user_info(self, request):
        self.v1.find_element(By.XPATH, "//input[@data-testid='royal_email']").send_keys("admin")
        self.v1.find_element((By.XPATH, "//input[@data-testid='royal_pass']").send_keys("Password")
        print(request.node.name)

    def login(self, request):
        self.v1.find_element(By.XPATH, "//button[@data-testid='royal_login_button']").click()