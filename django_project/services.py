import json
import sys
from urllib import request, parse




def get_translate(text, source, target):
    url = 'http://127.0.0.1:5000/translate'
    params = {"q": text, "source": source, "target": target}
    url_params = parse.urlencode(params)

    r = request.Request(url, data=url_params.encode())
    response = request.urlopen(r)
    response_str = response.read().decode()
    return json.loads(response_str)["translatedText"]
    
    
    