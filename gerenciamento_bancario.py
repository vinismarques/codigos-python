class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Idade: {self.idade}'


class Conta():

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def consultarSaldo(self):
        return self.saldo


vinicius = Cliente('Vinicius', '027242', '25')
conta = Conta(vinicius, 390)

# print(vinicius.nome, vinicius.cpf, vinicius.idade)
# print(f'Nome: {vinicius.nome}, CPF: {vinicius.cpf}, Idade: {vinicius.idade}')
print(vinicius)

conta.depositar(10)
conta.sacar(390.5)

print(f'Cliente {conta.cliente.nome} tem R$ {conta.consultarSaldo() :.2f}'
      f' em sua conta')
