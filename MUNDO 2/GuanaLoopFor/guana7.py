# Ex 51 Ler o primeiro termo e a razão de uma PA e mostrar os 10 termos
t = int(input('\033[31mQual o primeiro termo da P.A?\n\033[m'))
r = int(input('\033[35mQual a razão?\n\033[m'))
print(' ')
a = t + r * (11 - 1) # Cálculo do 11o termo
for c in range(t, a, r): # O a é o 11o pq só vai até o 10o
    print(c, end=' → ')
print('\033[1;33mACABOU!\033[m')