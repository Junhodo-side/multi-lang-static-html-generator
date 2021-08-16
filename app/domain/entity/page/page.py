import abc
# page is aggregate root(entry point)
class Page:
    def __init__(self, path:str, html: str, language: str):
        self.path = path
        self.language = language
        self.html = html