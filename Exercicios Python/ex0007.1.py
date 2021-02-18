#nome = input('Qual é o seu nome:')
#print('Prazer em te conhecer {:20}!'.format(nome)) escreve o nome em 20 caracteres
#print('Prazer em te conhecer {:>20}!'.format(nome)) alinha o nome a direita em vinte espaços
#print('Prazer em te conhecer {:<20}!'.format(nome)) alinha o nome a esquerda em vinte espaços
#print('Prazer em te conhecer {:^20}!'.format(nome)) centraliza o nome em vinte espaços
#print('Prazer em te conhecer {:=^20}!'.format(nome)) centraliza o nome e coloca 20 sinais de igaul
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
p = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, p, d))
#print('A soma é {},\n o produto é {} e a \n divisão é {:.2f}'.format(s, p, d)) O contra barra (\) n, quebra a linha do codigo para a proxima linha
print('A divisão inteira é {} e a potência é {:.2f}'.format(di, e), end=' ')