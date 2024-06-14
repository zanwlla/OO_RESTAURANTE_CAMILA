#questão 5
from modelos.atividade4 import Livro

#questão 6
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro3 = Livro("As crônicas de Nárnia", "Clive Staples Lewis", 1949)
livro1.emprestar()
print(f"O livro '{livro1.titulo}' está disponível? {'Sim' if livro1.disponivel else 'Não'}")

#questão 7
livros = [livro1,livro2,livro3]
livros_disponiveis = Livro.verificar_disponibilidade(livros, 1937)
print(f"Livros disponíveis publicados em 1937: {[livro.titulo for livro in livros_disponiveis]}")