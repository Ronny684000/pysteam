import pytest

from utils.config_reader import *
from browser.browser import Browser


@pytest.fixture(autouse=True)
def handle_browser():
    Browser.maximise()
    Browser.set_page_load_timeout(get_page_load_timeout())
    Browser.go_to_url(get_base_url())
    yield
    Browser.quit()
