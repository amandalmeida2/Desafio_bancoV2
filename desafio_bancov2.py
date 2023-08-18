# Criar as opções que serão mostradas ao usuário: String múltipla precisa ser definidar por 3 aspas duplas ou simples
def menu ():
    menu = """  
    Selecione a operação a ser realizada:
        
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar conta corrente
    [6] Listar contas
    [7] Sair

    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
            
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
            
        print(f"\n Depósito realizado com suscesso no valor de {valor:.2f}")
            
        print(f"\n Seu saldo atual é: R$ {saldo:.2f} ")
    else:
        print("Operação falhou! O valor informado é inválido")  
    return saldo, extrato
            
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
        
    excedeu_limite = valor > limite
        
    excedeu_saques = numero_saques >= limite_saques
        
        
    if excedeu_saldo:
        
         print ("Operação falhou! Você não tem saldo suficiente!")
            
    elif excedeu_limite:
        
        print ("Operação falhou! Valor informado está acima do limite!")
            
    elif excedeu_saques:
        
                print ("Operação falhou! Você atingiu o número diário de saques!")
        
    elif valor > 0:
            
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
                
        print(f"Saque realizado com sucesso no valor de: R$ {valor:.2f}")
                
        print(f"\n Seu saldo atual é: R$ {saldo:.2f} ")
            
    else:
            
        print("Operação falhou! O valor informado é inválido")
    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print("\n ........ EXTRATO ..........")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("..............................")
    
def criar_usuario(usuarios):
    cpf = input("informe o seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("/n Já existe usuário com este CPF! ")
        return

    nome=input("Digite seu nome completo: ")
    data_nascimento=input("digite sua data de nascimento (dd-mm-aaaa): ")
    endereco=input("Digite seu endereço (logradouro, n° - bairro - cidade/sigla do estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")
        
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf= input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
         print("Conta criada com sucesso! ")
         print(f"\n Agência: {agencia}")
         print(f"\n Número da conta: {numero_conta}")
         print(f"\n Usuário: {usuario}")
         return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)    
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == "1": 
            
            valor = float(input("Informe o valor do depósito "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
    
            print(f"\nO seu saldo é R$: {saldo:.2f} ")
            
            print("\nO limite para saque é de R$ 500,00")

            valor = float(input("\nInforme o valor do saque "))
            
            saldo, extrato =sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,                  
            )
                                   
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuario(usuarios)
            
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            
        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "7":
            break
        else:
            print("operação inválida! Por favor, selecione novamente a operação desejada") # Caso a opção digitada não está dentro da especificação do menu
     

main ()