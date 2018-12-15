import requests
import json


def requisicao(titulo):
    try:
        req = requests.get(
            f"http://www.omdbapi.com/?apikey=c7160b0b&t={titulo}&type=movie"
        )
        dicionario = json.loads(req.text)
        return dicionario
    except Exception:
        print("Erro na conexão")
        return None


def printar_detalhes(filme):
    print("Título: ", filme["Title"])
    print("Ano: ", filme["Year"])
    print("Diretor: ", filme["Director"])
    print("Atores: ", filme["Actors"])
    print("Nota: ", filme["imdbRating"])
    print("Prêmios: ", filme["Awards"])
    print("Poster: ", filme["Poster"])


sair = False
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
            printar_detalhes(filme)
