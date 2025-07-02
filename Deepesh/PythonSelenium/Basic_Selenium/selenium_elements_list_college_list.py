nb import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nirfindia.org/Rankings/2024/CollegeRanking.html")

# explicit and fluent wait
wait = WebDriverWait(driver, 20, poll_frequency=2)


def get_element(locator, condition=ec.element_to_be_clickable):
    element = wait.until(condition(locator))
    return element


def get_elements_list(locator, condition=ec.presence_of_all_elements_located):
    elements_list = wait.until(condition(locator))
    return elements_list


colleges_list = get_elements_list(locator=(By.XPATH, "//tbody//tr[@role='row']/td[2]"))
for college in colleges_list:
    with open("college_list.txt", "a") as file:
        print(college.text)
        file.write(f"{college.text}\n")

