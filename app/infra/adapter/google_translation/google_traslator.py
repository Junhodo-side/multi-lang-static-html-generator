import google.cloud.translate_v2 as googletrans

class GoogleTranslator:
    def __init__(self):
        self.translator = googletrans.Client()

    def translate(self, input: str, src_lang: str, dest_lang: str) -> str:
        # result = self.translator.translate(text= input, src= src_lang, dest= dest_lang)
        try:
            result = self.translator.translate(values=input, target_language=dest_lang, source_language=src_lang)
            return result['translatedText']
        except:
            return None






