# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n = float(input('Digite o valor em metros (m):'))
cm = n*100
mm = n*1000
dam = n/10
hm = n/100
km = n/ 1000
print('O valor em centimetros equivale a {} cm'. format(cm))
print('O valor em milimetros equivale a {} m.m'.format(mm))
print('O valor em decametros equivale a {} dam'.format(dam))
print('O valor em hectometros equivale a {} hm'.format(hm))
print('O valor em kilometros equivale a {} km'.format(km))
