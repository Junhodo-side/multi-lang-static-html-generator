import click
import googletrans

from app.application.usecase.generate import GenerateUseCase
from app.infra.adapter.google_translation.google_traslator import GoogleTranslator
from app.infra.repository.page_repository import PageRepository
@click.group()
def cli():
    pass


@cli.command()
@click.option('--path', type=str, required=True)
@click.option('--src_lang', type=str, required=True)
@click.option('--dest_lang', type=str, required=True)
def generateFile(path: str, src_lang: str, dest_lang: str):
    generate_usecase = GenerateUseCase(translator=GoogleTranslator(), page_repository=PageRepository())
    generate_usecase.generate(path=path, src_lang=src_lang, dest_lang=dest_lang)

if __name__ == '__main__':
    generateFile()
