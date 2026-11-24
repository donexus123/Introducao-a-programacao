matriz = []

for linha in range(3):
    lista = []

    for coluna in range (3):
        valor = int(input(f"Digite o valor [{linha}][{coluna}]: "))
        lista.append (valor)

    matriz.append(lista)

print ("\nMatriz:")
for linha in matriz:
    print(linha)

pesquisa = int(input("\nDigite um valor para pesquisar: "))

if any(pesquisa in linha for linha in matriz):
    print("O valor pertence á matriz!")

else:
    print("O valor não pertence a matriz.")
