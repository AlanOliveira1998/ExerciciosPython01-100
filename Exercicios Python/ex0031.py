# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
# Condição: Consideramos um número como sendo par quando o dividimos por dois e seu resto é zero. Já um número é ímpar quando, na divisão por dois, o resto é diferente de zero.

n = int(input('Digite um numero:'))
resultado = n % 2
if resultado == 0:
    print(f'O numero {n} é par')
else:
    print(f'O numeor {n} é impar')