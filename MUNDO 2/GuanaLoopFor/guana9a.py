# Ex 53 Ler uma frase e dizer se é um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
for letra in range(1):
    p = frase[::-1]
    if p == frase:
        print('A frase digitada é um PALÍNDROMO!')
        print(f'{frase} X {p}')
    else:
        print('A frase digitada não é um PALÍNDROMO')
        print(f'{frase} X {p}')