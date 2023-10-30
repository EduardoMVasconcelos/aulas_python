tabuada = int(input("Informe um numero para a tabuada: "))
lista = []
numero = 1

for i in range(1, 10+1):
    lista.append(3*numero)
    numero +=1 
print(f"Tabuada do  {tabuada}: {lista}")