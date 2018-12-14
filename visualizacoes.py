# Entrada de dados
N = int(input())

visitas = []
for i in range(N):
    A = int(input())
    visitas.append(A)

# Processamento
soma = 0
for i, v in enumerate(visitas):
    soma += v
    if soma >= 1000000:
        print(i+1)
        break
