import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")


def get_element(locator):
    element = wait.until(ec.presence_of_element_located(locator))
    return element


get_element(locator=(By.PARTIAL_LINK_TEXT, "What is Software Testing")).click()
time.sleep(3)

windows_list = driver.window_handles
driver.switch_to.window(windows_list[1])

header = get_element(locator=(By.XPATH, "//h3[contains(text(), 'Software Testing')]"))
assert header
driver.close()

driver.switch_to.window(windows_list[0])
time.sleep(3)
get_element(locator=(By.PARTIAL_LINK_TEXT, "What is Manual Testing")).click()
time.sleep(3)
