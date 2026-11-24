alturas = []
sexos = []

for i in range(10):
    altura = float(input(f"Pessoa nº: {i + 1} Digite a sua altura: "))
    sexo = input("Digite o sexo (Masc/Fem): ")

    alturas.append(altura)
    sexos.append(sexo)

menor = min(alturas)
maior = max(alturas)
pos_maior = alturas.index(maior)
pos_menor = alturas.index(menor)

print("Maior Altura: ", maior)
print("Sexo da pessoa mais alta é: ", sexos[pos_maior])

print("Menor Altura: ", menor)
print("Sexo da pessoa mais baixa é: ", sexos[pos_menor])
