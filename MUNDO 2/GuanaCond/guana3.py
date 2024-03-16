# Ex 37 Ler um número inteiro e pedir ao usuário para escolher a base
#   de conversão, 1 = Binário 2 = Octal 3 = Hexadecimal

print('\033[35m-=-\033[m' * 16)
print('\033[32m  BEM-VINDO(A) AO NOSSO CONVERSOR DE NÚMEROS!\033[m')
print('\033[35m-=-\033[m' * 16)

num = int(input('Digite um número inteiro para converter: '))

op = print("""DIGITE:
    \033[30m[ 1 ] Para binário\033[m
    \033[31m[ 2 ] Para octal\033[m
    \033[34m[ 3 ] Para hexadecimal\033[m""")
opcao = int(input('\033[32mDigite aqui --->\033[m '))

if opcao == 1:
    print('{} convertido para binário fica {}.'.format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} convertido para octal fica {}.'.format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal fica {}.'.format(num, hex(num) [2:]))
else:
    print('Parece que algo deu errado. Tente novamente!')