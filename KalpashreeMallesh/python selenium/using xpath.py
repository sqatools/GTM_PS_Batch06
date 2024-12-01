import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"//a[text()='Home']").click()
driver.find_element(By.XPATH,"//a[text()='Python Selenium']").click()
driver.find_element(By.XPATH,"//input[contains(@size, '10')]").send_keys("Online training")
driver.find_element(By.XPATH,"//input[contains(@type, 'submit')]").click()
time.sleep(10)
driver.close()