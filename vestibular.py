# Entrada
N = int(input())
gabarito = input()
respostas = input()

# Processamento
nota = 0
comparacao = list(zip(gabarito, respostas))
for gi, ri in comparacao:
    if gi == ri:
        nota += 1

# Resultado
print(nota)
