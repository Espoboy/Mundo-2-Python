# Ex 65 Ler vários números inteiros, mostrar a média entre eles e dizer
    # qual foi o menor e qual foi maior e perguntar se quer digitar mais

maior = menor = soma = contagem = 0
escolha = ''

while escolha != 'N':
    valor = float(input('Digite um valor: '))
    escolha = str(input('Você deseja continuar? [S/N]\n').upper().strip())
    contagem += 1
    soma += valor
    if contagem == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor 

media = soma / contagem

print(f'A média entre os números digitados é de {media:.1f}.')
print(f'O maior valor foi {maior:.1f} e o menor foi {menor:.1f}.')