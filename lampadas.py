N = input()
acao = input().split()
A = 0
B = 0

for i in acao:
    if i == '1':
        if A == 1:
            A = 0
        else:
            A = 1
    elif i == '2':
        if A == 1:
            A = 0
        else:
            A = 1
        if B == 1:
            B = 0
        else:
            B = 1

print(A)
print(B)
