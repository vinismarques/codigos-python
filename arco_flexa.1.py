from array import array
from math import hypot
# import math

N = int(input())

penalty = 0
a = array('i', (0,)) * N

for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)

    a[i] = int(hypot(x, y))

    # dist.append(math.hypot(x, y))

    for j in range(i):
        if a[i] >= a[j] and i != j:
            penalty += 1


print(penalty)
