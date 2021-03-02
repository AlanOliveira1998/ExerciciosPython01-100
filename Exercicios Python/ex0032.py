# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de ate 200Km e R$ 0,45 para viagens mais longas.
dis = float(input('De quanto foi a distancia da sua viagem:'))
preço_a = dis * 0.5
preço_b = dis * 0.45
if dis <= 200:
    print(f' O preço de sua passagem é de R$ {preço_a}')
else:
    print(f'O preço de sua passagem é de R$ {preço_b}')
print('-----Obrigado por compra com a nossa companhia-----')