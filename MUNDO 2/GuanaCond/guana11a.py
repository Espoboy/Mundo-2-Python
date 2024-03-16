# Ex 45 Jokenpô contra PC

# JEITO GUANABARA

print('\033[1;31m♦♣♠♥\033[m' * 6)
print('\033[1;31m♦\033[m', ' ' * 6, '\033[1;33mJOKENPÔ\033[m', ' ' * 5, '\033[1;31m♥\033[m')
print('\033[1;31m♦♣♠♥\033[m' * 6)

from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2) 


print('''\033[33mSUAS OPÇÕES
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura\033[m''')
escolha = int(input())

print('\033[34mJO')
sleep(1)
print('\033[34mKEN')
sleep(1)
print('\033[34mPÔ!')
sleep(1)
if computador == escolha:
    print('\033[34mInfelizmente dessa vez não houve vencedor\033[m')
elif computador == 2 and escolha == 1:
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')
elif escolha == 2 and computador == 1:
    print('\033[35mVocê teve sorte dessa vez...\033[m')
elif computador == 0 and escolha == 2:
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')
elif escolha == 0 and computador == 2:
    print('\033[35mVocê teve sorte dessa vez...\033[m')
elif computador == 1 and escolha == 0:
    print('\033[31mMUAHAHAHA! VENCI!!\033[m')    
elif escolha == 1 and computador == 0:
    print('\033[35mVocê teve sorte dessa vez...\033[m')

print('Computador  - {}\nPlayer - {}'.format(lista[computador], lista[escolha]))

