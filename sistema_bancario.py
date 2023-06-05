"""
Sistema bancário para desafio de projeto
Formação Python Developer - DIO
Aluno: Paulo Jonas Alves da Silva
"""

menu = """
########### SYS-BANK ###########

[D] - DEPOSITAR
[S] - SACAR
[E] - EXTRATO
[Q] - SAIR

########### ######## ###########

=>"""

saldo = 0
limite = 500

numero_depositos = 0

numero_saques = 0
LIMITE_SAQUES = 3

extrato = f"""
########### EXTRATO ###########


"""

while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        valor_deposito = float(input("Informe o valor para depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            movimento_deposito = f"\nDepósito - Valor de R$ {valor_deposito:4.2f}\n"
            extrato += movimento_deposito
            numero_depositos += 1
        else:
            print("Valor inválido. Tente novamente.")


    elif opcao.upper() == 'S':
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Informe o valor do saque: "))
            if valor_saque <= limite and valor_saque <= saldo:
                saldo -= valor_saque
                movimento_saque = f"\nSaque - Valor de R$ {valor_saque:4.2f}\n"
                extrato += movimento_saque
                numero_saques += 1
            elif valor_saque > limite:
                print(f"Valor superior ao limite de saque: R$ {limite:.2f}")
            else:
                print("Não há saldo suficiente.")
        else:
            print("Número de saques atingidos.")


    elif opcao.upper() == 'E':
        if numero_saques == 0 and numero_depositos == 0:
            print(extrato + "\n\nNão há movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual - R$ {saldo:4.2f}\n")

    elif opcao.upper() == 'Q':
        print("Obrigado por usar nosso sistema.")
        break

    else:
        print("Operação inválida, obrigado por usar nosso sistema.")
