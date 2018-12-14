def fatorial(N):
    fat = 1
    if N > 1:
        for i in range(N, 0, -1):  # start (inclusivo), stop (exclusivo), step
            fat = fat * i
    return fat


N = int(input())
print(fatorial(N))
