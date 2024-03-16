# Ex 57 Ler o sexo de uma pessoa, porém só aceita o valor M ou F

print('----Bem Vindo----')
sexo = ''
while sexo == '':
    sexo = str(input('Digite seu gênero [M/F]:')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        sexo = ''
        print('Tente outra vez!')
print('Fim!')