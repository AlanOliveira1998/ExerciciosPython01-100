#O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um prgrama que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
lista = [a,b,c,d]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)