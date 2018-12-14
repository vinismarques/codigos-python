from array import array

N = int(input())

penalty = 0
a = array('i', (0,)) * N

for i in range(N):
    x, y = input().split()
    x = abs(int(x))
    y = abs(int(y))

    a[i] = x + y

    # dist.append(math.hypot(x, y))

    for j in range(i):
        if a[i] >= a[j] and i != j:
            penalty += 1


print(penalty)
