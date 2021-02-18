# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
n1 = float(input('Digite a temperatura em graus Celsius (ºC):'))
#Tc = (n1 * 1.8) + 32
Tc = (9*n1/5) + 32
print('Sua nova temperatura em gruas Fahrenheit corresponte a {} ºF '.format(Tc))