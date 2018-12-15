import requests
import json
import math


def requisicao(titulo, pagina=1):
    try:
        req = requests.get(
            f"http://www.omdbapi.com/?apikey=c7160b0b&s={titulo}&type=movie&page={pagina}"
        )
        dicionario = json.loads(req.text)
        return dicionario
    except Exception:
        print("Erro na conexão")
        return None


def printar_detalhes(filme):
    print(filme)
    # print("Título: ", filme["Title"])
    # print("Ano: ", filme["Year"])
    # print("Diretor: ", filme["Director"])
    # print("Atores: ", filme["Actors"])
    # print("Nota: ", filme["imdbRating"])
    # print("Prêmios: ", filme["Awards"])
    # print("Poster: ", filme["Poster"])


sair = False
pagina = 1
while not sair:
    op = input('Escreva o nome de um filme ou "sair" para fechar: ')

    if str.lower(op) == "sair":
        sair = True
        print("Saindo...")
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print("Filme não encontrado")
        else:
            num_resultados = int(filme["totalResults"])
            num_paginas = math.ceil(num_resultados / 10)
            for i in range(1, num_paginas+1):
                filme = requisicao(op, i)
                # VER O QUE TÁ DANDO PAU AQUI. TÁ ENTRANDO NO LOOP MAIS VEZES DO QUE DEVERIA
                for i in filme["Search"]:
                    # printar_detalhes(filme["Search"][i])
                    print(filme["Search"][i])
                    printar_detalhes(filme["Search"][i])


            # for i in range(int(filme["totalResults"])):
            #     # printar_detalhes(filme["Search"][i])
            #     print(filme["Search"][i])
