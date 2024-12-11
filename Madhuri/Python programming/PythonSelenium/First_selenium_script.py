"""
Installed selenium with command
pip install selenium
Pip:python package manager
-->webelement:- Any field visible on UI is known as webelement like link,button,textfeild,radio etc
--> each webelement has their aadress to locate on website.That is kmown as Locator
---> We have different type of locators given below.
  1) ID = "id"
  2) XPATH = " xpath"
  3) Link_TEXT = "link text"
  4) PARTIAL_LINK_TEXT = " partial link text"
  5) NAME = "name"
  6) TAG_NAME = "tag name"
  7) CLASS_NAME = "class name"
  8) CSS_SELECTOR = "css selector"
"""

import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
"""
# open any specific browser
driver: WebDriver = webdriver.Edge()
#driver = webdriver.Edge()
#driver = webdriver.firefox()
driver.get("https://www.google.co.in/")
# maximize the browser window
driver.maximize_window()
# set timeout  for web element
driver.implicitly_wait(30)

# open the website in the browser
driver.get("https://www.google.com/")
search_field = driver.find_element(By.NAME,"q")
print(search_field)
#search_field.send_keys("Python programming")

#search_btn = driver.find_element(By.NAME,"btnk")
#search_btn.click()

time.sleep(10)

# Close the browser
driver.close()

driver.get("https://www.facebook.com/login.php/")
search_email= driver.find_element(By.NAME,"email")
print(search_email)
search_email.send_keys("madhuri@gmail.com")
search_password = driver.find_element(By.NAME,"pass")
print(search_password)
search_password.send_keys("123$$")
search_Login = driver.find_element(By.NAME,"login")
search_Login.click()
"""
import time

from selenium import webdriver
from  selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)


driver.get("https://www.google.com/")
time.sleep(20)
""""
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# ID locator
dob_elem = driver.find_element(By.ID,"birthday")
dob_elem.send_keys("02/22/1987")
time.sleep(4)
# Name locator
from_city = driver.find_element(By.ID,"Fromcity")
from_city.send_keys("pune")
time.sleep(4)
# link Text locator //a[text()='python selenium]
python_selenium_link = driver.find_element(By.LINK_TEXT,"python selenium")
python_selenium_link.click()
time.sleep(4)
# partial_link_TEXT locator
pytest_framework = driver.find_element(By.PARTIAL_LINK_TEXT,"pytest")
pytest_framework.click()
time.sleep(4)
driver.close()
"""
driver.get()
time.sleep(10)






