# Ex 60 Ler um número e mostrar seu fatorial 

num = int(input('Digite um valor: '))
'''fatorial = 1
while num > 1:
    fatorial *= num
    num = num - 1

print(fatorial)'''

fac = 1
for numero in range(num, 0, - 1):
    fac *= numero

print(fac)
