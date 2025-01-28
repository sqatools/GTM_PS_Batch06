import time

from base.selenium_base_code import SeleniumBase
from .flight_booking_page_locators import *


class GoibiboWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)


    def launch_goibibo_website(self, url):
        self.driver.get(url)

    def close_popups(self):
        self.click_element(signup_popup_loc)
        try:
            self.click_element(scan_to_download_app_popup_loc)
        except Exception as e:
            print(e)
        try:
            self.switch_to_iframe(iframe_push_prompt_loc)
            self.click_element(notifications_popup_loc)
            self.switch_to_default_content()
        except Exception as e:
            print(e)

    def select_one_way_or_round_trip(self):
        self.click_element(round_trip_radio_loc)

    def enter_value_to_from_city(self, from_city):
        self.click_element(from_city_loc)
        self.send_keys_to_element(from_city_loc_input, from_city)
        element_list = self.get_elements(city_suggestion_list)
        for element in element_list:
            updated_text = element.text.replace("\n", "")
            print(updated_text)
            if updated_text == from_city:
                element.click()
                break

    def enter_value_to_dest_city(self, dest_city):
        # self.click_element(dest_city_loc)
        self.send_keys_to_element(dest_city_loc_input, dest_city)
        element_list = self.get_elements(city_suggestion_list)
        for element in element_list:
            updated_text = element.text.replace("\n", "")
            print(updated_text)
            if updated_text == dest_city:
                element.click()
                break

    def select_departure_date(self, departure_date):
        self.click_element(dept_date_loc)
        depart_date_xpath = (By.XPATH, f"//div[contains(@aria-label,'{departure_date}')]")
        self.click_element(depart_date_xpath)
        self.click_element(depart_date_xpath)


    def select_travellers_and_class(self, travel_class):
        self.click_element(travellers_and_class_dropdown_button)
        self.click_element(travellers_and_class_increase_count_of_Children)
        flight_class_xpath = (By.XPATH, f"//li[text()='{travel_class}']")
        self.click_element(flight_class_xpath)
        self.click_element(travellers_and_class_submit_loc)

    def special_fares(self):
        self.click_element(special_fares_for_student)
        print(special_student_radio.is_selected())

    def click_on_search_flights(self):
        self.click_element(search_flights_button_loc)
