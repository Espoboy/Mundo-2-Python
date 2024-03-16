# Ex 64 Ler vários números inteiros, o programa para se o user digitar 999
    #Mostrar quantos números foram digitados e a soma entre eles

print('----Bem-Vindo----')
contagem = 0
soma = 0
encerrar = 999
num = 0
while num != 999:
    num = int(input('Digite um valor [999 Para encerrar]: '))
    if num != 999:    
        contagem += 1
        soma += num
print(f'Você digitou {contagem} números.')
print(f'A soma entre esses números equivale a {soma}')