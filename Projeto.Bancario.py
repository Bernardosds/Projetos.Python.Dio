menu = """
Escolha a Opção desejada:

[1]Depositar
[2]Sacar
[3]Extrato
[4]Sair 

=>"""
menu_deposito = """
Digite o valor a ser depositado(Para cancelar a operação digite 0): """
menu_saque = """
Digite o valor que você quer sacar da conta(Limite de 500 Reais por saque): """
saldo = float(0)
limite = float(500)
lista_extrato = [""]
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
        opcao = input(menu)

        if opcao == "1":
                while True:
                        try:
                                deposito = float(input(menu_deposito)) 
                        except ValueError:
                                print("Por favor insira um valor numérico válido para o depósito.")
                                continue
                        if deposito > 0:
                                saldo += deposito
                                lista_extrato.append(f"Deposito de R$ {deposito} Saldo após transação: {saldo}")
                                print("\nDepósito realizado com sucesso!")
                                break
                        elif deposito == 0:
                                print("\nOPERAÇÃO CANCELADA!")
                                break 

                        else: 
                                print("O valor para depósito deve ser positivo e maior do que zero!")
        elif opcao == "2":
                while True:
                        try:
                                saque = float(input(menu_saque)) 
                        except ValueError:
                                print("Por favor insira um valor numérico válido para sacar.")
                                continue
                        if saque > 0 and saque <= limite and saque <= saldo and numero_saques < LIMITE_SAQUES:
                                print("Você sacou R$", saque)
                                saldo -= saque
                                lista_extrato.append(f"Saque de R$ {saque}    Saldo após transação: {saldo}")
                                numero_saques += 1
                                break
                        elif saque == 0:
                                print("\nOPERAÇÃO CANCELADA!")
                                break
                        elif saque < 0:
                                print("Você só pode sacar valores positivos, tente novamente!")
                        elif numero_saques == 3:
                                print("Você já ultrapassou o limite de saques diários, tente novamente amanhã!")
                                break 
                        elif saque > 500:
                                print("O limite para saques é de R$ 500")
                        elif saque > saldo:
                                print(f"Saldo insuficiente! Seu saldo é: {saldo}")

                      
        elif opcao == "3":
            lista_extrato.append(f"SALDO ATUAL: {saldo}")
            print("EXTRATO: ")
            print("\n".join(lista_extrato))
            lista_extrato.pop()
            input("Pressione ENTER para continuar")


        elif opcao == "4":
                break
        else:
                print("\nOpção inválida tente novamente!")
