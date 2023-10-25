inicio = int(input("Informe o inicio: "))
fim = int(input("Informe o fim: "))
lista = []

for i in range(fim, inicio-1, -1):
    lista.append(i)
print(lista)