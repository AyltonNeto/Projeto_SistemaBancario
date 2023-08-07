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

while True:
    operacao = input(
'''\nQual operação deseja realizar?
[E]Extrato
[D]Depositar
[S]Sacar
[Q]Sair
\n''')
    
# Operação de Depósito  
    if operacao == 'D' or operacao =='d':    
        while operacao == 'D' or operacao == 'd':
            valor = input('\nQual valor deseja depositar? Para retornar ao menu digite[R]\n')
            if numerico(valor) and float(valor) > 0:
                saldo += float(valor)
                print('\nOperação realizada com sucesso!')
                cont_dep += 1
                registros[f'{cont_dep}º Depósito'] = f'{valor}'
                print('\nRetornando ao menu de operações...')
                operacao = 'R'

            elif valor == 'R' or valor == 'r':
                operacao = 'R'

            else: print('\nDefina um valor possível!')

# Operação de Saque
    elif operacao == 'S' or operacao == 's':
        while operacao == 'S' or operacao == 's':
            valor = input('\nQual valor deseja sacar? Para retornar ao menu digite[R]\n')
            if cont_saq == 3:
                print('\nLimite de 3 saques diários atingido!')
                operacao = 'R'
            
            elif valor == 'R' or valor == 'r':
                operacao = 'R'
            
            elif numerico(valor) and float(valor) > saldo:
                print(f'\nValor maior que saldo disponível!\nSaldo = R${saldo}0')

            elif numerico(valor) and float(valor) <= limite and float(valor) > 0:
                saldo -= float(valor)
                print('\nOperação realizada com sucesso!')
                cont_saq += 1
                registros[f'{cont_saq}º Saque'] = f'{valor}'
                print('\nRetornando ao menu de operações...')
                operacao = 'R'
                
            elif numerico(valor) and float(valor) > limite:
                print(f'\nValor superior ao seu limite de saque\nLimite de Saque = R${limite}0')
            
            else:
                print('\nOperação Falhou! Informe um valor válido!')

# Operação de Ver Extrato
    elif operacao == 'E' or operacao == 'e':
        print('\n+========== EXTRATO ============+')
        if not registros:
            print('|Não foram realizadas operações!|')
        else:
            cont_reg = 0
            for registro, quantia in registros.items():
                cont_reg += 1
                quantia = f'{float(quantia):.2f}'
                if "Depósito" in registro:
                    print(f'| {str(cont_reg).zfill(3)} Depósito   +R$ {quantia.ljust(11)}|')
                
                else: 
                    print(f'| {str(cont_reg).zfill(3)} Saque      -R$ {quantia.ljust(11)}|')
        print(f'+===============================+\nSaldo = R$ {float(saldo):.2f}')

# Sair
    elif operacao == 'Q' or operacao == 'q':
        print('\nObrigado por utilizar nossos serviços!\n')
        break

# Menu
    elif operacao == 'R':
        continue

# Erro
    else: print('\nOpção Inválida! Por favor, selecione novamente a operação desejada.')