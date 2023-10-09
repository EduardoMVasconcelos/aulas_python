tabuada = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
termino = int(input("Terminar em: "))

if comeco < termino:
    print(f"Vou montar a tabuada de {tabuada} começando em {comeco} e terminando em {termino}")
    for i in range(comeco, termino+1):
        print(f"{tabuada} x {i} = {tabuada*i}")

else: 
    print("Inválido")