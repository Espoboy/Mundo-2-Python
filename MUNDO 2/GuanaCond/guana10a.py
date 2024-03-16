# 44 Escrever um programa que calcula o valor a ser pago por um produto
#   considerando seu preço normal e a forma de pagamento

# Jeito brincando

'''À vista(dinheiro/cheque) - 10% de desconto // À vista no cartão - 5% de desconto
Em até 2x no cartão - Preço normal // A partir de 3x - 20% de juros no valor total'''

print('\033[0;31m↔ \033[m' * 14)
print(' ' * 5, '\033[1;33mSATURNNY STORE\033[m')
print('\033[0;31m↔ \033[m' * 14)

print('\033[33mBem vindo à Saturnny Store!')
print('Qual item deseja comprar?\033[m')

print("""\033[36m[ 1 ] IPhone 15 Ultra\033[m
\033[31m[ 2 ] Samsung S24 Pro Max\033[m
\033[32m[ 3 ] Nokia 3310\033[m""")

item = int(input('\033[1;33mDigite aqui: \033[m'))

if item == 1:
    print("O valor do IPhone 15 Ultra é de R$16.000. Como deseja pagar?")
    print("""\033[36m[ 1 ] Dinheiro/Cheque\033[m
\033[31m[ 2 ] À vista Cartão\033[m
\033[32m[ 3 ] Parcelado\033[m""")
    pagamento = int(input('\033[0;33mDigite aqui: \033[m'))
    if pagamento == 1:
        desconto = 16000 - (16000 * 10 / 100)
        print('Você conseguiu um desconto de 10% totalizando o valor de {}'.format(desconto))
    elif pagamento <= 2:
        desconto = 16000 - (16000 * 5 / 100)
        print('Você conseguiu um desconto de 5% totalizando o valor de {}'.format(desconto))
    elif pagamento == 3:
        parcelas = int(input('De quantas vezes deseja parcelar?\n'))
        if parcelas == 2:
            parcela = 16000 / parcelas
            print('O valor total será de R$16.000 dividido em 2 vezes que fica {}.'.format(parcela))
        else:
            juros = 16000 + (16000 * 20 / 100)
            parcela = juros / parcelas
            print('Parcelando em {}x o valor do produto fica R${:.2f}, parcelas de {:.2f} e com um juros de 20%.'.format(parcelas, juros, parcela))

elif item == 2:
    print("O valor do Samsung S24 Pro Max é de R$6.000. Como deseja pagar?")
    print("""\033[36m[ 1 ] Dinheiro/Cheque\033[m
\033[31m[ 2 ] À vista Cartão\033[m
\033[32m[ 3 ] Parcelado\033[m""")
    pagamento = int(input('\033[0;33mDigite aqui: \033[m'))
    if pagamento == 1:
        desconto = 6000 - (6000 * 10 / 100)
        print('Você conseguiu um desconto de 10% totalizando o valor de {}'.format(desconto))
    elif pagamento <= 2:
        desconto = 6000 - (6000 * 5 / 100)
        print('Você conseguiu um desconto de 5% totalizando o valor de {}'.format(desconto))
    elif pagamento == 3:
        parcelas = int(input('De quantas vezes deseja parcelar?\n'))
        if parcelas == 2:
            parcela = 6000 / parcelas
            print('O valor total será de R$16.000 dividido em 2 vezes que fica {}.'.format(parcela))
        else:
            juros = 6000 + (6000 * 20 / 100)
            parcela = juros / parcelas
            print('Parcelando em {}x o valor do produto fica R${:.2f}, parcelas de {:.2f} e com um juros de 20%.'.format(parcelas, juros, parcela))

elif item == 3:
    print("O valor do Nokia 3310 é de R$150. Como deseja pagar?")
    print("""\033[36m[ 1 ] Dinheiro/Cheque\033[m
\033[31m[ 2 ] À vista Cartão\033[m
\033[32m[ 3 ] Parcelado\033[m""")
    pagamento = int(input('\033[0;33mDigite aqui: \033[m'))
    if pagamento == 1:
        desconto = 150 - (150 * 10 / 100)
        print('Você conseguiu um desconto de 10% totalizando o valor de {}'.format(desconto))
    elif pagamento <= 2:
        desconto = 150 - (150 * 5 / 100)
        print('Você conseguiu um desconto de 5% totalizando o valor de {}'.format(desconto))
    elif pagamento == 3:
        parcelas = int(input('De quantas vezes deseja parcelar?\n'))
        if parcelas == 2:
            parcela = 150 / parcelas
            print('O valor total será de R$16.000 dividido em 2 vezes que fica {}.'.format(parcela))
        else:
            juros = 150 + (150 * 20 / 100)
            parcela = juros / parcelas
            print('Parcelando em {}x o valor do produto fica R${:.2f}, parcelas de {:.2f} e com um juros de 20%.'.format(parcelas, juros, parcela))

print('\033[1;31mObrigado pela preferência!\033[m')