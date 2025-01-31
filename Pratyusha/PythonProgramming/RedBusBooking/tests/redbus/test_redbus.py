import time

import pytest
from modules.redbus.bus_booking_page_class import RedBusWebsite
from resource.redbus.bus_booking_data import *

@pytest.mark.usefixtures("get_driver")
class TestRedBus:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.rb = RedBusWebsite(self.driver)


    def test_bus_booking(self):
        self.rb.launch_redbus_website(redbusurl)
        self.rb.enter_value_to_source(source_city)
        time.sleep(5)
