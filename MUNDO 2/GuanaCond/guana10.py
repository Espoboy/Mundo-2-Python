# 44 Escrever um programa que calcula o valor a ser pago por um produto
#   considerando seu preço normal e a forma de pagamento

#JEITO NORMAL

'''À vista(dinheiro/cheque) - 10% de desconto // À vista no cartão - 5% de desconto
Em até 2x no cartão - Preço normal // A partir de 3x - 20% de juros no valor total'''

print('\033[0;31m↔ \033[m' * 14)
print(' ' * 5, '\033[1;33mSATURNNY STORE\033[m')
print('\033[0;31m↔ \033[m' * 14)

valor = float(input('Valor das compras: R$'))

print('FORMA DE PAGAMENTO')
print("""\033[36m[ 1 ] Dinheiro/Cheque\033[m
\033[31m[ 2 ] À vista Cartão\033[m
\033[32m[ 3 ] Parcelado 2x\033[m
\033[34m[ 4 ] Parcelado 3x ou mais\033[m""")

forma = int(input('Qual é a forma?\n'))

if forma == 1:
    desconto = valor - (valor * 10 / 100)
    print('Você conseguiu um desconto de 10% totalizando o valor de R${:.2f}'.format(desconto))
elif forma == 2:
    desconto = valor - (valor * 5 / 100)
    print('Você conseguiu um desconto de 5% totalizando o valor de R${:.2f}'.format(desconto))
elif forma == 3:
    parcela = valor / 2
    print(f'O valor total será de R${valor:.2f} dividido em 2 vezes que fica {parcela:.2f}.')
else:
    parcelas = int(input('Quantas parcelas?\n'))
    juros = valor + (valor * 20 / 100)
    parcela = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(parcelas, parcela))
    print('O valor total será de R${:.2f} com uma taxa de juros de 20%.'.format(juros))