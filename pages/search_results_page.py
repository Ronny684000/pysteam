import time

from selenium.webdriver.common.by import By
from utils.constants import *
from browser.driver import Driver
from elements.dropdown import Dropdown
from elements.label import Label
from pages.abstract_page import AbstractPage
from utils.wait_utils import Wait
from utils.config_reader import *


class SearchResultsPage(AbstractPage):
    __key_element = Label("//div[@class='termcontainer']", "Key element")
    __result_price_locator = "//div[contains(@class,'col search_price_discount_combined')]"
    __dropdown_item_locator = "//a[@data-gpnav]"
    __sort_dropdown = Dropdown("//a[@id='sort_by_trigger']",
                               "//a[contains(@id, 'SC') and contains(., '{}')]", "Sort dropdown")
    __single_result = Label("//a[@id='sort_by_trigger']", "Result item")

    def __init__(self):
        super().__init__()

    def verify_item_list_not_empty(self):
        items = Driver.get_driver().find_elements(By.XPATH, self.__dropdown_item_locator)
        assert len(items) != 0, "Results list is empty"
        return SearchResultsPage()

    def sort_results(self):
        option_name = SORTING_OPTION_NAME_RU if get_browser_lang() == "ru" else SORTING_OPTION_NAME_EN
        self.__sort_dropdown.select_option(option_name)
        time.sleep(2)
        return SearchResultsPage()

    def __get_prices_list(self):
        return list(map(lambda x: x.get_attribute("data-price-final"),
                        Wait.wait_for_elements_presence(self.__result_price_locator)))

    def verify_sort_is_correct(self, games_to_check):
        prices = self.__get_prices_list()[0:games_to_check]
        print(prices)
        assert prices == sorted(prices, reverse=True), "Games are not sorted"
        return SearchResultsPage()

    def verify_page_is_loaded(self):
        assert self.__key_element.wait_for_display() is not None, "Page is not loaded"
        return SearchResultsPage()
