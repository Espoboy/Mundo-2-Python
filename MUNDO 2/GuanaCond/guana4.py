# Ex 38 escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela:
# O primeiro valor é o maior
# O segundo valor é o maior
# Não existe valor maior, os dois são iguais.

print('\033[36m-+\033[m' * 20)
print(' ' * 8 ,'\033[34;4mCOMPARADOR DE NÚMEROS\033[m')
print('\033[36m-+\033[m' * 20)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Agora o segundo: '))

if num1 > num2:
    print('\033[33m{} é um número maior que {}.\033[m'.format(num1, num2))
elif num2 > num1:
    print('\033[32m{} é um número maior que {}.'.format(num2, num1))
else:
    print('\033[32mNão existe valor maior, os dois são iguais!\033[m')