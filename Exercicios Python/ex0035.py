# Escreva um programa que pergunte o salrio de uma funcionario e calcule o valor do seu aumento: - Para salarios superiores a R$ 1.250,00 calcule um aumento de 10% e para salarios inferiores ou iguais a R$ 1250,00 o aumento é de 15%
s = float(input('Digite o valor do seu salário: R$ '))
maior_que_1250 = (s * 0.1) + s
menor_que_1250 = (s * 0.15) + s
if s > 1250:
    print(f'Seu salário com aumento é de R$ {maior_que_1250}')
if s <= 1250:
    print(f'Seu salário com aumento é de R$ {menor_que_1250}')