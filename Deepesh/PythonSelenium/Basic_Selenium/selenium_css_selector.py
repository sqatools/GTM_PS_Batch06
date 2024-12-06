"""
CSS Selector
1. by class name : we can mention the class with dot.
   .classname
   .post-title.entry-title

2. by id : we can mention id with # in css selector
      #fromcity
      #destcity

3. by attribute: We can mention attribute name in css selector syntax
      -> tagname[attibute='value']
      -> input[id=billing_name]
      -> h3[class='post-title entry-title']


4. by partial starting attribute value: In this selector we have to provide the starting partial
       value of any attribute.

     -> tagname[^attribute='partial value']
     -> h3[class^='post-title']
     -> input[id^='street']

5. element navigation.
     div>h1[align='center']
     ul>li>input[value=radio_123]



"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
# implicit wait
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Mumbai")
driver.find_element(By.CSS_SELECTOR, "#destcity").send_keys("Bangalore")
website_name= driver.find_element(By.CSS_SELECTOR, ".post-title.entry-title").text
print(website_name)
driver.find_element(By.CSS_SELECTOR, "input[id=billing_name]").send_keys("Mohit")


time.sleep(5)
