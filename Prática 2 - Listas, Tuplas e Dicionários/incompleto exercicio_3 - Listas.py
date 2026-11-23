from random import randint

n = int(input("Lançamentos do dado: "))
lista = [0]*6

for i in range(n):
    face = randint(1,6)
    lista[face - 1] += 1

for i in range(6):
    print(f"O percentual do número {i + 1} é: {(lista[i]/n) * 100:.2f}% ")
