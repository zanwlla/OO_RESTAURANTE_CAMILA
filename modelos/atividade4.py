
#questão 1
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
#questão 2
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"
#questão 3
    def emprestar(self):
        self.disponivel = True
#questão 3
    @staticmethod
    def verificar_disponibilidade(livros, ano):
        return [livro for livro in livros if livro.ano_publicacao == ano and livro.disponivel]

#questão 2
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("As crônicas de Nárnia", "Clive Staples Lewis", 1949)

#questão 3
print(livro1)
print(livro2)

#questão 3
livro3 = Livro("Romeu e Julieta", "William Shakespeare", 1595)
livro3.emprestar()
print(f"O livro '{livro3.titulo}' está disponível? {'Sim' if livro3.disponivel else 'Não'}")

#questão 4
livros = [livro1, livro2, livro3]
livros_disponiveis = Livro.verificar_disponibilidade(livros, 1595)
print(f"Livros disponíveis publicados em 1595: {[livro.titulo for livro in livros_disponiveis]}")
