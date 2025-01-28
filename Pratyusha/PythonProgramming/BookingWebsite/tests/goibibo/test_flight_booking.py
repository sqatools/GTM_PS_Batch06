import time

import pytest
from modules.goibibo.flight_booking_page_class import GoibiboWebsite
from resource.goibibo.flight_booking_data import *

@pytest.mark.usefixtures("get_driver")
class TestGoibiboWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gib = GoibiboWebsite(self.driver)


    def test_flight_booking(self):
        self.gib.launch_goibibo_website(goibibo_url)
        self.gib.close_popups()
        self.gib.select_one_way_or_round_trip()
        self.gib.enter_value_to_from_city(from_city)
        self.gib.enter_value_to_dest_city(dest_city)
        self.gib.select_departure_date(dept_date)
        #time.sleep(10)
        self.gib.select_travellers_and_class(travel_class)
        #self.gib.special_fares()
        self.gib.click_on_search_flights()
        time.sleep(10)
