# Primeira representação de uma estrutura condicionl

#if carro.esquerda():
  #  bloco True
#else:
 #   |bloco False

#tempo = int(input('Quantos anos tem seu carro?'))
#if tempo <=3:
 #   print('Seu carro está novo')
#else:
 #   print('Seu carro está velho')
#print('--FIM--')

# Condição Simplificada

#tempo = int(input('Quantos anos tem seu carro?'))
#print('Carro novo' if tempo<=3 else'Carro velho')
#print('--FIM--')

#nome = str(input('Qual é o seu nome?')).strip()
#if nome == 'Gustavo':
 #   print('Que nome linto voce tem')
#else:
 #   print('Seu nome é tão normal!')    
#print(f'Bom dia, {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
n = (n1 + n2) / 2
print(f'A sua média corresponde a {n}')
if n >=6:
    print('Voce está aprovado')
else:
    print('Você está reprovado, por favor verificar com a direção do curso')
print('--FIM--')