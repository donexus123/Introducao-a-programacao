from random import randint

n = int(input("digite quantas vezes o dado será rodado:"))
lista = [0] * 6

for i in range (n):
    dado = randint(1,6)
    lista[dado - 1] += 1

for i in range(6):
    print(f"O percedual do número {i + 1} é: {(lista[i]/n) * 100:.2f}% ")
