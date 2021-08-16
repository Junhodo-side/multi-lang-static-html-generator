from app.domain.entity.page.page import Page
import os

class PageRepository:
    def save(self, page: Page) -> bool:
        os.makedirs(os.path.dirname(page.path), exist_ok=True)
        with open(page.path, "w") as f:
            f.write(page.html)
            f.close()

    def find_by_path(self, path: str, language: str) -> Page:
        with open(path, 'r') as file:
            html = file.read()
            return Page(
                html=html,
                path=path,
                language=language
            )