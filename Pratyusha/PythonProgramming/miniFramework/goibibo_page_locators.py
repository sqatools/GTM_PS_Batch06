from selenium.webdriver.common.by import By

signup_popup_loc = (By.XPATH, "//span[contains(@class, 'icClose')]")
one_way_or_roun_trip = (By.XPATH, "//p[contains(text(), 'One')]")
from_city_loc = (By.XPATH, "//span[contains(text(),'From')]//following-sibling::p[contains(text(), 'Enter city or airport')]")
to_city_loc = (By.XPATH, "//span[contains(text(),'To')]//following-sibling::p[contains(text(), 'Enter city or airport')]")
from_city_loc_input = (By.XPATH, "//span[contains(text(),'From')]//following-sibling::input")
to_city_loc_input = (By.XPATH, "//span[contains(text(),'To')]//following-sibling::input")