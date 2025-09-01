print("--- Sistema Bancário ---")
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] sair
=> """

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "s":
        if numero_saques < limite_saques:
            valor = float(input("Informe o valor a ser sacado: "))
            if valor <= saldo:
                saldo -= valor
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de saques atingido!")

    elif opcao == "e":

        print("\n============EXTRATO BANCARIO===========") 
        print("Não foram realizadas movimentações.")
        print(f"Extrato: R$ {saldo:.2f}")
        print("=========================================")
        

    elif opcao == "x":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        


