from browser.driver_factory import DriverFactory
from utils.config_reader import *


class Driver:
    __instance = None

    @classmethod
    def get_driver(cls):
        if cls.__instance is None:
            cls.__instance = DriverFactory.get_webdriver(get_browser_name(), get_browser_lang())
        return cls.__instance

    @classmethod
    def close_driver(cls):
        cls.__instance.quit()
        cls.__instance = None
