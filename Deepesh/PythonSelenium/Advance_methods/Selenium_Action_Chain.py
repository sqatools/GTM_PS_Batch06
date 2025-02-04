import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

"""
Alert class only works with java script popup alert, there you can not find element.
"""

driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

def hover_to_element():
    menu_option = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']")
    action = ActionChains(driver)
    action.move_to_element(menu_option)
    action.perform()
    time.sleep(3)

    demo_testing_site = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='Demo Testing Site']//parent::a")
    action.move_to_element(demo_testing_site)
    action.perform()
    time.sleep(5)

    alert_box = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='AlertBox']//parent::a")
    action.move_to_element(alert_box)
    action.click(alert_box)
    action.perform()

    time.sleep(5)


#hover_to_element()

def drag_and_drop_images():
    iframe_elm = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_elm)

    image1 = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    target_elem = driver.find_element(By.ID, "trash")
    action = ActionChains(driver)
    action.drag_and_drop(image1, target_elem)
    action.perform()
    time.sleep(5)

    images_headers = ['High Tatras 2', 'High Tatras 3', 'High Tatras 4']
    for header in images_headers:
        image_elem = driver.find_element(By.XPATH, f"//h5[text()='{header}']//parent::li")
        action.drag_and_drop(image_elem, target_elem)
        action.perform()
        time.sleep(3)


    time.sleep(5)

#drag_and_drop_images()
def scroll_to_element_and_click():
    alert_box  = driver.find_element(By.XPATH, "//div[@id='footer']//a[text()='AlertBox']")
    action = ActionChains(driver)
    action.scroll_to_element(alert_box)
    action.click(alert_box)
    action.perform()
    time.sleep(10)

# scroll_to_element_and_click()
def scroll_to_specific_position():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    action = ActionChains(driver)
    action.scroll_by_amount(100, 5000)
    action.perform()
    time.sleep(10)

#scroll_to_specific_position()

def context_or_right_click():
    # pip install pyautogui
    import pyautogui
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    home_tab = driver.find_element(By.XPATH, "//div[@class='widget PageList']//a[text()='Home']")
    action = ActionChains(driver)
    action.context_click(home_tab)
    action.perform()
    time.sleep(2)
    pyautogui.press("up")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(5)

context_or_right_click()

driver.close()
