# Ex 61 Refazer exercício 51 utilizando while

primeiro_termo = int(input('\033[31mQual o primeiro termo da P.A?\n\033[m'))
razao = int(input('\033[35mQual a razão?\n\033[m'))
print(' ')

""" 
'''an11 = an1 + r(n - 1)'''
decimo_primeiro = primeiro_termo + razao * (11 - 1) # Cálculo do 11o termo
"""
n = 1

while n <= 10:
    print('\033[31m', primeiro_termo, '\033[m', end=('\033[1;34m → \033[m'))
    n += 1
    primeiro_termo += razao


print('\033[1;33mACABOU!\033[m')