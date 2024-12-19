import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
@pytest.fixture(scope="module", autouse=True)
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.co.in")


def test_search_on_google():
    driver.find_element(By.NAME, "q").send_keys("Python Selenium")
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)


