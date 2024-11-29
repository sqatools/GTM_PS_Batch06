"""
install selenium with command
pip install selenium
pip : python package manager

->  Webelement : Any field visible on UI is known as webelement like link,. button, text field, radio etc
->  Each web element has their address to locate on website, that is known as locator.
->  We have different type of locator given below.

    1). ID = "id" : DONE
    2). XPATH = "xpath"
    3). LINK_TEXT = "link text" # : DONE
    4). PARTIAL_LINK_TEXT = "partial link text" : DONE
    5). NAME = "name" : DONE
    6). TAG_NAME = "tag name" : DONE
    7). CLASS_NAME = "class name"
    8). CSS_SELECTOR = "css selector"

"""
import time

# import webdriver from selenium
from selenium import webdriver

# import By class to get all locator type
from selenium.webdriver.common.by import By

# Open any specific browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
#driver = webdriver.Edge()

# maximize the browser window
driver.maximize_window()

# Set timeout for web element
driver.implicitly_wait(10)

# Open the website in the browser
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# TAG_NAME Locator
header = driver.find_element(By.TAG_NAME, "h1")
print("header value :", header.text)


# ID Locator
dob_elem = driver.find_element(By.ID, "birthday")
dob_elem.send_keys("04/22/1990")
time.sleep(3)

# Name Locator
from_city = driver.find_element(By.ID, "fromcity")
from_city.send_keys("Pune")
time.sleep(3)

# LINK Text locator
python_selenium_link = driver.find_element(By.LINK_TEXT, "Python Selenium")
python_selenium_link.click()
time.sleep(3)

# PARTIAL_LINK_TEXT locator
pytest_framework = driver.find_element(By.PARTIAL_LINK_TEXT, "Pytest")
pytest_framework.click()
time.sleep(3)

driver.close()


