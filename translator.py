from googletrans import Translator


class GoogleTranslator():
    def __init__(self, src='ee', dest='en'):
        self.translator = Translator()
        self.src = src
        self.dest = dest

    def translate(self, text):
        return self.translator.translate(text, src=self.src, dest=self.dest).text
