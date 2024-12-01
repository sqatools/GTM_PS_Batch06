import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# TAG_NAME
header = driver.find_element(By.TAG_NAME, "h1")
print("header value: ", header.text)
# ID Locator
dob_elem = driver.find_element(By.ID, "birthday")
dob_elem.send_keys("08/26/2000")
time.sleep(3)
# Name Locator
frm_city = driver.find_element(By.NAME, "fromcity")
frm_city.send_keys("Pune")
time.sleep(3)
# Link Text
python_selenium_link = driver.find_element(By.LINK_TEXT, "Python Selenium")
python_selenium_link.click()
time.sleep(3)
# PARTIAL_LINK_TEXT
pytest_framework = driver.find_element(By.PARTIAL_LINK_TEXT, "Pytest")
pytest_framework.click()


time.sleep(5)

driver.close()