# Input
T = int(input())
dias = []

for i in range(T):
    dias.append(input().split())

# Processing
garrafas = []

for i in range(T):
    compradas = int(dias[i][0])
    vazias = int(dias[i][1])
    q, r = divmod(compradas, vazias)
    quantidade = q + r
    garrafas.append(quantidade)

# Output
for i in garrafas:
    print(i)
