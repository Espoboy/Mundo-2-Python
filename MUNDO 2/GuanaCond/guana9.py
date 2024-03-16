# Ex 43 Calcular IMC

print('\033[34m↓ \033[m' * 14)
print(' ' * 3, "\033[32mCALCULADORA DE IMC\033[m")
print('\033[34m↑ \033[m' * 14)

peso = float(input("Kilos: "))
altura = float(input("Metros: "))

imc = (float(peso) / float(altura ** 2))
print ("Seu IMC é de: {:.1f}".format(imc))

print('\033[34m↓ \033[m' * 14)

if imc < 18.5:
    print("Magreza, Obesidade Grau 0.")
elif imc >= 18.5 and imc < 25:
    print("Normal, Obesidade Grau 0.")
elif 25 <= imc < 30:
    print("Sobrepeso, Obesidade Grau 1.")
elif 30 <= imc <= 39.9:
    print("Obesidade, Obesidade Grau 2.")
elif imc >= 40:
    print("Obesidade Mórbida, Obesidade Grau 3.")
print('\033[34m↑ \033[m' * 14)
    