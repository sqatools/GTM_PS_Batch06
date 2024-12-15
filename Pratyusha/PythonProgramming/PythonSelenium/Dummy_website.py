import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

website_name = driver.find_element(By.XPATH, "//h3[contains(text(), 'Dummy Website')]").text
print(website_name)
time.sleep(2)

# TAG_NAME
header = driver.find_element(By.TAG_NAME, "h1")
print("header value: ", header.text)
time.sleep(2)

choose_option = driver.find_element(By.XPATH, "//div[@align='left']/ul/li[2]//following-sibling::li/input[@value='radio_558']")
choose_option.click()
time.sleep(2)

first_name = driver.find_element(By.XPATH, "(//*[@name='firstname'])[1]")
first_name.send_keys("Pratyusha")
time.sleep(2)

last_name = driver.find_element(By.XPATH, "//input[@id='firstname']//following::input[@id='firstname']")
last_name.send_keys("Nalam")
time.sleep(2)

# ID Locator
dob_elem = driver.find_element(By.ID, "birthday")
dob_elem.send_keys("08/26/2000")
time.sleep(2)

choose_gender = driver.find_element(By.XPATH, "//input[@id='female']")
choose_gender.click()
time.sleep(2)

print("Choose gender is selected: ", choose_gender.is_selected())

one_way_or_round_trip = driver.find_element(By.XPATH, "//input[@id='oneway']//following::input[@id='roundtrip']")
one_way_or_round_trip.click()
# //input[@id='oneway']//following::input[contains(text(), 'Round')]

# Name Locator
# frm_city = driver.find_element(By.NAME, "fromcity")
frm_city = driver.find_element(By.XPATH, "//input[@name='fromcity']")
frm_city.send_keys("Pune")
time.sleep(2)

dest_city = driver.find_element(By.XPATH, "//input[@id='destcity']")
dest_city.send_keys("Maharashtra")
time.sleep(2)

dept_date = driver.find_element(By.XPATH, "//input[@name='departdate']")
dept_date.send_keys("12/04/2024")
time.sleep(2)

return_date = driver.find_element(By.XPATH, "//*[@name='returndate']")
return_date.send_keys("12/04/2024")
time.sleep(2)

visa_date = driver.find_element(By.XPATH, "//input[contains(@name, 'visadate')]")
visa_date.send_keys("12/04/2024")
time.sleep(2)

receive_platform = driver.find_element(By.XPATH, "//input[contains(@id, 'whatsapp')]")
receive_platform.click()

print("Ticket receiving platform is selected: ", receive_platform.is_selected())

billing_address_email = driver.find_element(By.XPATH, "//input[@id='billing_name']//following::input[@id='billing_email']")
billing_address_email.send_keys("admin123@gmail.com")

street_address = driver.find_element(By.XPATH, "//input[@id='street_address2']//preceding-sibling::input[@id='street_address1']")
street_address.send_keys("dummy street")
time.sleep(2)

city_name = driver.find_element(By.XPATH, "//tr/td[contains(text(), '6001')]//following-sibling::td[text()='Mumbai']")
print(city_name.text)

time.sleep(2)
"""# Link Text
python_selenium_link = driver.find_element(By.LINK_TEXT, "Python Selenium")
python_selenium_link.click()
time.sleep(3)
# PARTIAL_LINK_TEXT
pytest_framework = driver.find_element(By.PARTIAL_LINK_TEXT, "Pytest")
pytest_framework.click()"""


# time.sleep(5)

driver.close()