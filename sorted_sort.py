L = [5, 4, 3, 2, 1]

# Usado para gerar uma nova lista
R = sorted(L)
print(R)

# Usado para ordenar uma lista, sem manter o original
L.sort()
print(L)

# Reverso com sort()
L = [5, 4, 3, 2, 1]
L.sort(reverse=True)
print(L)

# Reverso com sorted()
L = [5, 4, 3, 2, 1]
print(sorted(L, reverse=True))
