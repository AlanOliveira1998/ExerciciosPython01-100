#Criar um programa que calcule o IMC de uma pessoa
print('Ola, eu sou a Kenny e agora vamos calcular o seu IMC (Índice de Massa Corporal), vamos lá?')
nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
altura = float(input('Qual a sua altura?'))
peso = float(input('Qual é o seu peso?'))
n = peso/(altura*altura)
print('Seu IMC corresponde a {:.2f}'.format(n))