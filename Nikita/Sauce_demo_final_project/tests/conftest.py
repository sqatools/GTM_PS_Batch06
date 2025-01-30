import pytest
import os
from datetime import datetime
from base.webdriver_factory import WDFactory
from resources.session_data import *


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default=None, help='browser to launch')
    parser.addoption("--headless", action='store', default=None, help='GUI execution option')


@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    if browser is not None and headless is not None:
        wd = WDFactory(browser=browser, headless=bool(headless))
    else:
        wd = WDFactory(browser='chrome')
    driver = wd.get_driver_instance()
    request.cls.driver = driver
    yield  # teardown
    driver.close()


def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.now().strftime('%d-%m-%Y_%H_%M_%S')
        log_filename = timestamp + "_execution.log"
        log_file_path = os.path.join(log_folder_path, log_filename)
        config.option.log_file = log_file_path
