"""
Implicit wait: Implicit wait applies on all the web element by default, the timeout
               given in implicit wait is maximum time out to find the element.
               if driver found the element within 1 sec or so, then it will
               perform operation and move ahead.

explicit wait : explicit wait applies on specific element with given condition,
                it does not apply on all the element.
fluent wait :  Fluent wait it the explicit wait the configurable polling frequency of web element
static wait : static wait is the hard sleep, that script has to wait, till given period of
              sleep time.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
# implicit wait
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")

# explicit and fluent wait
wait = WebDriverWait(driver, 20, poll_frequency=2)


t1 = time.time()
try:
    login_popup_cls_btn = driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")
    login_popup_cls_btn.click()
except Exception as e:
    print(e)
    pass
t2 = time.time()
print("total time taken :", t2 -t1)


p1 = time.time()
try:
    from_city_field  = wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='From']//following-sibling::p")))
    from_city_field.click()
except Exception as e:
    print(e)
p2 = time.time()
print("total time wait :", p2 -p1)

driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input").send_keys("Mumbai")
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Mumbai, India']").click()
driver.find_element(By.XPATH, "//span[text()='To']//following-sibling::input").send_keys("Bangalore")
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Bengaluru, India']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Departure']//parent::div").click()
time.sleep(2)  # static wait
driver.find_element(By.XPATH, "//div[contains(@aria-label,'Dec 12')]").click()


time.sleep(5)
