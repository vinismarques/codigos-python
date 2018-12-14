N = int(input())
numbers = input().split()
soma = 0

for i in range(len(numbers)):
    soma = soma + int(numbers[i])

print(soma)
