# Tradutor
## Esse projeto é uma API que faz requisições no LibreTranslate, que eu subi localmente e consumi pela API que ele disponibiliza. Os dados dessas requisições são coletadas através de uma interface criada em Vue js.
Foi uilizado o repositório gratuíto LibreTranslate https://github.com/ssut/py-googletrans, dentro da própria documentação já tem o passo a passo para clonar e buildar o repositório.
### Esse método faz a requisição para API do LibreTranslate.
Coloquei essa função dentro '.django_project/services.py', onde esse arquivo fica responsável por fazer requisições para outras APIs. 


    def get_translate(text, source, target):
        url = 'http://127.0.0.1:5000/translate'
        params = {"q": text, "source": source, "target": target}
    
        url_params = parse.urlencode(params)
        r = request.Request(url, data=url_params.encode())
        response = request.urlopen(r)
        response_str = response.read().decode()
        return json.loads(response_str)["translatedText"]


## A API foi construída em Django Rest Framework (DRF)
Caso você queira clona o repositório.

    git clone git@github.com:Denisdev2002/tradutor.git

Entre no diretório raiz

    cd Treino_api/django_project
Instale as dependências.

    pip install requeriments.txt 


