from selenium.webdriver.common.by import By

first_name_loc = (By.XPATH, "(//input[@name='firstname'])[1]")
last_name_loc = (By.XPATH, "(//input[@name='firstname'])[2]")
dob_calendar = (By.ID, "birthday")
male_radio_button = (By.ID, "male")
female_radio_button = (By.ID, "female")
add_more_pass_dd = (By.ID, "admorepass")
