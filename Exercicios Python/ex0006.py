# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um numero:'))
#print('Analisando o numero escolhido tems que seu dobro vale {}, seu triplo vale {} e sua raiz quadrada vale {}.'.format(d, t, r))
print('Analisando o numero escolhido, temos que \n seu dobro vale {}; \n seu triplo vale {} \n sua raiz quadrada vale {:.2f}'.format(n1*2, n1*3, n1**(1/2)))
#print('Analisando o numero escolhido, temos que \n seu dobro vale {}; \n seu triplo vale {} \n sua raiz quadrada vale {:.2f}'.format(n1*2, n1*3, pow(n1, (1/2))))
#Outro calculo de raiz quadrada pow(n, (1/2))
