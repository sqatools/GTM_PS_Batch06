import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")

email_id = driver.find_element(By.NAME, "email")
email_id.send_keys("Admin")

pass_word = driver.find_element(By.ID, "pass")
pass_word.send_keys("admin@123")

login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
time.sleep(5)


driver.close()