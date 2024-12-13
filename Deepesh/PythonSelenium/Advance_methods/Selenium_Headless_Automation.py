import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
headless = False


opt = Options()
if headless:
    opt.add_argument("--headless")
opt.add_argument("--window-size=800,600")
opt.add_argument("--disable-popup-blocking")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--ignore-certificate-errors")
prefs = {"download.default_directory": r"E:\Filesdata\batch06\\",
         "download.prompt_for_download": False,
         "safebrowsing_for_trusted_source_enabled": True,
         "safebrowsing.enabled": False
         }
opt.add_experimental_option("prefs", prefs)
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
driver.maximize_window()

# implicit wait
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
driver.find_element(By.ID, "destcity").send_keys("Kolkata")

driver.find_element(By.ID, "eamil").click()
driver.find_element(By.ID, "billing_name").send_keys("John Doe")

var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
driver.save_screenshot(f"{var}_dm_website.png")

driver.get("https://www.python.org/downloads/")

time.sleep(5)
download_btn = driver.find_element(By.XPATH, "//div[@class='download-os-windows']//a[text()='Download Python 3.13.1']")
download_btn.click()
time.sleep(20)
driver.close()
