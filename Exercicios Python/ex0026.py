#Crie um programa que leia o nepme de uam pessoa e diga se ela tem silva nonome
nome = str(input('Qual o seu nome:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))