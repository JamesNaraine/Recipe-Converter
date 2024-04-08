from deep_translator import GoogleTranslator



def Translating(targetText, language):
    Output = GoogleTranslator(source='auto', target=language).translate(targetText)
    return Output
   