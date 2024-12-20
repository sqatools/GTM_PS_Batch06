import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestDummyTicketWebsite:

    def test_user_info(self, request):
        self.v1.find_element(By.ID, "fromcity").send_keys("mumbai")
        self.v1.find_element(By.ID, "destcity").send_keys("kolkata")
        print(request.node.name)

    def test_billing_info(self, request):
        self.v1.find_element(By.ID, "bulling_name").send_keys("Rahul")
        self.v1.find_element(By.ID, "billin_phone").send_keys("787987987")
        print(request.node.name)
