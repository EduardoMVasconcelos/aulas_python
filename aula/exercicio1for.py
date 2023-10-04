par = 0
impar = 0

for i in range(1, 11):
    numeros = int(input("Informe um numero inteiro: "))
    if numeros % 2 == 0:
        par += 1
    elif numeros % 2 != 0:
        impar += 1

print(f"A quantidade de numeros pares é = {par}")
print(f"A quantidade de numeros pares é = {impar}")
