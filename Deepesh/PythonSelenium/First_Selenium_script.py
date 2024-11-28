"""
install selenium with command
pip install selenium
pip : python package manager
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in")
time.sleep(5)

driver.close()
