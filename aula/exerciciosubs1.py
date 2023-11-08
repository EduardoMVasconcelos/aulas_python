media_positiva = 0 
lista_positiva = []

for i in range(1, 11):
    nome = input("Informe o nome do Aluno: ")
    nota1 = float(input("Informe a nota 1: (0 - 10)"))
    nota2 = float(input("Informe a nota 2: (0 - 10)"))
    nota3 = float(input("Informe a nota 3: (0 - 10)"))
    nota4 = float(input("Informe a nota 4: (0 - 10)"))
    media = (nota1+nota2+nota3+nota4)/4
    if media >= 7:
        media_positiva +=1
        lista_positiva.append(nome)
print(f"A quantidade de alunos com a media positiva é de {lista_positiva}")
    