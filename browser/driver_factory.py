from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @classmethod
    def get_webdriver(cls, browser_name, lang):
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--lang=" + lang)
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
