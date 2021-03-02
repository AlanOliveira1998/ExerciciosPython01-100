# Escreva um programa que leia a velocidade de um carro: - Se ele ultrapassar 80Km/h, mostre na tela uma mensagem que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite
vel = float(input('Digite a velocidade do carro:'))
multa = (vel - 80) * 7 
if vel >80:
    print(f'Voê estava a cima do limite permitido e foi multado, o valor da multa a pagar é de R$ {multa}')
else:
    print('Você está dentro do limite proposto')