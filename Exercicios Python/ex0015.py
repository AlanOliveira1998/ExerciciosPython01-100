#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Km = float(input('Digite o numero de Km percorridos:'))
Di = int(input('Digite quantos dias ele foi alugado:'))
km1 = (Km * 0.15) + (Di * 60)
print('O valor total a pagar e de R$ {:.2f}'.format(km1))