from abc import ABC

from elements.button import Button
from elements.input_field import InputField
from elements.label import Label
from pages.abstract_page import AbstractPage
from pages.search_results_page import SearchResultsPage


class MainMenuPage(AbstractPage, ABC):
    __key_element = Label("//video", "Key element")
    __search_field = InputField("//input[@id='store_nav_search_term']", "Search input field")
    __search_button = Button(
        "//img[contains(@src, 'https://store.cloudflare.steamstatic.com/public/images/blank.gif')]",
        "Search button")

    def __init__(self):
        super().__init__()

    def find_game(self, text):
        self.__search_field.send_text(text)
        self.__search_button.click()
        return SearchResultsPage()

    def verify_page_is_loaded(self):
        assert self.__key_element.wait_for_display() is not None, "Page is not loaded"
        return MainMenuPage()
