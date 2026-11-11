saldo = 1.50
numero = 0

while numero != (4):

    numero = int(input("<1> Depositar "
    "<2> Sacar "
    "<3> Consultar saldo "
    "<4> Sair "
    "Digite o valor da opção: "))
    if numero == 1:
        deposito = int(input("Digite o valor que quer depositar: "))
        deposito += saldo
        print("Sucesso! seu saldo atual disponível é:", saldo)

    if numero == 2:
        sacar = float(input("Digite o valor que quer sacar: "))
        if sacar > saldo:
            print ("Saldo insuficiente")
        else:
            saldo -= sacar
            print("Sucesso! o valor está sendo sacado, seu saldo restante é:", saldo)

    if numero == 3:
        print("Seu saldo atual disponível é:", saldo)

    if numero == 4:
            print("Volte sempre!")

    input()

print ("Volte sempre!")
