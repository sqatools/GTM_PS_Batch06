import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
headless = False

opt = Options()
if headless:
    opt.add.argument("--headless")
    opt.add_argument("--window-size=800,600")
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--allow-running-insecure-contnet")

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"//a[text()='Home']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Python Selenium']").click()
driver.find_element(By.XPATH,"//input[contains(@size, '10')]").send_keys("Online training")
#driver.find_element(By.XPATH,"//input[contains(@type, 'subm')]").click()
driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(10)
driver.close()