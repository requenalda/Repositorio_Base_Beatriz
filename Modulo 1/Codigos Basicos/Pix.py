opcao = int(input("Digite o que deseja fazer: \n1- Fazer o Pix\n2-Extrato\n3-Depositar\n4-Sair"))
if opcao == 1:
    valor = input("Digite o valor a mandar: ")
    quem = input("Digite para quem eu vou mandar (@Layslao)")
    print("Pix realizado com sucesso !! 🤑")
elif opcao ==2:
    valor = input("Extrato: ")
    quem = input("Ver meu extrato (@Layslao) ")
    print("Extrato aberto com sucesso")
elif opcao ==3:
    valor = input("Digite o valor para deposita: ")
    quem = input("Digite para quem vou depositar (@Layslao)")
    print("Deposito realizado com sucesso")
else:  
    quem = input("quem vai sair (@Layslao)")
    print("saiu do app")
