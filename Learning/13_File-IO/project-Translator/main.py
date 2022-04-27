# Project-Translator


# Using py-translate


















"""
# Using 'translate' module...
from translate import Translator
translator = Translator(to_lang="es")


try:
    with open("./english.txt", "r") as lang_en:
        english_text = lang_en.read()
        translation = translator.translate(english_text)
        with open("./spanish.txt", "w") as lang_es:
            lang_es.write(translation)

except FileNotFoundError as e:
    print("Sorry, File Not Found :(")


# This sucker has usage limit!
"""




