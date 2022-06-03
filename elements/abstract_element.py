import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser.driver import Driver
from utils.config_reader import get_explicit_timeout


class AbstractElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def wait_for_display(self):
        try:
            return WebDriverWait(Driver.get_driver(), get_explicit_timeout()).until(
                expected_conditions.presence_of_element_located((By.XPATH, self.locator)))
        except TimeoutError:
            logging.error("Element is not displayed")

    def click(self):
        element = Driver.get_driver(). \
            find_element(By.XPATH, self.locator)
        self.wait_for_display()
        element.click()
