import abc
from app.domain.entity.page.page import Page

class PageRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, page: Page) -> bool:
        pass

    @abc.abstractmethod
    def find_by_path(self, path: str) -> Page:
        pass