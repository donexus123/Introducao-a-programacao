h = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M para homem ou F para mulher): ")

if sexo == "M":
    peso = (72.7 * h) - 58
    print("O peso ideal é:", peso)
if sexo == "F":
    peso = (62.1 * h) - 44.7
    print("O peso ideal é:", peso)
