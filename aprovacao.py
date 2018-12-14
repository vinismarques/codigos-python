A, B = input().split()
A = float(A)
B = float(B)

media = (A+B)/2
resultado = ""

if media >= 7:
    resultado = "Aprovado"
elif media >= 4 and media < 7:
    resultado = "Recuperacao"
else:
    resultado = "Reprovado"

print(resultado)
