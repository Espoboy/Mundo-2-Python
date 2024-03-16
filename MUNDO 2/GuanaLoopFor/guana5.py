# Ex 49 Tabuada de um número que o usuário escolher

c = int(input('Qual valor você quer na nossa tabuada?\n'))
print(' ')
for n in range(1,11):
    print(f'{n:2}', 'x', c, '=', (n * c))