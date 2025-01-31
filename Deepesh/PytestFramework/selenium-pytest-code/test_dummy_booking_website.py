import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver")
class TestDummyTicketWebsite:

    def test_user_info(self, request):
        self.v1.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.v1.find_element(By.ID, "destcity").send_keys("Kolkata")
        print(request.node.name)


        self.v1.find_element(By.ID, "billing_phone").send_keys("787987987")
        print(request.node.name)
