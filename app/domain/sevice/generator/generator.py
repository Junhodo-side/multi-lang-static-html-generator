import abc
from collections import Generator
from app.domain.entity.page.page import Page
import app.domain.values.language as language


class Translator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def translate(self, input: str, src_lang: str, dest_lang: str) -> str:
        pass


class PageGenerator:
    def __init__(self, translator: Translator):
        self.translator = translator

    def generate(self, page: Page, dest_lang: str)-> Generator:
        if dest_lang == language.ALL_LANGUAGE:
            for lang_code in language.get_all_language_code():
                path = self.__generate_path__(src_path=page.path, language=lang_code)
                translated_html = self.translator.translate(input=page.html, src_lang=page.language,dest_lang=lang_code)
                if translated_html != None:
                    yield Page(html=translated_html, language=dest_lang, path=path)

        else:
            path = self.__generate_path__(src_path=page.path, language=dest_lang)
            translated_html = self.translator.translate(input=page.html, src_lang=page.language, dest_lang=dest_lang)
            yield Page(html=translated_html, language=dest_lang, path=path)

    def __generate_path__(self, src_path: str, language: str) -> str:
        path = src_path.split("/")
        return ("/".join(path[:len(path)-2])  + "/" + language + "/" + path[len(path)-1])