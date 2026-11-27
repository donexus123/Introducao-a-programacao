def main():
    frase = input("digite uma frase(1 para encerrar): ").lower()

    if frase == "1":
        print("programa encerrado")

    else:
        dicionario = {}

        for letra in frase:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario [letra] = 1

        print (dicionario)

main()
