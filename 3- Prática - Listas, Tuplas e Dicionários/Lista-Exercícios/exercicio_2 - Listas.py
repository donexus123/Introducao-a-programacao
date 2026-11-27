matriz = []

for linha in range(3):
    lista = []

    for coluna in range (3):
        valor = int(input(f"Digite o valor [{linha}][{coluna}]: "))
        lista.append (valor)

    matriz.append (lista)

print ("\nPrimeira Matriz:")
for linha in matriz:
       print(linha)

for i in range (3):
            temp = matriz[1][i]
            matriz[1][i] = matriz[i][1]
            matriz[i][1] = temp

print ("\nSegunda Matriz:")
for linha in matriz:
       print(linha)
