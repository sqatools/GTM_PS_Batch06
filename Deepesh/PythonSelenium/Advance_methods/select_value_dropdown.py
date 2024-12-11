import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


def get_value_select_dropdown():
    pass_dd = driver.find_element(By.ID, "admorepass")
    select1 = Select(pass_dd)
    # select1.select_by_index(2)
    # select1.select_by_value("4")
    select1.select_by_visible_text("Add 1 more passenger (100%)")
    time.sleep(3)
    driver.save_screenshot("addmore_pass.png")

    country_dd = driver.find_element(By.ID, "billing_country")
    country_dd.screenshot("country_ddp_element.png")
    select2 = Select(country_dd)
    select2.select_by_visible_text("India")
    driver.save_screenshot("country_dropdown.png")
    time.sleep(5)


#get_value_select_dropdown()


def search_dropdown():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/dropdown.html")
    search_input = driver.find_element(By.ID, "browser")
    search_input.send_keys("Chr")
    time.sleep(2)
    # Use keyboard key to select the value in the dropdown
    #data_list = driver.find_element(By.ID, "browsers")
    search_input.send_keys(Keys.ARROW_DOWN)
    time.sleep(3)
    search_input.send_keys(Keys.ENTER)
    time.sleep(5)

search_dropdown()
