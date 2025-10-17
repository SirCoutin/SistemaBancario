def Deposito(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de {valor:.2f} concluído! Seu saldo atual é de: {saldo:.2f}")
        print(f"Operação sucedida! Seu novo saldo é: {saldo:.2f}")
    else:
        print("Operação Falhou!")
    return saldo, extrato

def Saque(saldo, valor, extrato, numero_saques):

        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque de {valor:.2f} concluído! Seu saldo atual é de: {saldo:.2f}")
        print(f"Saque feito com sucesso! Seu novo saldo é: {saldo:.2f}")
        return saldo, numero_saques, extrato

def Extrato(extrato):
    num_op = 0
    print("Seu Extrato: ")
    for extratos in extrato:
        num_op += 1
        print(f"{num_op}: {extratos}")

def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    
    usuarios[nome] = {'Data Nascimento': data_nascimento, 
                      'CPF': cpf, 
                      'Endereço': endereco}
    
    return usuarios


def Main():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    numero_contas_novas = 0
    usuarios = {}

    while True:

        opcao = input(menu)

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: "))

            if saldo < valor:
                print("\nOperação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("\nOperação falhou! O valor do saque excede o limite.")
            elif numero_saques > LIMITE_SAQUES:
                print("\nOperação falhou! Número máximo de saques excedido.")
            elif valor < 0:
                print("\nOperação falhou! Número inválido!.")
            else:
                saldo, extrato= Deposito(saldo, valor, extrato)
            
        
        elif opcao == "s":

            print(f"Seu saldo atual é de: {saldo:.2f}")
            valor = float(input("Informe o valor do saque: "))

            if valor > 0:
               print("\nOperação Falhou!")
            else:
                saldo, numero_saques, extrato = Saque(saldo, valor, extrato, numero_saques)

        elif opcao == "e":
            Extrato(extrato)

        elif opcao == "u":
            nome = input("Informe seu nome completo: ")
            data_nascimento = input("Informe sua data de nascimento (no padrão dd/mm/yy): ")
            cpf = input("Informe seu CPF: ")
            endereco = input("Informe seu endereço: ")
            
            if cpf in usuarios.get(nome, {}).get(cpf, {}):
                print("CPF já cadastrado!")
            else:
               usuarios = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

            print(usuarios)

        elif opcao == "q":
            break

Main()