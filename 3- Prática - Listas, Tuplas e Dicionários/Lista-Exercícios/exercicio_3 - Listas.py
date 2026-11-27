mensagem = []
alfabeto = " abcdefghijklmnopqrstuvwxyz"

entrada = input("Digite os números criptografados separados por vírgula: ")
numeros = entrada.split(",")

for item in numeros:
    numero = int(item)
    letra = alfabeto[numero]
    mensagem.append(letra)

print("".join(mensagem))
