from selenium.webdriver.common.by import By

source_loc = (By.XPATH, "//label[contains(text(), 'source')]//parent::div")
source_loc_input = (By.XPATH, "//label[contains(text(), 'source')]//parent::div//following::div/input")