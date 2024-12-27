from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.edge.options import Options as edge_option
from resources.session_data import *


class WDFactory:
    """
    Webdriver Factory
    """
    def __init__(self, browser, headless=False):
        self.browser = browser
        self.headless = headless

    def get_driver_instance(self):
        global driver
        if self.browser.lower() == 'chrome':
            opt = chrome_option()
            if self.headless:
                opt.add_argument("--headless")
            opt.add_argument("--window-size=800,600")
            opt.add_argument("--disable-popup-blocking")
            opt.add_argument("--allow-running-insecure-content")
            opt.add_argument("--ignore-certificate-errors")
            prefs = {"download.default_directory": download_path,
                     "download.prompt_for_download": False,
                     "safebrowsing_for_trusted_source_enabled": True,
                     "safebrowsing.enabled": False
                     }
            opt.add_experimental_option("prefs", prefs)
            opt.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=opt)

        elif self.browser.lower() == 'firefox':
            opt = firefox_option()
            if self.headless:
                opt.add_argument("--headless")
            driver = webdriver.Firefox(options=opt)

        elif self.browser.lower() == 'edge':
            opt = edge_option()
            if self.headless:
                opt.add_argument("--headless")
            driver = webdriver.Edge(options=opt)

        driver.maximize_window()
        return driver
