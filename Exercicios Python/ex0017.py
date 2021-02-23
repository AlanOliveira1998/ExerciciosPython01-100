#Crie um programa que leia um numero real qualquer e mostre somete a sua parte inteira
import math
n = float(input('Digite um numero:'))
inteiro = math.trunc(n)
print('A parte inteira do numero {} corresponde a {}'.format(n, inteiro))