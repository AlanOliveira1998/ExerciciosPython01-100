import emoji
print('Olá eu sou Levy seu amigo robo e hoje eu vou calcular o seu IMC (Indice de Massa Corporal.) Alan Vamos lá ?')
nome = (input('Qual o seu nome?'))
idade = str(input('Qual a sua idade?'))
peso = float(input('Qual o seu peso ?'))
altura = float(input('Qual a sua altura em metros?'))
imc = peso / (altura*altura) 
print(emoji.emojize(f'O seu IMC corresponde a {imc}. Abaixo segue os valores de referencia para consulta, obrigado por usar nossa calculadora :earth_americas:', use_aliases=True))  
print('menor que 18,5: baixo; \n peso entre 18,5 e 24,9: intervalo normal \n entre 25 e 29,9: sobrepeso; \n entre 30 e 34,9: obesidade classe I; \n entre 35 e 39,9: obesidade classe II; \n maior que 40: obesidade classe III')