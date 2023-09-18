numero = int(input("Informe o numero impar: "))
contador = 1

while contador <= numero:
    if numero %2 != 0:
        print(numero)
        numero -= 2
        contador +=1