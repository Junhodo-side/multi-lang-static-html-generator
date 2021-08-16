from app.domain.sevice.generator.generator import Translator, PageGenerator
from app.domain.entity.page.repository.page_repository import PageRepository
from app.domain.entity.page.page import Page
class GenerateUseCase:
    def __init__(self, translator: Translator, page_repository: PageRepository):
        self.page_repository = page_repository
        self.generator = PageGenerator(translator)

    def generate(self, path:str, src_lang: str, dest_lang: str) -> int:
        page = self.page_repository.find_by_path(path=path, language=src_lang)
        cnt = 0
        for page in self.generator.generate(page=page, dest_lang=dest_lang):
            if self.page_repository.save(page):
                cnt += 1

        return cnt






