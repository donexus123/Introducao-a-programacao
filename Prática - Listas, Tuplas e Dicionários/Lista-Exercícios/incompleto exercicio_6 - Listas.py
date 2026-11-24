pontos = []

n = int(input("Quantos pontos deseja informar? "))

for i in range(n):
    x = float(input(f"Digite a coordenada de x do ponto {i + 1}: "))
    y = float(input(f"Digite a coordenada de y do ponto {i + 1}: "))

    pontos.append((x , y))

distancias = []

for i in range(n):
    for j in range(i + 1, n):
        x1 = pontos[i][0]
        y1 = pontos[i][1]

        x2 = pontos[j][0]
        y2 = pontos[j][1]

        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        distancias.append(distancia)
