# Desafio de Projeto: Criando um Sistema Bancário
Esse desafio foi proposto pela DIO em seu Bootcamp sobre Ciência de Dados.

## 1ª Versão
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato. 
Nessa versão, só existirá 1 cliente.

### Detalhes
#### Depósito
- Valores sempre positivos;
- Armazenados em uma variável;
- Exibidos no extrato.

#### Saque
- Permitir até 3 saques diários;
- Limite de R$500 por saque;
- Exibir mensagem na falta saldo;
- Armazenados em uma variável;
- Exibidos no extrato.

#### Extrato
- Listar todos os depósitos e saques;
- Exibir saldo atual no final.
- Formato: "R$xxx.xx".

## 2ª Versão
Para a segunda versão do sistema, devemos exercitar o uso de funções. Então tenho que transformar as operações de saque, depósito e extrato em funções. Também devo criar 2 novas funções: criar usuário (cliente) e criar conta corrente (vinculada ao cliente).

### Detalhes
Todas as operações devem ser funções e cada função vai ter uma regra na passagem de argumentos.

#### Saque
- Deve receber os argumentos apenas por nome (keyword only)

Sugestão de Argumentos: saldo, valor, extrato, limite, num_saques, limite_saques.<br>
Sugestão de Retorno: saldo e extrato.

#### Depósito
- Deve receber os argumentos apenas por posição (positional only)

Sugestão de Argumentos: saldo, valor, extrato. <br>
Sugestão de Retorno: saldo e extrato. 

#### Extrato
- Deve receber argumentos por posição e por nome  (positional and keyword)

Sugestão de Agumentos Posicionais: saldo. <br>
Sugestão de Argumentos Nomeados: extrato.

#### Criar Usuário (Cliente)
- Os usuários devem ser armazenados em uma lista;
- Um usuário é composto por: nome, data de nascimento, CPF e endereço;
- Devem ser armazenados somente os números do CPF; 
- Não deve permitir o cadastro de 2 usuários com o mesmo CPF.

Sugestão de Formatação do Endereço: logradouro, nº - bairro - cidade/sigla estado

#### Criar Conta Corrente
- Deve armazenar as contas em uma lista;
- Uma conta é composta por: agência, número da conta e usuário.
- O numero da conta deve ser sequencial, iniciando em 1.
- O número da agência é fixo: "0001".
- O usuário pode ter mais de uma conta, mas uma conta pertence somente um usuário.