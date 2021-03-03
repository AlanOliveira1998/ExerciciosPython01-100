#Faça um programa que leia tres numeros e mostre qual e o maior e qual e o menor
#Lendo tres numeros
n1 = int(input('Numero aleatório 1:'))
n2 = int(input('Numero aleatório 2:'))
n3 = int(input('Numero aleatório 3:'))
# Para maior 
if n1 > n2 > n3:
    print(f'O maior numero é {n1}')
if n2 > n1 > n3:
    print(f'O maior numero é {n2}')
if n3 > n2 > n1:
    print(f'O maior numero é {n3}')
# Para menor
if n1 < n2 < n3:
    print(f'E o menor numero é {n1}')
if n2 < n1 < n3:
    print(f'E o menor numero é  {n2}')
if n3 < n2 < n1:
    print(f'E o menor numero é  {n3}')
