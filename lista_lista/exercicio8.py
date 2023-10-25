quantidade = int(input("Informe a quantidade de notas: "))
contador = 1
lista = []
notas = 0 

for i in range(1, quantidade+1):
    nota = float(input(f"Informe a {contador}º nota: "))
    contador += 1
    lista.append(nota)
    notas += nota
print(f"Notas: {lista}")
print(f"Média: {notas/quantidade}")