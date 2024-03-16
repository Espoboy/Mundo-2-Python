# Aula 14 Estrutura de Repetição While

# Comparando While e For

for c in range(1,10):
    print(c, end=' ')
print('Fim')

c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('Fim')

print(' ')

'''for p in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')

print(' ')'''

n = 1
r = ''
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
print('Fim')

print(' ')

m = 1
par = impar = 0
while m != 0:
    m = int(input('Digite um valor: '))
    if m != 0:
        if m % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'\033[35mVocê digitou {par} números pares e {impar} números ímpares.\033[m')
