# 1 criando uma classe usando construtor
class Restaurante:
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
# 2 criando uma instância de classe Restaurante com construtor
restaurante_praca=Restaurante('Praça','Gourmet')

print(restaurante_praca)
