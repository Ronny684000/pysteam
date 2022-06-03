from browser.driver import Driver


class Browser:

    @classmethod
    def switch_to_window(cls, window_name):
        Driver.get_driver().switch_to_window(window_name)

    @classmethod
    def switch_to_frame(cls, frame_name):
        Driver.get_driver().switch_to_frame(frame_name)

    @classmethod
    def switch_to_default(cls):
        Driver.get_driver().switch_to_default_content()

    @classmethod
    def switch_to_alert(cls):
        return Driver.get_driver().switch_to_alert()

    @classmethod
    def go_to_url(cls, url):
        Driver.get_driver().get(url)

    @classmethod
    def back(cls):
        Driver.get_driver().back()

    @classmethod
    def forward(cls):
        Driver.get_driver().forward()

    @classmethod
    def maximise(cls):
        Driver.get_driver().maximize_window()

    @classmethod
    def quit(cls):
        Driver.close_driver()

    @classmethod
    def set_page_load_timeout(cls, timeout):
        Driver.get_driver().set_page_load_timeout(timeout)
