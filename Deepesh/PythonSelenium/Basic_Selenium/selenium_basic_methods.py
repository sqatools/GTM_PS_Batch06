"""
get website title
get website URL
browser forward and back operation
browser refresh
check element is displayed
check element is selected
check element is enabled
get attribute of element
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")


def get_website_title():
    print("website title :", driver.title)


def get_current_url():
    # navigate to facebook.com
    driver.get("https://www.facebook.com")
    print("website title :", driver.title)

    # get current URL
    print("current_url :", driver.current_url)
    driver.back()
    time.sleep(5)

    print("old current_url :", driver.current_url)
    driver.forward()
    time.sleep(5)
    print("website title :", driver.title)

    print("new current_url :", driver.current_url)
    driver.forward()
    time.sleep(5)
    print("website title :", driver.title)

    #driver.get("https://sqatools.in/dummy-booking-website/")

    # re-load the page with refresh method
    driver.refresh()

    time.sleep(3)

def refresh_page():
    driver.refresh()
    time.sleep(5)


def check_element_status():
    from_city_element = driver.find_element(By.NAME, "fromcity")
    # is_displayed look for element is visible on website
    print("check element is displayed :", from_city_element.is_displayed())

    # is_enabled look for element is visible and also enabled to perform operation.
    print("check element is enabled :", from_city_element.is_enabled())

    whatsApp_radio = driver.find_element(By.ID, "whatsapp")
    print("whatApp radio button is selected before click:", whatsApp_radio.is_selected()) # False
    whatsApp_radio.click()
    print("whatApp radio button is selected after click:", whatsApp_radio.is_selected()) # False

    check_box = driver.find_element(By.XPATH, "//td[text()='6001']//parent::tr//input")
    print("before click checkbox :", check_box.is_selected())
    check_box.click()
    time.sleep(5)
    print("after click checkbox :", check_box.is_selected())


def get_attribute_value():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    link_element = driver.find_element(By.XPATH, "//a[contains(text(),'What is Software Testing')]")
    print(link_element.get_attribute("href"))

    name_list = [
        'Unit Testing', 'Smoke Testing', 'Monkey Testing', 'Ad-hoc Testing'
    ]

    for name in name_list:
        elem = driver.find_element(By.XPATH, f"//a[contains(text(),'{name}')]")
        print(elem.get_attribute("href"))

    """
    https://automationbysqatools.blogspot.com/2020/07/software-testing.html
    https://automationbysqatools.blogspot.com/2020/08/unit-testing.html
    https://automationbysqatools.blogspot.com/2020/08/smoke-testing.html
    https://automationbysqatools.blogspot.com/2020/09/monkey-testing.html
    https://automationbysqatools.blogspot.com/2020/07/adhoc-testing.html
    """

#get_website_title()
#get_current_url()
#refresh_page()
# check_element_status()
get_attribute_value()
driver.close()
