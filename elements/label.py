from browser.driver import Driver
from elements.abstract_element import AbstractElement


class Label(AbstractElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def get_text(self):
        return Driver.get_driver(). \
            find_element_by_xpath(self.locator).text
