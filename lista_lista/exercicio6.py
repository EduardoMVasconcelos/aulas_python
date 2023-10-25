quantidade = int(input("Informe a quantidade de itens da lista: "))
contador = 0
lista = []

for i in range(1, quantidade+1):
    numero = int(input(f"Informe o numero de indice {contador} da lista: "))
    contador += 1
    lista.append(numero*2)
print(lista)
    
