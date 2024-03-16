# Ex 42 Refazer o Ex 35 acrescentando o recurso de mostrar o tipo do triângulo

print('\033[30m▼ \033[m' * 8)
print(' ' * 2, '\033[37mTRIÂNGULOS\033[m')
print('\033[30m▲ \033[m' * 8)

seg1 = float(input('Primeiro segmento: '))
print('\033[30m▲ \033[m' * 8)
seg2 = float(input('Segundo segmento: '))
print('\033[30m▲ \033[m' * 8)
seg3 = float(input('Terceiro segmento: '))
print('\033[30m▲ \033[m' * 8)
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg3 + seg1 > seg2:
    print('\033[34mDÁ\033[m pra formar um triângulo!')
    print('\033[30m▲ \033[m' * 8)
    if seg1 == seg2 == seg3:
        print('É um triângulo equilátero!')
    elif seg1 == seg2 != seg3  or seg2 == seg3 != seg1 or seg1 == seg3 != seg2:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
    #elif: seg1 != seg2 !=seg3 != seg1:
        #print('É um triângulo escaleno!')
else:
    print('\033[33mNÃO\033[m dá pra formar um triângulo!')
print('\033[30m▲ \033[m' * 8)

