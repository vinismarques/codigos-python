arquivo = open('arquivo.txt', 'r')

for i in range(1001):
    arquivo.write(f'Teste de escrita {i}\n')
