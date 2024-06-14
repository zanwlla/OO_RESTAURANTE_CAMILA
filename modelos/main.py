from modelos.atividade4 import Livro

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

def __str__(self):
        return f"'{livro1.titulo}' feito por {livro1.autor}, {livro2.titulo}' feito por {livro2.autor} "

print(livro1)
print(livro2)