n = int(input("Informe a quantidade de valores: "))
soma = 0

for i in range(1, n+1):
    numero = int(input("Informe os numeros: "))
    soma += numero
    
print(f"A média aritmética é = {soma/n}")