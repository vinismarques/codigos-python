risada = input()

consoantes = ['a', 'e', 'i', 'o', 'u']
resul = ''

for i in risada:
    if i in consoantes:
        resul += i

if resul == resul[::-1]:
    print("S")
else:
    print("N")
