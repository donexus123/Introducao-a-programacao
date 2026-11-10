numero = int(input("Digite um número inteiro positivo: "))

original = numero

contador = 0

if numero == 0:
  contador = 1
else:
  
  while numero > 0:
    numero //= 10  
    contador += 1

print("O número", original, "possui", contador, "algarismo(s).")