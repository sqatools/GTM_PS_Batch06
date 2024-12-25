import pytest
from datetime import datetime
from selenium import webdriver


@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield  # teardown
    driver.close()


def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.now().strftime('%d-%m-%Y_%H_%M_%S')
        config.option.log_file = "logs/" + timestamp + "_execution.log"
