# Ex 63 Escreva um programa que leia um número n inteiro e mostre os n primeiros
#   números de uma sequência de fibonacci

'''Sequencia de Fibonacci, uma sequência 
gerada a partir de um único número(geralmente 1), 
onde o primeiro número é somado ao seu anterior.

(0, 1, 1, 2, 3, 5, 8 ,13...)'''

num = int(input('Digite um valor: '))

f1 = 0
f2 = 1
contagem = 0

while contagem < num:
    print('\033[34m', f1, '\033[m', end='\033[31m → \033[m')
    antigo_f1 = f1
    f1 = f2
    f2 = antigo_f1 + f1
    
    contagem += 1
print('\033[33m FIM! \033[34m')