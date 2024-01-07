from ..v1.papagopy import Papagopy
papago = Papagopy()

def translate_v1(text, language_code):
    return papago.translate(text, language_code)