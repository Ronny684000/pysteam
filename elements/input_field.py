from selenium.webdriver.common.by import By

from browser.driver import Driver
from elements.abstract_element import AbstractElement


class InputField(AbstractElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_text(self, text_to_send):
        element = Driver.get_driver(). \
            find_element(By.XPATH, self.locator)
        self.click()
        element.send_keys(text_to_send)
