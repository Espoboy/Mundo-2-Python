# Ex 46 Faça um programa que mostre na tela uma contagem
#   regressiva de 10 a 0 esperando 1 segundo.

from emoji import emojize
from time import sleep


print('\033[31mCONTAGEM REGRESSIVA!\033[m')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
for f in range(0, 10):
    print(emojize(":fireworks:"), end=' ')