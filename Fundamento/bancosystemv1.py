# Menu de opções do sistema
menu = """
[d] Depósito
[l] Levantamento
[e] Extrato
[q] Sair

=> """

# Variáveis iniciais
# Saldo da conta
saldo = 0  
# Limite máximo por levantamento
limite = 500             
# Histórico de operações
extrato = ""
# Contador de levantamentos
num_levantamento = 0      
# Limite de levantamentos diários
LIMITE_LEVANT = 3

# Loop principal do programa
while True:
    opcao = input(menu)
    
    # Depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        # Verifica se o valor é válido
        if valor > 0:  
            saldo += valor
            # Registra no extrato
            extrato += f"Depósito: {valor:.2f} KZ\n"  
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # Levantamento
    elif opcao == "l":
        valor = float(input("Informe o valor do levantamento: "))
        
        # Condições para verificar se o levantamento é permitido
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_levant = num_levantamento >= LIMITE_LEVANT
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite de levantamento.")
        elif excedeu_levant:
            print("Operação falhou! Você excedeu o número de levantamentos permitidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Levantamento: {valor:.2f} KZ\n"
            # Incrementa o número de levantamentos
            num_levantamento += 1  
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # Extrato
    elif opcao == "e":
        print("\n=======================================")
        print("                EXTRATO                ")
        print("=======================================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f} KZ")
        print("\n=======================================")
        print("    Muito obrigado e volte sempre! :)")
        print("=======================================")
    
    # Sair do sistema
    elif opcao == "q":
        # Encerra o loop
        break  
    # Caso o usuário insira uma opção inválida
    else:
        print("Operação inválida, por favor selecione uma operação válida.")
