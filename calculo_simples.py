peca_1 = input().split()
peca_2 = input().split()
preco = 0

for pi, p in enumerate(peca_1):
    peca_1[pi] = float(p)

for pi, p in enumerate(peca_2):
    peca_2[pi] = float(p)

preco = peca_1[1] * peca_1[2] + peca_2[1] * peca_2[2]

# preco = peca_1
# print(type(peca_1[0]))

print("VALOR A PAGAR: R$ {:.2f}" . format(preco))
