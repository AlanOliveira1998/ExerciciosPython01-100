# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar (usa 1 dolar = a 3.27 reais)
n1 = float(input('Digite o valor que tem na carteira em reais: R$'))
d = n1 / 3.27
print('Com R${:.2f} você poderar comprar U${:.2f} dolares'.format(n1, d))

