# Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento
n1 = float(input('Digite seu salário: R$'))
n = n1 * 0.15
n2 = n + n1
print('Seu novo salário equivale a R$ {:.2f}'.format(n2))