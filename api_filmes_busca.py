import requests
import json
import math


def requisicao(titulo):
    try:
        resul = []

        req = requests.get(
            f"http://www.omdbapi.com/?apikey=c7160b0b&s={titulo}&type=movie"
        )
        dicionario = json.loads(req.text)
        resul.append(dicionario)

        num_resultados = int(dicionario["totalResults"])
        num_paginas = math.ceil(num_resultados / 10)

        if num_paginas > 1:
            for i in range(2, num_paginas + 1):
                req = requests.get(
                    f"http://www.omdbapi.com/?apikey=c7160b0b&s={titulo}&type=movie&page={i}"
                )
                dicionario = json.loads(req.text)
                resul.append(dicionario)
        return resul
    except Exception:
        print("Erro na conexão")
        return None


def printar_detalhes(paginas):
    for pagina in paginas:
        for filme in pagina["Search"]:
            print("Título: ", filme["Title"])
            print("Ano: ", filme["Year"])
            print("IMDb ID: ", filme["imdbID"])
            print("Poster: ", filme["Poster"])
            print()


sair = False
while not sair:
    op = input(
        f'Escreva o nome de um filme para realizar a busca ou "sair" para fechar: '
    )

    if str.lower(op) == "sair":
        sair = True
        print("Saindo...")
    else:
        resultado = requisicao(op)
        if len(resultado) == 0:
            print("Filme não encontrado")
        else:
            printar_detalhes(resultado)
