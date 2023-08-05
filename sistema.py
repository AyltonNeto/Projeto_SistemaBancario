# Função para acessar o menu
def menu():
    print('''\nQual operação deseja realizar?
[1]Ver Extrato
[2]Depositar
[3]Sacar
[4]Sair
''')
    return input()

# Função para confirmar se a entrada é numérica
def numerico(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True

print('\nBem vindo ao Banco Ipim LTDA!')
operacao, saque, saldo, cont_saq, cont_dep, limite = 0, 0, 0.0, 0, 0, 500.0
registros = {}

while operacao != '4':
    operacao = menu()

# Operação de Depósito  
    if operacao == '2':    
        while operacao == '2':
            valor = input('\nQual valor deseja depositar?(Para retornar ao menu digite[R])\n')
            if numerico(valor) and float(valor) > 0:
                saldo += float(valor)
                print('\nOperação realizada com sucesso!')
                cont_dep += 1
                registros[f'{cont_dep}º Depósito'] = f'{valor}'
                print('\nRetornando ao menu de operações...')
                operacao = 0

            elif valor == 'R' or valor == 'r':
                operacao = 0

            else: print('\nDefina um valor possível!')

# Operação de Saque
    elif operacao == '3':
        while operacao == '3':
            valor = input('\nQual valor deseja sacar?(Para retornar ao menu digite[R])\n')
            if cont_saq == 3:
                print('\nLimite de 3 saques diários atingido!')
                operacao = 0
            
            elif valor == 'R' or valor == 'r':
                operacao = 0
            
            elif numerico(valor) and float(valor) > saldo:
                print(f'\nValor maior que saldo disponível!\nSaldo = R${saldo}0')

            elif numerico(valor) and float(valor) <= limite and float(valor) > 0:
                saldo -= float(valor)
                print('\nOperação realizada com sucesso!')
                cont_saq += 1
                registros[f'{cont_saq}º Saque'] = f'{valor}'
                print('\nRetornando ao menu de operações...')
                operacao = 0
                
            elif numerico(valor) and float(valor) > limite:
                print(f'\nValor superior ao seu limite de saque\nLimite de Saque = R${limite}0')
            
            else:
                print('\nDefina um valor possível!')

# Operação de Ver Extrato
    elif operacao == '1':
        print('\nExtrato:\n+-----------------------------+')
        cont_reg = 0
        for registro, quantia in registros.items():
            cont_reg += 1
            quantia = f'{float(quantia):,.2f}'
            if "Depósito" in registro:
                print(f'|{str(cont_reg).zfill(3)} Depósito   +R$ {quantia.ljust(10)}|')
            
            else: 
                print(f'|{str(cont_reg).zfill(3)} Saque      -R$ {quantia.ljust(10)}|')
        print(f'+-----------------------------+\nSaldo = R$ {float(saldo):.2f}')

# Sair
    elif operacao == '4':
        print('\nObrigado por utilizar nossos serviços!\n')

# Menu
    elif operacao == '0':
        continue

# Erro
    else: print('\nOpção Inválida!')