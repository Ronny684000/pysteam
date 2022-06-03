from abc import ABC, abstractmethod


class AbstractPage(ABC):
    pass

    @abstractmethod
    def verify_page_is_loaded(self):
        pass



