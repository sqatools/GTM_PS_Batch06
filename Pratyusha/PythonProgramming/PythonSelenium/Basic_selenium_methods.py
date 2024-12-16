import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

def get_website_title():
    print("Website title: ", driver.title)

def get_current_url():
    driver.get("https://www.facebook.com")
    print("Current URL: ", driver.current_url)
    driver.back()
    time.sleep(5)
    print("Old URL: ", driver.current_url)
    driver.forward()
    time.sleep(5)
    print("New URL: ", driver.current_url)
    driver.back()
    time.sleep(5)

    # driver.get("https://sqatools.in/dummy-booking-website/")

def refresh_page():
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.refresh()
    time.sleep(3)

def check_element_status():
    first_name = driver.find_element(By.NAME, "firstname")
    print("Check element is displayed: ", first_name.is_displayed())
    print("Check element is enabled: ", first_name.is_enabled())

    whatsapp_radio = driver.find_element(By.ID, "whatsapp")
    print("Is whatsapp radio selected before click: ", whatsapp_radio.is_selected())
    whatsapp_radio.click()
    time.sleep(2)
    print("Is whatsapp radio selected before click: ", whatsapp_radio.is_selected())

    checkbox = driver.find_element(By.XPATH, "//td[text()='6002']//parent::tr/td/input")
    print("Is checkbox selected before click: ", checkbox.is_selected())
    checkbox.click()
    time.sleep(2)
    print("Is checkbox selected after click: ", checkbox.is_selected())

def get_attribute():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    link_element = driver.find_element(By.XPATH, "//a[contains(text(), '  What is Software Testing')]")
    print(link_element.get_attribute("href"))

    name_list = ['Unit Testing', 'Smoke Testing', 'System Testing', 'Load Testing']
    for name in name_list:
        elem = driver.find_element(By.XPATH, f"//a[contains(text(), '{name}')]")
        print(elem.get_attribute("href"))

def get_testing_types():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    types_of_func_and_nonfunc = driver.find_elements(By.XPATH, "//*[text() = 'Functional Testing']//ancestor::ul[@class='ullist']//ul[1]//child::li//a[contains(text(), 'Testing')]")
    for type in types_of_func_and_nonfunc:
        print(f"{type.text}", ":", type.get_attribute("href"))

# get_website_title()
# get_current_url()
# refresh_page()
# check_element_status()
# get_attribute()
get_testing_types()

driver.close()
