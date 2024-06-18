import textwrap

def menu():
        menu = """
        Escolha a Opção desejada:

        [1]Depositar
        [2]Sacar
        [3]Extrato
        [4]Sair 
        [5]Criar Novo Usuário
        [6]Criar Conta Corrente

        =>""" 
        return input(textwrap.dedent(menu))
def criar_usuario():
        while True:
                print("Por favor, informe os dados de usuário abaixo: ")
                cpf = input("CPF: ").replace('.','').replace('-','')
                for usuario in usuarios:
                        if usuario["cpf"] == cpf:
                                print("Já existe um usuário com este CPF")
                                break
                else: 
                        print("Podemos prosseguir com o cadastro") 
                        nome = input("Nome: ")
                        data_nascimento = input("Data de nascimento no formato: DD/MM/AAAA: ")
                        endereco= input("Endereço (Logradouro, Numero - bairro - cidade/sigla estado): ")
                        usuario = {
                            "nome":nome, "cpf":cpf, "data":data_nascimento,"endereco":endereco 
                        }
                        usuarios.append(usuario)
                        break
                break   

def criar_conta(numerodaconta):
        cpf = input("Digite seu CPF:")
        for usuario in usuarios:
                if usuario["cpf"] == cpf:
                        print("Conta Criada com Sucesso!")
                        contas.append({"cpf":cpf ,"numero": numerodaconta,"agencia": agencia})
                        print(f"Contas{contas}")
                        numerodaconta += 1
                        break 
        else: print("Usuário não cadastrado!")
        return numerodaconta
                      
def deposito(saldo):
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
        return  saldo

def saque(saldo,numero_saques):
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
        return saldo, numero_saques        

def extrato():
        lista_extrato.append(f"SALDO ATUAL: {saldo}")
        print("EXTRATO: ")
        print("\n".join(lista_extrato))
        lista_extrato.pop()
        input("Pressione ENTER para continuar")

menu_deposito = """
Digite o valor a ser depositado(Para cancelar a operação digite 0): """
menu_saque = """
Digite o valor que você quer sacar da conta(Limite de 500 Reais por saque): """
saldo = float(0)
limite = float(500)
lista_extrato = [""]
numero_saques = 0
LIMITE_SAQUES = 3 
usuarios =[]
numerodaconta = 1
agencia = "0001"
contas = []


while True:
        opcao = menu()

        if opcao == "1":
                saldo = deposito(saldo)

        elif opcao == "2":
                saldo, numero_saques = saque(saldo,numero_saques)
 
        elif opcao == "3":
                extrato()

        elif opcao == "4":
                break
        
        elif opcao == "5":
                criar_usuario()

        elif opcao == "6":
                numerodaconta = criar_conta(numerodaconta)

        else:
                print("\nOpção inválida tente novamente!")
