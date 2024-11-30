"""
-> Webelement: Any field visisble on UI is known as webelement like link, button, text field, radio button, checkbox, etc,.
-> Each webelement has their address to locate on the website, that is known as locator.
-> We have different types of locator given below.
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open any specific browser
driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

# Set timeout for web element
driver.implicitly_wait(10)

# Open the website in the browser
driver.get("https://www.google.co.in")

search_field = driver.find_element(By.NAME, "q")
print(search_field)
search_field.send_keys("Python Programming")

search_btn = driver.find_element(By.NAME, "btnK")
search_btn.click()

time.sleep(5)



# Close the browser
driver.close()
