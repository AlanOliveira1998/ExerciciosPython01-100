# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a sua nota da prova 1:'))
n2 = float(input('Digite a sua nota da sua prova 2:'))
m = (n1 + n2) / 2
print('A sua média entre as duas notas equivale a {:.2f}'.format(m))
if m > 6:print('Está aprovado, boas férias')
if m < 6:print('Está reprovado, consultar a secretária para fazer a recuperação')