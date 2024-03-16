# Ex 59 Ler dois valores e mostrar um menu onde 
'''1 = soma
2 = multiplicação
3 = maior
4 = novos números
5 = sair do programa'''

from time import sleep

print('------Bem vindo------')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = 1

print('=' * 20)
print(' ')

# Se menu for 5 (Sair do programa) o programa encerra
while menu != 5:

    print('Escolha uma opção')
    print("""[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do programa""")
    
    print(' ')
    menu = int(input('Sua escolha: '))

    # Soma
    if menu == 1:
        soma = num1 + num2
        print(f'\033[31mA soma entre {num1} e {num2} é equivalente a {soma}.\033[m')
        print('=' * 20)
        print(' ')
        sleep(1.5)

    # Multiplicação
    if menu == 2:
        multiplicação = num1 * num2
        print(f'\033[31mO produto entre {num1} e {num2} equivale a {multiplicação}.\033[m')
        print('=' * 20)
        print(' ')
        sleep(1.5)

    # Comparação
    if menu == 3:
        if num1 > num2:
            print(f'\033[31mO número {num1} é maior que {num2}.\033[m')
            print('=' * 20)
            print(' ')
            sleep(1.5)
        elif num1 == num2:
            print(f'\033[31mOs dois valores são {num1}, são iguais!\033[m')
            print('=' * 20)
            print(' ')
            sleep(1.5)
        else:
            print(f'\033[31mO número {num2} é maior que {num1}.\033[m')
            print('=' * 20)
            print(' ')
            sleep(1.5)
    
    # Novos valores
    if menu == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    
    if menu == 0 or menu > 5:
        print('\033[31mHouve um erro, tente novamente!\n\033[m')
        print(' ')

print('\033[1;33mFinalizando...\033[m')
sleep(2)
print('\033[35mObrigado por utilizar nosso programa!\033[m')