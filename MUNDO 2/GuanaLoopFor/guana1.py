# Aula 13

''' Laço "for", "para".
Laços são estruturas de repetição que executam um código
quantas vezes for necessário para suprir uma condição. '''

'print("Oi")'

# Se eu quiser escrever mais vezes?

for c in range(0,6): # 'c' pode ser qualquer nome de variável
    print('oi', end=' ')

print(' ')

for c in range(0,6):
    # range(0,6) conta 0, 1, 2, 3, 4, 5 o 6 fica de fora
    print(c, end=' ')

print(' ')

for c in range(6, 0, -1):
    # range(6, 0, -1) tira de 1 em 1 até o 0
    print(c, end=' ')

print(' ')

for c in range(0, 7, 2):
    # range(0, 7, 2) conta de 2 em 2
    print(c, end=' ')

print(' ')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c, end=' ')

print(' ')

s = 0
for c in range(0, 4):
    n = float(input('Digite um valor: '))
    s += n
print(f'O somatório dos valores foi {s:.1f}')