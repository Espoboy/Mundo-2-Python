# Ex 62 Melhorar o Ex 61 perguntando se quer mostrar mais termos
#   o programa encerra quando o usuário disser 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

a = 1

while a <= 10:
    print('\033[31m', primeiro_termo, end='\033[34m → \033[34m')
    a += 1
    primeiro_termo += razão

# a = 11 aqui

print('\033[1;33m PAUSA \033[m')


escolha = 1
while escolha != 0:
    escolha = int(input('\033[32mQuantos termos você quer mostrar a mais? (Digite 0 para encerrar)\n\033[m'))
    a = 1
    while a <= escolha:
        print('\033[31m', primeiro_termo, end='\033[34m → \033[34m')
        a += 1
        primeiro_termo += razão

