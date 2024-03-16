# Ex 50 Ler 6 números inteiros mostrando a soma apenas dos pares
#   desconsiderando os ímpares

s = 0
parcont = 0
for c in range(1, 7):
    n = int(input(f'Valor {c}:'))
    if n % 2 == 0:
        s += n
        parcont += 1
print(f'Você informou {parcont} números pares. O total da soma é de: {s}')