import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")

email_id = driver.find_element(By.XPATH, "//input[@name='email' and @data-testid='royal_email']")
email_id.send_keys("admin")

pass_word = driver.find_element(By.XPATH, "//div[@id='passContainer']/input[contains(@class, 'inputtext')]")
pass_word.send_keys("admin@123")

# create_new_account = driver.find_element(By.XPATH, "//a[contains(text(), 'new')]")
# create_new_account.click()

# forgot_password = driver.find_element(By.XPATH, "//a[contains(text(), 'Forgotten') or @name='email']")
# forgot_password.click()

login_btn = driver.find_element(By.XPATH, "//button[@name='login' and @data-testid='royal_login_button']")
login_btn.click()

time.sleep(2)


# driver.close()