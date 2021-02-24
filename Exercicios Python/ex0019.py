#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosse e tangente
import math
n = int(input('Digite o valor do seu angulo:'))
se = math.sin(math.radians(n))
co = math.cos(math.radians(n))
ta = math.tan(math.radians(n))
print('O valo do seno corresponde a {:.2f},\n do coseno {:.2f} \n e da tangente {:.2f}'.format(se, co, ta))