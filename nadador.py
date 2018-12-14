competidores = []
competidores.append(int(input()))
competidores.append(int(input()))
competidores.append(int(input()))

colocacao = sorted(competidores)
for i in colocacao:
    if i == competidores[0]:
        print("1")
    elif i == competidores[1]:
        print("2")
    else:
        print("3")
