import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")

# explicit and fluent wait
wait = WebDriverWait(driver, 20, poll_frequency=2)


# element = wait.until(ec.presence_of_element_located((By.XPATH, "value")))


def get_element(locator, condition=ec.element_to_be_clickable):
    element = wait.until(condition(locator))
    return element


def get_elements_list(locator, condition=ec.presence_of_all_elements_located):
    elements_list = wait.until(condition(locator))
    return elements_list


from_city = get_element(locator=(By.ID, "fromcity"))
from_city.send_keys("Mumbai")
dest_city = get_element(locator=(By.ID, "destcity"))
dest_city.send_keys("Bangalore")

# with implicit wait
element_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(element_list)
for element in element_list:
    element.click()

time.sleep(3)

# with explicit wait
radio_btn_list = get_elements_list(locator=(By.XPATH, "//div[@align='left']/ul//input"))
for btn in radio_btn_list:
    btn.click()

time.sleep(3)


