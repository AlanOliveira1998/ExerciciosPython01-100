#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra A; Em que posição ela aparece a primeira vez; Em que posição ela aparece a ultima vez
n = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase'. format(n.count('A')))
print('A primeira letra A apareceu na posição {}'.format(n.find('A')+1))
print(' A ultima letra A apareceu na posição {}'.format(n.rfind('A')+1))