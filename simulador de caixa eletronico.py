saldo = float(1000)

print("Bem vindo ao seu banco!")

while True:
    print("Caixa Eletronico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Saldo")
    print("3 - Retirar Saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opcao (1 - 4): "))

    if opcao == int(1):
        print("O seu saldo e de R${:.2f}".format(saldo))
        print("\n")
    elif opcao == int(2):
        deposito = float(input("Quanto deseja depositar? "))

        if deposito > 0:
            saldo += deposito
            print("Voce depositou R$ {:.2f}".format(deposito))
            print("\n")
        else:
            print("Valor de deposito invalido!")
        print("\n")

    elif opcao == int(3):
        tirar = float(input("Quanto deseja retirar? "))
        print("\n")
        saldo -= tirar
        
    elif opcao == int(4):
        print("Muito obrigado por sua visita! Ate mais breve!")
        break
        
    else:
        print("Codigo errado, tente novamente")
        print("\n")
