import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    request.cls.v1 = driver
