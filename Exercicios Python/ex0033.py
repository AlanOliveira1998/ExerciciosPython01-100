# falça um programa que leia um ano qualquer e mostre se ele é bissexto
# Condição: 
#1 - Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.;
#2 - Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.;
#3 - Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.;
#4 - O ano é bissexto (tem 366 dias).;
#5 - O ano não é um ano bissexto (tem 365 dias).;

ano = int(input('Digite um ano qualquer:'))
#Condição 1:
resul_1 = ano /4
if resul_1 = % 0:
    resul_1 / 100
    n = resul_1 / 100
    if n != 0:
        print('O ano de {} é bissesto')
