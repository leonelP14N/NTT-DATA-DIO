import textwrap

def menu():
    # Menu
    return input(textwrap.dedent("""
        ================ MENU ================
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        => """))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: {valor:.2f}\tAKZ\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, num_levant, limite_levant):
    if valor > saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! Excede o limite de levantamento. @@@")
    elif num_levant >= limite_levant:
        print("\n@@@ Operação falhou! Limite de levantamentos excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Levantamento: {valor:.2f}\tAKZ\n"
        num_levant += 1
        print("\n=== Levantamento realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
        print("\n=======================================")
        print("                  EXTRATO                ")
        print("=======================================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: {saldo:.2f}\t\tAKZ.")
        print("\n=======================================")
        print("    Muito Obrigado e Volte sempre! :)")
        print("=======================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Usuário já existente! @@@")
    else:
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nº - bairro - cidade/estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado! @@@")

def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}\nC/C: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}")
    print("=" * 40)

def main():
    # Constantes e variáveis principais
    LIMITE_LEVANT = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    num_levant = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do levantamento: "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, num_levant, LIMITE_LEVANT)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida, tente novamente.")

main()