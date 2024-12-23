import time

# import webdriver from selenium
from selenium import webdriver

# import By class to get all locator type
from selenium.webdriver.common.by import By

# Open any specific browser
driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

# Set timeout for web element
driver.implicitly_wait(10)

# Open the website in the browser
driver.get("https://www.redbus.com/")

driver.find_element(By.ID, "src").send_keys("Mumbai, Maharashtra")
time.sleep(2)
driver.find_element(By.ID, "dest").send_keys("Banaglore, Karnataka")
time.sleep(2)
Start_date=driver.find_element(By.XPATH, "//input[@id='onward_cal']").click()
Start_date.send_keys("15-Dec-2024")
time.sleep(20)




#driver.find_element(By.XPATH, "//*[contains(text(), 'Thane West, Mumbai')]").click()
#time.sleep(60)

