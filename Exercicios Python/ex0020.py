#Um professor quer sortear uns dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a = input('Primeiro aluno:')
b = input('Segundo aluno:')
c = input('Terceiro aluno:')
d = input('Quarto aluno:')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')