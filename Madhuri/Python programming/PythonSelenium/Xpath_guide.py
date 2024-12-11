import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get( "https://www.facebook.com/login/" )
time.sleep(10)

driver.find_elements(By.XPATH,"//input[@data-testid='royal_email'").send_keys("admin")
driver.find_elements(By.XPATH,"//*@data-testid='royal_email").send_keys("admin@123")
time.sleep(5)


driver.close()