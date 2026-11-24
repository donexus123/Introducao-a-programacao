vetor1 = []
vetor2 = []
vetor3 = []

for i in range(5):
    valor = int(input(f"Digite o {i + 1}º do vetor 1: "))
    vetor1.append(valor)

for i in range(5):
    valor = int(input(f"digite o {i + 1}º do vetor 2: "))
    vetor2.append(valor)

for i in range(5):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3:", vetor3)
