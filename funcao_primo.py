def eh_primo(x):
    if x == 1:
        return True

    divisores = 0
    for i in range(x, 0, -1):
        if x % i == 0:
            divisores += 1
    return True if divisores == 2 else False


x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')
