# Ex 36 Aprovação de Empréstimo

'''Escrever um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa pergunta o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. O programa
deve calcular o valor da prestação mensal sabendo que ela não
pode exceder 30% do salário ou então será negado o empréstimo'''

print('\033[31m-=-\033[m' * 16)
print('\033[33m  BEM-VINDO(A) AO NOSSO BANCO DE EMPRÉSTIMOS!\033[m')
print('\033[31m-=-\033[m' * 16)

from time import sleep

# Coletando dados necessários
casa = float(input('\033[34mQual o valor da casa?\033[m\n'))
salario = float(input('\033[32mQual o seu salário?\033[m\n'))
anos = int(input('\033[36mEm quantos anos deseja quitar o empréstimo?\033[m\n'))

# Calculando prestações
prestacao = (casa / anos) / 12

print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação mensal será de R${:.2f}.'.format(casa, anos, prestacao))
print(' ')

print('\033[36mPROCESSANDO...')
sleep(3)

# Condição
if prestacao < (salario * 30 / 100):
    print('\033[32mPARABÉNS!!!\033[m Seu empréstimo será concedido imediatamente!')
else:
    print("""\033[31mNEGADO!!! \033[mFizemos uma análise da sua atual condição
e chegamos à conclusão de que esse empréstimo possui um alto risco
de acabar não sendo finalizado, pode tentar em outro momento.""")

# Final
print(' ')
print('\033[36mObrigado por utilizar nosso banco. :)\033[m')

