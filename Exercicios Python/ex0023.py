#Crie um programa que leia o nome de uma pessoa e mostre: O nome com todas as letras maiusculas; O nome com todas as letras minusculas; Quantas letras ao todo sem considerar os espços; Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')