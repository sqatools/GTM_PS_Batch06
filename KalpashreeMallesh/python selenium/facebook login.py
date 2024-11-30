import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
username = driver.find_element(By.NAME, "email")
print(username)
username.send_keys("kalpa_ec38@yahoo.in")
password =driver.find_element(By.NAME,"pass")
print(password)
password.send_keys("Sweetiepie")
login =driver.find_element(By.NAME,"login")
login.click()
time.sleep(20)
#driver.close()