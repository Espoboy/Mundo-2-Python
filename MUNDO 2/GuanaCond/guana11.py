# Ex 45 Jokenpô contra PC

print('\033[1;31m♦♣♠♥\033[m' * 6)
print('\033[1;31m♦\033[m', ' ' * 6, '\033[1;33mJOKENPÔ\033[m', ' ' * 5, '\033[1;31m♥\033[m')
print('\033[1;31m♦♣♠♥\033[m' * 6)

from random import choice
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']

computador = choice(lista).upper() 


print('\033[33mDigite Pedra, papel ou tesoura.\033[m')
escolha = str(input()).strip().upper()

print('\033[34mJO')
sleep(1)
print('\033[34mKEN')
sleep(1)
print('\033[34mPÔ!')
sleep(1)
if computador == escolha:
    print('\033[34mInfelizmente dessa vez não houve vencedor\033[m')
elif computador == 'TESOURA' and escolha == 'PAPEL':
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')
elif escolha == 'TESOURA' and computador == 'PAPEL':
    print('\033[35mVocê teve sorte dessa vez...\033[m')
elif computador == 'PEDRA' and escolha == 'TESOURA':
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')
elif escolha == 'PEDRA' and computador == 'TESOURA':
    print('\033[35mVocê teve sorte dessa vez...\033[m')
elif computador == 'PAPEL' and escolha == 'PEDRA':
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')    
elif escolha == 'PAPEL' and computador == 'PEDRA':
    print('\033[35mVocê teve sorte dessa vez...\033[m')

print('Computador  - {}\nPlayer - {}'.format(computador.capitalize(), escolha.capitalize()))
    