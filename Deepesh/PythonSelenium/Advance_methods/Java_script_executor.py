import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# https://www.w3schools.com/js/js_htmldom_document.asp

web_site_URL = driver.execute_script("return document.URL;")
print(web_site_URL)
website_title = driver.execute_script("return document.title;")
print(website_title)

from_city = driver.execute_script("return document.getElementById('fromcity');")
from_city.send_keys("Mumbai")

target_city = driver.execute_script("return document.getElementById('destcity');")
target_city.send_keys("Kolkata")
time.sleep(5)

domain_name = driver.execute_script("return document.domain;")
print(domain_name)

outerHeight = driver.execute_script("return window.outerHeight;")
print(outerHeight)
driver.close()
