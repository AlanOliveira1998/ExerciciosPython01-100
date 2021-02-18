#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
Al = input('Digite algo:')
#print('O tipo primitivo desse valor é {} '.format(type(Al))) Abaixo outro jeito de usar o .format
print(f'O tipo primitivo desse valor é{type(Al)}')
print('Só tem espaços?', Al.isspace())
print('É um numero?', Al.isnumeric())
print('É alfabético?', Al.isalpha())
print('É alfanumerico', Al.isalnum())
print('Está em maiusculo?', Al.isupper())
print('Está em minusculo?', Al.islower())
print('Está capitalizado?', Al.istitle())