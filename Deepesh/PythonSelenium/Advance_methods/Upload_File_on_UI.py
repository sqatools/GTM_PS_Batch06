import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
"""
Alert class only works with java script popup alert, there you can not find element.
"""

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")

upload_button = driver.find_element(By.ID, "myFile")
upload_button.send_keys("E:\\Filesdata\\count_name.txt")
time.sleep(5)

submit_btn = driver.find_element(By.XPATH, "//input[@id='myFile']//following-sibling::input[@type='submit']")
submit_btn.click()

success_elem = driver.find_element(By.XPATH, "//*[contains(text(), 'File Uploaded Successfully')]")
assert success_elem

time.sleep(5)

driver.close()
