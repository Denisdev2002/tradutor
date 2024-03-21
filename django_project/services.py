import os
import requests
# from display.views import TranslationAPIView


def get_translate(text, language, target_language):
    url = 'http://127.0.0.1:5000/translate'
    data = {
        "q": text,
        "source": language,
        "target": target_language
    }
    r = requests.post(url, json=data)
    if r.status_code == 200:
        translated_text = r.json().get['translated_text']
        return translated_text
    else:
        return "Erro ao traduzir o texto"

translation = get_translate("Hello, my name is","en","pt")
print(translation)
   
    
    