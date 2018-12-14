P, R = input().split()

P = int(P)
R = int(R)

if P == 0:
    resul = "C"
else:
    if R == 0:
        resul = "B"
    else:
        resul = "A"

print(resul)
