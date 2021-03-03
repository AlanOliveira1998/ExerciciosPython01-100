# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.
#Condição de existencia de um triangulo: Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
print ('-=' * 20)
print('Analisador de Triangulos')
print ('-=' * 20)
r1 = float(input('Digite da reta numero 1:'))
r2 = float(input('Digite da reta numero 2:'))
r3 = float(input('Digite da reta numero 3:'))

#Condiçao de existencia de eum triangulo
c = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
if c == True:
    print('Com esse valores você consegue formar um triangulo')
else:
    print('Com esses valores você não consegue formar um triangulo')
if r1 == r2:
    print('E esse triangulo é ISÒCELES')
if r1 != r2 != r3:
    print('E esse triangulo é ESCALENO')
if r1 == r2 == r3:
    print('E esse triangulo é EQUILATERO')