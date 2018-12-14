# list:
lista = ['Vini', 'Lari']


# tuple: imutável; sem métodos embutidos
tupla = ('Vini', 'Lari')


# dict: é possível adicionar key/values posteriormente; otimizado para pesquisa
dicionario = {'nome': 'Vini', 'idade': 25}

if 'Vini' in dicionario.values():
    print('"Vini" está nos dicionário.')

dicionario['endereco'] = 'Rua General Neto'


# set: valores únicos; sem index; otimizado para pesquisa
conjunto = {'Vini', 'Lari'}

conjunto.add('Deliel')
