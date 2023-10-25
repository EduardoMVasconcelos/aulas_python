quantidade = int(input("Informe a quantidade de numeros da lista: "))
contador = 1
soma = 0
lista = []

for i in range(1, quantidade+1):
    numero = int(input(f"Informe o {contador}º numero: "))
    contador += 1
    lista.append(numero)
    soma += numero
    mult *= numero