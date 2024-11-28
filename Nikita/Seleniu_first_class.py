import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")
time.sleep(5)


search_email = driver.find_element(By.NAME, "email")
print(search_email)
search_email.send_keys("nikita@gmail.com")

search_password = driver.find_element(By.NAME, "pass")
print(search_password)
search_password.send_keys("*******")




time.sleep(30)


driver.close()

