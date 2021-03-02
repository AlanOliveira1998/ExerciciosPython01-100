# Desenvolva um programa que que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
n = (n1 + n2) / 2
print(f'A sua média corresponde a {n}')
if n >=6:
    print('Voce está aprovado')
else:
    print('Você está reprovado, por favor verificar com a direção do curso')
print('--FIM--')