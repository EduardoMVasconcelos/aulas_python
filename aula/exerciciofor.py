print("Conta de adição!")
lista = []
resposta = "S"

while resposta == "S":
    numero = float(input("Informe um numero: "))
    numero2 = float(input("Informe outro numero: "))
    soma = numero + numero2
    lista.append(soma)
    resposta = input("Deseja realizar outra adição? [S ou N]: ")
print("Fim das adições")
print(f"Resultados: {lista}")