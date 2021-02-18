#Criar um programa que pergunte minha data de nascimento e mostre uma mensagem ao final
dia = int(input('Dia de nascimento:'))
mes = input ('Mes de nascimento:')
ano = int(input('Ano de nascimento:'))
#print('Você nasceu no dia' , dia, 'de' , mes, 'de', ano, ',correto?') Abaixo outra opção de escrever a mesma coisa
print('Você nasceu no dia {} de {} de {}, correto?'.format(dia, mes, ano))


