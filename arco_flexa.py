import math

N = int(input())

penalty = 0
dist = []
for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)

    dist.append(math.hypot(x, y))

    for j in range(len(dist)):
        if dist[i] >= dist[j] and i != j:
            penalty += 1

print(penalty)
