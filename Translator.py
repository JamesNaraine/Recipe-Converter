from googletrans import Translator


def Translating(targetText, source_language, dest_language):
    translator = Translator()
    translated = translator.translate(targetText, src = source_language, dest = dest_language)
    return translated.text
    # Output = GoogleTranslator(source='auto', target=language).translate(targetText)
    # return Output

# langs_list = GoogleTranslator().get_supported_languages()

# print(langs_list)


print(Translating("Luke is such a nerd","en","de"))