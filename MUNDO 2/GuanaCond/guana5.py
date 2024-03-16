# Ex 39 Escreva um programa que leia o ano de nascimento de um jovem e informe:
#   Se ele vai se alistar, se está na hora ou se já passou da hora
# O programa deve mostrar o atraso ou o tempo que falta

from datetime import date

print('\033[30m# \033[m' * 20)
print(' ' * 12, '\033[37;4mALISTAMENTO\033[m')
print('\033[30m# \033[m' * 20)

genero = str(input('Qual seu genero?\n(m/f) - ')).strip().upper()

if genero == 'M':

    atual = date.today().year

    ano = int(input('Em que ano você nasceu?\n'))
    print('=' * 20)

    idade = atual - ano

    print('Você já tem \033[33m{}\033[m anos de idade!'.format(idade))

    print('=' * 20)

    if idade > 18:
        atraso = idade - 18
        if atraso == 1:
            print('Já passou da hora rapaz, está atrasado em {} ano.'.format(atraso))
            print('Seu alistamento foi em {}'.format(atual - atraso))
        else:
            print('Já passou da hora rapaz, está atrasado em {} anos.'.format(atraso))
            print('Seu alistamento foi em {}'.format(atual - atraso))
    elif idade < 18:
        falta = 18 - idade
        if falta == 1:
            print('Calma jovem, ainda tem 1 ano pela frente até lá.')
            print('Seu alistamento será em {}'.format(atual + 1))
        else:
            print('Calma jovem, ainda tem {} anos pela frente até lá.'.format(falta))
            print('Seu alistamento será em {}.'.format(atual + falta))
    else:
        print('Você já está na idade rapaz, acho bom procurar um QG.')
    
elif genero == 'F':
    print('Fique em paz, mulheres não precisam se alistar')

else:
    print('Acho que houve algum problema. Tente novamente')
print('=' * 20)
