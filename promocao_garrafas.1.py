# Input
T = int(input())
dias = []

for i in range(T):
    dias.append(input().split())

# Processing
for i in range(T):
    compradas = int(dias[i][0])
    vazias = int(dias[i][1])

    print(compradas // vazias + compradas % vazias)
