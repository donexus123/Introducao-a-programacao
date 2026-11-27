ganho = float(input("Quanto você ganha por hora: "))
horas = float(input("Número de horas trabalhadas: "))

bruto = ganho * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print("Salário Bruto: R$", bruto)
print("IR (11%): R$", ir)
print("INSS (8%): R$", inss)
print("Sindicato (5%): R$", sindicato)
print("Salário Liquido: R$", liquido)
