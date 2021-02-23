#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente e calcule e mostre a sua hipotenusa
import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa corresponde a {h}')
# h = (co ** 2 + ca ** 2) ** (1/2)