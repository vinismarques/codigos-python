from math import gcd

N, M = input().split()
N = int(N)
M = int(M)

for i in range(M, 0, -1):
    if gcd(N, i) == 1:
        X = i
        break

print(X)
