# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e quantidade de tinta necessário para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2m^2
L = float(input('Digite o valor da largura:'))
A = float(input('Digite o valor da altura:'))
area = L * A
print('A area dessa parede corresponde a {} m²'.format(area))
q = area / 2
print('Para pintar essa parede, você precisara de {} litros de tinta!'.format(q))




