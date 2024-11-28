import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")
time.sleep(5)
search_field = driver.find_element(By.NAME, "email")
search_field.send_keys("8884440484")
search_field = driver.find_element(By.NAME, "pass")
search_field.send_keys("vibhorkhare")
search_button = driver.find_element(By.NAME, "login")
search_button.click()
time.sleep(20)
# driver.close()