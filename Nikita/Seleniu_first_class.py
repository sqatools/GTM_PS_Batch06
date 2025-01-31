import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


"""
search_email = driver.find_element(By.NAME, "email")
print(search_email)
search_email.send_keys("nikita@gmail.com")

search_password = driver.find_element(By.NAME, "pass")
print(search_password)
search_password.send_keys("*******")

search_btn = driver.find_element(By.NAME, "login")
search_btn.click()
"""
search_pname = driver.find_element(By.NAME,"firstname")
print(search_pname)
search_pname.send_keys("Nikita")

#search_lastname = driver.find_element(By.Name, "firstname")
#print(search_lastname)
#search_lastname .send_keys("M")
time.sleep(5)

#by name
search_bname = driver.find_element(By.NAME,"birthday")
print(search_bname)
search_bname.send_keys("12/12/2024")

#id
search_bname = driver.find_element(By.NAME,"birthday")
print(search_bname)
search_bname.send_keys("12/12/2024")

time.sleep(10)
driver.close()