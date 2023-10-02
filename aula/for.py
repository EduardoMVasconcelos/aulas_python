# Exemplo 1: Escreva um programa em Python
# para exibir os números de 1 até 5 no terminal
#-----------------------------------------------------
# Exemplo 2: Faça um programa que leia um valor
# inteiro e mostre a tabuada de 1 até 10 do valor lido

#range(stop)
#range(start, stop)
#range(start, stop, step)

#for cont in rang(5, 0, -1):
#    print(cont)

#num = int(input("informe um numero para a tabuada: "))

#for cont in range(1, 11):
#    print(f"{num} x {cont} = {num*cont}")

n = int(input("Informe a quantidade de notas: "))
soma = 0

for cont in range (1, n+1):
    notas = float(input("Informe as notas: "))
    soma = soma + notas
print(soma/n)
