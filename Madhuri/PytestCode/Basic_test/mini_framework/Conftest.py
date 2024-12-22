import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicity_wait(10)
    request.cls.driver = driver
    yield # teardown
    driver.close()

