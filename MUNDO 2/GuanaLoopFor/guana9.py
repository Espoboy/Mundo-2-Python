# Ex 53 Ler uma frase e dizer se é um palíndromo

# Método Guabnabara

frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
if junto == inverso:
    print('É um PALÍNDROMO!')
else:
    print('Não é um PALÍNDROMO!')
print(junto, inverso)