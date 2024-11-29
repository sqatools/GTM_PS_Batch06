"""
install selenium with command
pip install selenium
pip : python package manager

->  Webelement : Any field visible on UI is known as webelement like link,. button, text field, radio etc
->  Each web element has their address to locate on website, that is known as locator.
->  We have different type of locator given below.

    1). ID = "id"
    2). XPATH = "xpath"
    3). LINK_TEXT = "link text"
    4). PARTIAL_LINK_TEXT = "partial link text"
    5). NAME = "name"
    6). TAG_NAME = "tag name"
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
driver.get("https://www.google.co.in")

search_field = driver.find_element(By.NAME, "q")
print(search_field)
search_field.send_keys("Python Programming")

search_btn = driver.find_element(By.NAME, "btnK")
search_btn.click()

time.sleep(5)

# close the browser
driver.close()
