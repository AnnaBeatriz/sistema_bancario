menu = """
--------MENU--------
[1] Depositar
[2] Sacar
[3] Saldo e Limite Diário
[4] Extrato
[5] Sair
--------------------
=> """

saldo = 0
limite_diario = 1500  # Valor inicial do limite diário
limite_saque = 500  # Valor máximo por saque
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  # Número de saques permitidos por dia

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite_diario = valor > limite_diario
        excedeu_limite_saque = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_diario:
            print("Operação falhou! O valor do saque excede o limite diário.")

        elif excedeu_limite_saque:
            print(f"Operação falhou! O valor máximo por saque é de R$ {limite_saque:.2f}.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            limite_diario -= valor  # Atualiza o limite diário após o saque
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        saques_restantes = LIMITE_SAQUES - numero_saques
        valor_maximo_saque = min(limite_saque, saldo)

        print("\n------- Saldo e Limite Diário -------")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Limite Diário Restante: R$ {limite_diario:.2f}")
        print(f"Saques Restantes: {saques_restantes}")
        print(f"Valor Máximo por Saque: R$ {valor_maximo_saque:.2f}")
        print("-----------------------------------")

    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "5":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("""
      *******************************************************

        Obrigado por usar nosso banco, tenha um ótimo dia!
                            💕😘❤
      *******************************************************
      """)