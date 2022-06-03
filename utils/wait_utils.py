import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser.driver import Driver
from utils.config_reader import get_explicit_timeout, get_element_reload_timeout


class Wait:
    def __init__(self):
        pass

    @classmethod
    def wait_for_elements_presence(cls, locator):
        WebDriverWait(Driver.get_driver(), get_explicit_timeout()).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, locator)))
        time.sleep(int(get_element_reload_timeout()))
        return WebDriverWait(Driver.get_driver(), get_explicit_timeout()).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, locator)))


