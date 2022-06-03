from elements.abstract_element import AbstractElement


class Button(AbstractElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)
