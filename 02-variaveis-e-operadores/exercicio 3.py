senha_correta = "dudu"
senha = input("Digite sua senha: ")
contador = 1 

while senha != senha_correta:
  if contador >= 3:
    print("Você excedeu o limite de tentativas!")
    break

  print("Senha inválida!")
  senha = input("Digite novamente sua senha: ")
  contador += 1
else:
  print("Login realizado com sucesso!")
