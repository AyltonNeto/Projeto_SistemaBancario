def menu():
    operacao = input('\nQual operação deseja realizar?\n[T]Trocar Conta\n[C]Criar Conta\n[E]Ver Extrato\n[D]Depositar\n[S]Sacar\n[Q]Sair\n\n')
    return operacao

def numerico(valor):
    try: float(valor)
    except ValueError: return False
    return True

def deposito(conta, operacao, /):
    while operacao != 'R':
        valor = input('\nQual valor deseja depositar? Para retornar ao menu digite[R]\n')
        if numerico(valor) and float(valor) > 0:
            conta['saldo'] += float(valor)
            print('\n=== Operação realizada com sucesso! ===')
            cont_dep = len(conta['registros'])
            conta['registros'][f'{cont_dep}º Depósito'] = f'{valor}'
            print('\nRetornando ao menu de operações...')
            operacao = 'R'
        elif valor == 'R' or valor == 'r':
            operacao = 'R'
        else: print('\nDefina um valor possível!')
    return

def saque(*, conta, operacao, limite_saque):
    while operacao != 'R':
        valor = input('\nQual valor deseja sacar? Para retornar ao menu digite[R]\n')
        if conta['cont_saq'] == 3:
            print('\nLimite de 3 saques diários atingido!')
            operacao = 'R'
        
        elif valor == 'R' or valor == 'r':
            operacao = 'R'
        
        elif numerico(valor) and float(valor) > conta['saldo']:
            print(f'\nValor maior que saldo disponível!\nSaldo = R${conta["saldo"]}0')

        elif numerico(valor) and float(valor) <= limite_saque and float(valor) > 0:
            conta['saldo'] -= float(valor)
            print('\nOperação realizada com sucesso!')
            conta['cont_saq'] += 1
            conta['registros'][f'{conta["cont_saq"]}º Saque'] = f'{valor}'
            print('\nRetornando ao menu de operações...')
            operacao = 'R'
            
        elif numerico(valor) and float(valor) > limite_saque:
            print(f'\nValor superior ao seu limite de saque\nLimite de Saque = R${limite_saque}0')
        
        else:
            print('\nOperação Falhou! Informe um valor válido!')
    return

def extrato(conta):
    print(f'\n  Agência: {conta["agencia"]} C/C: {conta["numero_conta"]}\n+========== EXTRATO ============+')
    if not conta['registros']:
        print('|Não foram realizadas operações!|\n+===============================+')
    else:
        cont_reg = 0
        for registro, quantia in conta['registros'].items():
            cont_reg += 1
            quantia = f'{float(quantia):.2f}'
            if "Depósito" in registro:
                print(f'| {str(cont_reg).zfill(3)} Depósito   +R$ {quantia.ljust(11)}|')
            
            else: 
                print(f'| {str(cont_reg).zfill(3)} Saque      -R$ {quantia.ljust(11)}|')
        print(f'|-------------------------------|\n| Saldo = R$ {float(conta["saldo"]):.2f}\t\t|','\n+===============================+')
    return

def criar_usuario(usuarios):
    print('\nPara realizarmos o seu cadastro precisamos seguintes informações:')
    confirmado = 'N'
    while confirmado == 'N':
        nome = input('\nNome Completo: ')
        dt_nascimento = input('\nData de Nascimento(xx/xx/xxxx): ')
        cpf = input('\nCPF(somente números): ')
        logradouro = input('\nLogradouro(sem o numero): ')
        numero = input('\nNumero: ')
        bairro = input('\nBairro: ')
        cidade = input('\nCidade: ')
        sigla = input('\nEstado(sigla): ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{sigla}'
        while True:
            confirmacao = input(f'\n\nNome: {nome}\nData de Nascimento: {dt_nascimento}\nCPF: {cpf}\nEndereço: {endereco}\n\nOs dados estão corretos?[S/N]\n')
            if usuario_repetido(cpf, usuarios):
                print('\n ### Já existe um usuário com esse CPF! ###')
                confirmacao == input('\nGostaria de tentar novamente?[S/N]')
                break
            elif confirmacao == 'S' or confirmacao == 's':
                confirmado = 'S'
                break
            elif confirmacao == 'N' or confirmacao =='n':
                break
            else: print('\n### Opção Inválida! ###')
    usuarios.append({'nome': nome, 'data de nascimento': dt_nascimento, 'CPF': cpf, 'endereco': endereco })
    print('\n=== Usuário Criado com Sucesso! ===')
    return 

def usuario_repetido(cpf, usuarios):
    for usuario in usuarios:
        if usuario['CPF'] == cpf: return True, usuario
    return False, False

def usuario_possui_conta(cpf, usuarios):
    for usuario in usuarios:
        if usuario['CPF'] == cpf and 'conta' in usuario: return True
    return False

def criar_conta(AGENCIA, contas, cpf, num_conta, usuarios):
    contas.append({'agencia': AGENCIA, 'numero_conta': num_conta, 'CPF': cpf, 'registros': {}, 'saldo': 0, 'cont_saq': 0})
    for usuario in usuarios: 
        if usuario['CPF'] == cpf: usuario['conta'] = True

def selecionar_conta(cpf, contas):
    cont_conta = 0
    for conta in contas:
        if conta['CPF'] == cpf:
            print(f'\n\tOpção[{cont_conta}]\n\n Saldo:\t\tR${float(conta["saldo"]):.2f}\n Agência:\t{conta["agencia"]}\n C/C:\t\t{conta["numero_conta"]}')
            cont_conta += 1
    conta_escolhida = int(input('\nSelecione a opção com a conta desejada: '))
    try: contas[conta_escolhida]
    except IndexError: return print('\n### Opção Invalida! Tente novamente! ###'),selecionar_conta(cpf, contas)
    return contas[conta_escolhida]

def main():
    # Declaração de Variáveis
    LIMITE_SAQUE = 500.0
    AGENCIA = '0001'
    contas = []
    usuarios = []
    controle_app, num_conta = 1, 0

    # Início do Programa
    while True:
        # Login
        if controle_app == 1:
            print('\nBem vindo ao Banco Ipim LTDA!')
            verificacao = input('\nJá possui um usuário cadastrado?\n[S]Sim\n[N]Não\n[Q]Sair\n\n')
            if verificacao == 'N' or verificacao == 'n':
                confirmacao = input('\nGostaria de criar um usuário?\n[S]Sim\n[N]Não\n\n')
                if confirmacao == 'S' or confirmacao == 's':
                    criar_usuario(usuarios)
                elif confirmacao == 'N' or confirmacao == 'n':
                    print('\nObrigado por utilizar nossos serviços!\n')
                    break
                else: print('\n### Opção Inválida! ###\nRetornando ao menu de login...')
            elif verificacao == 'S' or verificacao == 's':
                login_cpf = input('\nDigite o seu CPF: ')
                repetido, usuario = usuario_repetido(login_cpf, usuarios)
                if repetido:
                    print(f'\nOlá, {usuario["nome"]}')
                    controle_app = 2
                else:
                    print('\n### Não foi possível localizar o usuário! ###')
            elif verificacao == 'Q' or verificacao == 'q':
                print('\nObrigado por utilizar nossos serviços!\n')
                break
            else:
                print('\n### Opção Inválida! Por favor, selecione novamente a operação desejada ###')
                continue

        # Criar Conta
        elif controle_app == 2 and usuario_possui_conta(login_cpf, usuarios) == False:
                verificacao = input('\nNão identificamos uma conta vinculada ao usuario! \nGostaria de criar um conta para realizar operações?[S/N]\n')
                if verificacao == 'S' or verificacao == 's':
                    criar_conta(AGENCIA, contas, login_cpf, num_conta, usuarios)
                    print('\n=== Conta criada com sucesso! ===')
                    num_conta += 1
                elif verificacao == 'N' or verificacao == 'n':
                    controle_app = 1

        # Menu de Operações
        elif controle_app == 2 and usuario_possui_conta(login_cpf, usuarios) == True:
            conta = selecionar_conta(login_cpf, contas)
            while True:
                operacao = menu()
                # Trocar Conta
                if operacao == 'T' or operacao == 't':
                    break
                # Criar Conta
                elif operacao == 'C' or operacao == 'c':
                    criar_conta(AGENCIA, contas, login_cpf, num_conta, usuarios)
                    print('\n=== Conta criada com sucesso! ===')
                    num_conta += 1
                # Depósito
                elif operacao == 'D' or operacao == 'd':
                    deposito(conta, operacao)
                # Saque
                elif operacao == 'S' or operacao == 's':
                    saque(conta=conta, operacao=operacao, limite_saque=LIMITE_SAQUE)
                # Extrato
                elif operacao == 'E' or operacao == 'e':
                    extrato(conta)
                # Sair
                elif operacao == 'Q' or operacao == 'q':
                    print('\nRetornando ao menu inicial...\n')
                    controle_app = 1
                    break
                # Menu
                elif operacao == 'R':
                    continue
                # Erro
                else: print('\n### Opção Inválida! Por favor, selecione novamente a operação desejada ###')
        else: print('\n### Opção Inválida! Por favor, selecione novamente a operação desejada ###')

main()