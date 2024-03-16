# Ex 55 Ler o peso de 5 pessoas e mostrar o maior e o menor
#   Método Guanabara. Não resolvi completamente só.
print('Digite o peso dos candidatos.')
for c in range(1, 6):
    peso = float(input(f'Candidato {c}: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print(f'O menor peso foi de {menor}kg e o maior foi de {maior}kg.')
