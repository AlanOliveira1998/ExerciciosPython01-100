#importando todas as funçoes da biblioteca
#import math
#num = int(input('Digite um numero:'))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {} é {}'.format(num, math.floor(raiz)))

#Importando apenas uma funçao da biblioteca
from math import sqrt, floor
nume = int(input('Digite um número:'))
raiz = sqrt(nume)
print('A raiz quadrada de {} é {}'.format(nume, floor(raiz)))