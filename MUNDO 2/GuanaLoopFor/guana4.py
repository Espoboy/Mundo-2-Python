# Ex 48 Escreva um programa que calcule a soma de todos
#   os números ímpares e múltiplos de 3, de 1 a 500
n = 0
cont = 0
for c in range(1,501):
    if c % 3 == 0 and c % 2 == 1:
        n += c
        cont += 1
print(f'A soma dos ímpares até 500 vale {n} e é um total de {cont} números somados.')
# OU
tnoc = 0
j = 0
for h in range(1, 501, 2):
    if h % 3 == 0:
        j += h
        tnoc += 1
print(f'A soma dos ímpares até 500 vale {j} e é um total de {tnoc} números somados.')