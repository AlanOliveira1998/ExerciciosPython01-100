# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. Deve mostrar na tela se o usuario venceu ou perdeu
import random #Faz o computador pensar
import time
print('-=' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar....')
print('-=' * 30)
n = int(input('Em que numero eu pensei?')) #O jogador tenta adivinhar
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print('PROCESSANDO....')
time.sleep(2) #faz o computador espera por 2 segundos
if n == escolhido:
    print('PARABENS!, você conseguiu vencer ')
else:
    print(f'GANHEI! Eu pensei no número {escolhido} e não no {n}!')