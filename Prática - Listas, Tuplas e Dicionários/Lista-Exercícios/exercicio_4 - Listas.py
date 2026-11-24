from random import randint

while True:
    n = int(input("Lançamentos do dado: *0 para encerrar* "))

    if n == 0:
        break

    lista = [0] * 6

    for i in range(n):
        face = randint(1,6)
        lista[face - 1] += 1

    for i in range(6):
        print(f"O percentual do número {i + 1} é: {(lista[i]/n) * 100:.2f}% ")
