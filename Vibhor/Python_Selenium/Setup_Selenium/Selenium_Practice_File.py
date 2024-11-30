import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(5)
search_field = driver.find_element(By.XPATH, "(//*[contains(@value,'radio_67')])").click()
search_field = driver.find_element(By.ID, "firstname")
search_field.send_keys("Vibhor")
search_field = driver.find_element(By.XPATH, "(//*[contains(@id,'firstname')])[2]")
search_field.send_keys("Khare")
search_field = driver.find_element(By.NAME, "birthday")
search_field.send_keys("23-03-1987")
search_button = driver.find_element(By.ID, "male")
search_button.click()
search_button = driver.find_element(By.ID, "oneway")
search_button.click()
search_field = driver.find_element(By.NAME, "fromcity")
search_field.send_keys("Lucknow")
search_field = driver.find_element(By.NAME, "destcity")
search_field.send_keys("Delhi")
search_field = driver.find_element(By.ID, "visadate")
search_field.send_keys("12-10-2024")
search_field = driver.find_element(By.XPATH, "(//*[contains(@type,'radio')])[10]").click()
billing_field = driver.find_element(By.ID, "billing_name")
billing_field.send_keys("Vibhor Khare")
search_field = driver.find_element(By.ID, "billing_phone")
search_field.send_keys("8884440484")
search_field = driver.find_element(By.ID, "billing_email")
search_field.send_keys("vibhorkhare23gmail.com")
search_field = driver.find_element(By.ID, "billing_address")
search_field.send_keys("Skyville Apartment Lucknow")
search_field = driver.find_element(By.ID, "billing_country")
search_field.send_keys("India")
search_field = driver.find_element(By.NAME, "postcode")
search_field.send_keys("226028")
search_field = driver.find_element(By.ID, "street_address1")
search_field.send_keys("Chinhat Lucknow")
search_field = driver.find_element(By.ID, "ContactForm2_contact-form-name")
search_field.send_keys("Vibhor Khare")
search_field = driver.find_element(By.NAME, "email")
search_field.send_keys("vibhorkhare23@gmail.com")
search_field = driver.find_element(By.ID, "ContactForm2_contact-form-email-message")
search_field.send_keys("Learning Python Automation testing")
search_field = driver.find_element(By.XPATH, "//*[contains(@id, 'admorepass')]/option[2]")
search_field.click()
time.sleep(5)
python_selenium_link = driver.find_element(By.LINK_TEXT, "Python Selenium")
python_selenium_link.click()
time.sleep(10)
# driver.close()