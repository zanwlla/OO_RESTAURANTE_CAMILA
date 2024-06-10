# atividade 1
# class Pessoa:
#     def __init__(self,nome, idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao
    
#     def __str__(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         return f"Saudação, me chamo {self.nome}, e trabalho como {self.profissao}."
    
# pessoa1 = Pessoa("Jhulya", 22+1, "Médica")
# print(pessoa1)              
# pessoa1.aniversario()         
# print(pessoa1.saudacao)    


# atividade 2
# class ContaBancaria:
#     def __init__(self,titular,saldo,ativo,profissao,idade):
#         self.titular=titular
#         self.saldo=saldo
#         self.ativo=False
#         self.profissao=profissao
#         self.idade=idade
# #atividade 3
#     def __str__(self):
#         return f'{self.titular} | {self.saldo} | {self.ativo} | {self.profissao} | {self.idade}'
# #atividade 4  
#     @classmethod
#     def ativar_conta(self):
#         self.ativo=True

# conta_titular=ContaBancaria('Edinelson','R$50.000',True,'Operador de Máquina',44)
# conta_titular.ativar_conta()
# print(conta_titular)

# #atividade 5
# conta2=ContaBancaria('Eloisa','R$35.000',False,'Veterinária',30)
# print(conta2)

# #atividade 6
# print(conta_titular.titular)
# print(conta2.titular)

# atividade 7
# class ClienteBanco:
#     def __init__(self, nome, idade, genero, investimento, saldo):
#         self.nome = nome
#         self.idade = idade
#         self.genero = genero
#         self.investimento = investimento
#         self.saldo = saldo

#     @classmethod
#     def criar_cliente(cls, nome, idade, genero, investimento, saldo):
#         return cls(nome, idade,genero, investimento, saldo)

# #atividade8
#     @classmethod
#     def atualizar_saldo(cls, cliente, valor):
#         cliente.saldo += valor
#         return cliente.saldo

# cliente1 = ClienteBanco.criar_cliente("Mariana", 30, "Feminino", "Carro", 1500.00)
# cliente2 = ClienteBanco.criar_cliente("Paulo", 45, "Masculino", "Casa", 2500.00)
# cliente3 = ClienteBanco.criar_cliente("Ana Alice", 50, "Feminino", "Viagem", 3000.00)

# #atividade8
# ClienteBanco.atualizar_saldo(cliente1, 500.00)  
# ClienteBanco.atualizar_saldo(cliente2, -1000.00)  
# ClienteBanco.atualizar_saldo(cliente3, 200.00)  


# print(vars(cliente1))
# print(vars(cliente2))
# print(vars(cliente3))
