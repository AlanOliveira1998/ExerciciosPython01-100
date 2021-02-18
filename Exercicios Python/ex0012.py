# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto
n1 = float(input('Digite o valor do produto: R$'))
d = n1 - (n1 * 0.05)
print('O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}'.format(n1, d))