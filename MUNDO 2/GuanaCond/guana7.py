# Ex 41 Escrever um programa que leia o ano de nascimento de um atleta
#    e mostre sua categoria de acordo com a idade.
'''Até 9 anos = Mirim, Até 14 = Infantil, Até 19 = Junior
   Até 20 = Senior, Acima = MASTER'''

print('\033[32m♦ ♦ \033[m' * 10)
print(' ' * 2, '\033[34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[34m')
print('\033[32m♦ ♦ \033[m' * 10)

from datetime import date

atual = date.today().year
ano = int(input('Ano de seu nascimento: '))
idade = atual - ano

print('\033[32m♦ ♦ \033[m' * 10)

print('A sua idade hoje é de {} anos.'.format(idade))

print('\033[32m♦ ♦ \033[m' * 10)

if idade <= 9:
    print('A categoria correta para você é a Mirim.')
elif idade <= 14:
    print('A categoria correta para você é a Infantil.')
elif idade <= 19:
    print('A categoria correta para você é a Júnior.')
elif idade <=25:
    print('A categoria correta para você é a Sênior.')
else:
    print('A categoria correta para você é a Master.') 
print('\033[32m♦ ♦ \033[m' * 10)