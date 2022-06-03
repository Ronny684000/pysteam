import configparser


def get_browser_lang():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("BROWSER_SETTINGS", "lang")


def get_browser_name():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("BROWSER_SETTINGS", "browser_name")


def get_page_load_timeout():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("DRIVER_SETTINGS", "page_load_timeout")


def get_explicit_timeout():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("DRIVER_SETTINGS", "explicit_timeout")


def get_element_reload_timeout():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("DRIVER_SETTINGS", "element_reload_timeout")


def get_base_url():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser.get("TEST_SETTINGS", "base_url")
