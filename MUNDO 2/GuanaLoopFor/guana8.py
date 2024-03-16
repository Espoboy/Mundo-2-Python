# Ex 52 Ler um número inteiro e dizer se é primo

num = int(input('Digite um valor:'))
tot = 0 
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end='\033[m')
print('')
if tot == 2:
    print(f'{num} é primo! Pois ele é dividido somente {tot}x.')
else:
    print(f'{num} não é primo pois ele é dividido {tot}x.')