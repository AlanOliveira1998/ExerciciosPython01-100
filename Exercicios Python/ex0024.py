#Faça um programa que leia de de 0 a 9999 e mostre na tela cada um dos digitos separados:
#Exemplo: 1834
# unidade 4; dezena: 3; centena: 8; milhar: 1
num = int(input('Informe um numero:'))
print(f'Analisando o numero {num}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'milhar: {m}')