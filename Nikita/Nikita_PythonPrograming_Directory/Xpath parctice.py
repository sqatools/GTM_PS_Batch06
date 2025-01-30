import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://www.saucedemo.com/")
#
# time.sleep(3)
#
# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
#
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("secret_sauce")
# time.sleep(5)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(10)


# //tagname[@attribute='value']
# //*[@attribute='value']
#
# //input[@data-testid='royal_email']
#//*[@data-testid='royal_email']
#
# // tagname[contains( @ attribute, 'attribute value')]
# // input[contains( @ placeholder, 'Pass')]
# // button[contains( @ data - testid, 'royal_login')]
