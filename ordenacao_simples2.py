# Entrada
N = int(input())
numbers = input().split()

# Processamento
for ni, num in enumerate(numbers):
    numbers[ni] = int(num)
ordered = sorted(numbers)

# Saída
for i in ordered:
    print(i, end=' ')

print()
