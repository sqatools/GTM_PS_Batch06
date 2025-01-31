import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Sauce Labs Bike Light").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
driver.find_element(By.XPATH, "//div[@id = 'shopping_cart_container']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='checkout']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Pratyusha")
driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Nalam")
driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']").send_keys("432 534")
driver.find_element(By.XPATH, "//input[@id='continue']").click()
time.sleep(3)
driver.find_element(By.ID, "finish").click()
time.sleep(3)
