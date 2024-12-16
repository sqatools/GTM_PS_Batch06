import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
"""
Alert class only works with java script popup alert, there you can not find element.
"""

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


def alert_box1():
    alert_box_elem = driver.find_element(By.ID, "btnShowMsg")
    alert_box_elem.click()
    time.sleep(2)
    alert_box = Alert(driver)
    print("alert box msg :", alert_box.text)
    alert_box.accept()

#alert_box1()

def confirm_box():

    confirm_box_elem = driver.find_element(By.ID, "button")
    confirm_box_elem.click()
    time.sleep(2)
    alert2 = Alert(driver)
    # Accept the alert and verify
    """
    alert2.accept()
    msg = driver.find_element(By.ID, "demo")
    assert msg.text == "You pressed OK!"
    """

    # Dismiss the alert
    print(alert2.text)
    alert2.dismiss()
    msg = driver.find_element(By.ID, "demo")
    assert msg.text == "You pressed Cancel!"


#confirm_box()

def prompt_box():
    prompt_box_elem = driver.find_element(By.ID, "promptbtn")
    prompt_box_elem.click()
    time.sleep(2)
    alert3 = Alert(driver)
    input_val = "GrowTechMind"
    alert3.send_keys(input_val)
    time.sleep(2)
    alert3.accept()

    msg = driver.find_element(By.ID, "prompt")
    print("UI msg :", msg.text)
    assert msg.text == f"Hello {input_val}! How are you today?"

prompt_box()

