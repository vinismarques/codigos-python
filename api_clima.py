import requests
import json
import pytemperature


def consultar_clima(city):
    try:
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=75ba75b9f3c7017093a7b941dcf19a81"
        )
        return json.loads(req.text)
    except Exception:
        print(f"Não foi possível encontrar a cidade desejada.")
        return json.loads(req.text)


def printar_detalhes(clima):
    cidade = clima['name']
    temperatura = pytemperature.k2c(clima['main']['temp'])
    print(f"A temperatura em {cidade} neste momento é de {temperatura:.1f} graus Celsius.")


print("Este programa irá consulta informações sobre o clima de cidades.")
sair = False
while not sair:
    op = input('Escreva o nome de uma cidade ou "sair" para fechar: ')

    if str.lower(op) == "sair":
        sair = True
        print("Saindo...")
    else:
        clima = consultar_clima(op)
        if clima['cod'] != 200:
            print(f"Código do erro: '{clima['cod']}'. Mensagem: '{clima['message']}'.")
        else:
            printar_detalhes(clima)
