# Atividade 1
class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
    def __str__(self):
        return f'{self.modelo}|{self.cor}|{self.ano}'
    
carro1=Carro('Voyage','Cinza','2019')
print(carro1)

# Atividade 2
class Restaurante:
    nome=''
    categoria=''
    chef=''
    avaliação=''
    ativo=False

restaurante_DOM=Restaurante()
restaurante_DOM.nome='Rancho Fundo'
restaurante_DOM.categoria='Caseira'
restaurante_DOM.chef='Madalena'
restaurante_DOM.avaliação='5 estrelas'
print(vars(restaurante_DOM))

# Atividade 3
class Restaurante:
    def __init__(self,nome,categoria,chef,avaliação):
        self.nome=nome
        self.categoria=categoria
        self.chef=chef
        self.avaliação=avaliação
        self.ativo=False
# Atividade 4
    def __str__(self):
        return f'{self.nome}|{self.categoria}|{self.chef}|{self.avaliação}|{self.ativo}'
    
# Atividade 3
restaurante_DOM=Restaurante('Rancho Fundo','Caseira','Madalena','4 estrelas')

# Atividade 4
print(restaurante_DOM)

# Atividade 5
class Cliente:
    def __init__(self,nome,idade,CPF):
        self.nome=nome
        self.idade=idade
        self.CPF=CPF
        self.estado='PR'
    
    def __str__(self):
        return f'{self.nome}|{self.idade}|{self.CPF}|{self.estado}'
cliente1=Cliente('Tais',25, '234.551.098-28')

print(cliente1)


