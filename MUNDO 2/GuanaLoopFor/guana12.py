# Ex 56 Ler nome, idade e sexo de 4 pessoas
#   e mostrar a média de idade, nome do homem mais velho
#   e quantas mulheres tem menos de 20 anos

total_idade = 0
m = 0
for p in range(1,5):
    print('{:=^21}'.format(f'{p}ª PESSOA'))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    total_idade += idade

    if idade < 20 and sexo == 'F':
        m += 1
    
    if sexo ==  'M' and p == 1:
        velho = idade
        n = nome
    else:
        if sexo == 'M' and idade > velho:
            velho = idade
            n = nome


        
media = total_idade / 4

print(f'A média da idade do grupo é {media:.1f}.')
print(f'O homem mais velho tem {velho} anos e seu nome é {n.capitalize()}.')
print(f'Ao todo são {m} mulheres com menos de 20 anos.')