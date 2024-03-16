# Ex 40 Criar um programa que leia duas notas de um aluno calculando sua média
#   < 5 REPROVADO, >= 5 e < 7 RECUPERAÇÃO, >= 7 APROVADO

print('\033[35mx+\033[m' * 10)
print(' ' * 3, '\033[32mMÉDIA FINAL\033[m')
print('\033[35mx+\033[m' * 10)

n1 = float(input('Primeira nota: '))
print('\033[35mx+\033[m' * 10)
n2 = float(input('Segunda nota: '))
print('\033[35mx+\033[m' * 10)

media = (n1 + n2) / 2

print('Sua média foi {:.1f}.'.format(media))

print('\033[35mx+\033[m' * 10)


if media < 5:
    print('\033[31mREPROVADO!\033[m Esse não foi o seu ano rapaz...')
elif 7 > media >= 5:
    print('\033[34mRECUPERAÇÃO!\033[m Você tem uma chance ainda!')
else:
    print('\033[32mAPROVADO!!!!\033[m Parabéns, você se saiu muito bem esse ano!')

print('\033[35mx+\033[m' * 10)
