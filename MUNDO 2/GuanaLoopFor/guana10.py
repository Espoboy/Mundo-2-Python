# Ex 54 Ler o ano de nascimento de 7 pessoas e mostrar quantas são maiores
#   e quantas são menores de idade
print('Digite o ano de nascimento.')
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Pessoa {c}:'))
    idade = date.today().year - ano
    if idade >= 21  :
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores.')
    