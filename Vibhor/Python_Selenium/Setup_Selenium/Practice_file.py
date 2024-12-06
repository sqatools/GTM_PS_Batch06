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

login_popup_cls_btn = driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")
login_popup_cls_btn.click()
from_city_field  = wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='From']//following-sibling::p")))
from_city_field.click()
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
