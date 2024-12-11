import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

# default header email
header_email = driver.find_element(By.XPATH, "//div[@class='header_mail']")
print(header_email.text)

iframe_element = driver.find_element(By.NAME, "globalSqa")
driver.switch_to.frame(iframe_element)

# iframe header email
header_email_iframe = driver.find_element(By.XPATH, "//div[@class='header_mail']")
print(header_email_iframe.text)

# click to menu item
menu_item = driver.find_element(By.ID, "mobile_menu_toggler")
menu_item.click()
time.sleep(3)

# switch to default content
driver.switch_to.default_content()
about_elem = driver.find_element(By.XPATH, "//li//a[text()='About']")
about_elem.click()

time.sleep(5)

