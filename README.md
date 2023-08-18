# Desafio Criando um sistema Bancário com Python - Versão 2

Um grande banco requisitou o desenvolvimento de um novo sistema em linguagem Pyhon. Para a primeira versão do sistema foram implementadas apenas 3 operações: depósito, saque e extrato. 

Para a segunda Versão o banco requisitou o desenvolvimento de novas funções:

## Condições Versão 1

📌 Deve ser possível depositar apenas valores positivos para a conta bancária;

📌 A Primeira versão trabalha com apenas 1 usuário;

📌 Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;
    
📌 O sistema deve permitir realizar 3 saques diários com limitie máximo de R$ 500,00 por saque; 
    
📌 Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo;

📌 Todos os saques devem ser armazenados em uma variável e exbidos na operação de extrato;

 📌 A opção extrato deve listar todos os depósitos e saques realizados na conta, no fim da listagem deve ser exibido o saldo atual da conta;
    
📌 Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

## Condições Versão 2

📌 Deve-se criar Funções para as operações existentes: sacar, depositar e visualizar extrato;

📌 Criar novas funções: Criar Usuário e Criar Conta Corrente vinculada a usuário;

📌 Saque: deve receber argumentos apenas por nome (keyword only);

📌 Depósito: deve receber argumentos apenas por posição (positional only);

📌 Extrato: deve receber argumentos por posição e nome;

📌 Criar Usuário: Deve armazenar os usuários em uma lista. Nãos podemos cadastrar 2 usuários com o mesmo CPF;

📌 Criar conta corrente: Deve armazenar contas em uma lista. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário. 

📌 Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista. 
  
