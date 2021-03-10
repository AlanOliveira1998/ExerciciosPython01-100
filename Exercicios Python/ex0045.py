# Elabore um programa que calcule um valor a ser pago por um produto, considerndo o seu preço normal e condições de pagamento:
# A vista no dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2 vezes no cartão: preço normal
# 3 vezes ou mais no cartão: 20% de juros
print('--=--' * 10)
print('LOJAS GUANABARA')
print('--=--' * 10)
preço = float(input('Preço das compras: R$'))
a_vista_dinheiro = preço - (preço * 0.1)
a_vista_no_cartao = preço - (preço * 0.05)
ate_2_vezes_cartao = (preço / 2) 
tres_vezes_ou_mais = (preço * 0.2) + preço
print('FORMAS DE PAGAMENTO \n [1] à vista dinheiro/cheque \n [2] à vista no cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão')
n = int(input('Escolha uma das opções acima:'))
if n == 1:
    print ('O valor a ser pago é de R$ {} com 10% de desconto'.format(a_vista_dinheiro))
elif n == 2:
    print ('O valor a ser pago e de R$ {} com 5% de desconto'.format(a_vista_no_cartao))
elif n == 3:
    print ('O valor da compra é de {} e as parcelas a pagar é de duas de R$ {}'.format(preço, ate_2_vezes_cartao))
elif n == 4:
    parcelas = int(input('Quantas parcelas?'))
    valor = tres_vezes_ou_mais / parcelas
    print('Sua compra será parcelada em {}x de R$ {} e terá um acrescimo de 20% de juros, seu novo valor pago ao final do parcelamento é de R$ {}'.format(parcelas, valor, tres_vezes_ou_mais))
