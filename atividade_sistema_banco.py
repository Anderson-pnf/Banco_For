minha_conta = '2505'
minha_senha = '2001'
saldo = 2500
extrato = []

for chances in range(1,4):
    conta = input('Digite sua conta: ')
    senha = input('Digite sua senha: ')
    if conta == minha_conta and senha == minha_senha:
        menu = input('''Acesso liberado!
                     
Menu:               
1. Depósito.
2. Saque.
3. Saldo.
4. Extrato.
5. Saída.
O que você deseja?
                     
>> ''')
        if menu == '1':
            deposito = float(input('''Digite o valor do depósito:
>> '''))
            saldo += deposito
            extrato.append(f'Depósito: R${deposito:.2f}')
            print(f'Depósito realizado com sucesso! Seu novo saldo é: R${saldo:.2f}')
            
            volta_menu = input('''Você deseja voltar ao menu principal?
1. Sim.
2. Não.
>> ''')
            if volta_menu == '1':
                menu = input('''
Menu:               
1. Depósito.
2. Saque.
3. Saldo.
4. Extrato.
5. Saída.
O que você deseja?
                     
>> ''')
        if menu == '2':
            saque = float(input('''Digite o valor do saque:
>> '''))
            saldo -= saque
            extrato.append(f'Saque: R${saque:.2f}')
            print(f'Saque realizado com sucesso! Seu novo saldo é: R${saldo:.2f}')
            volta_menu = input('''Você deseja voltar ao menu principal?
1. Sim.
2. Não.
>> ''')
            if volta_menu == '1':
                menu = input('''
Menu:               
1. Depósito.
2. Saque.
3. Saldo.
4. Extrato.
5. Saída.
O que você deseja?
                     
>> ''')
        if menu == '3':
            print(f'Seu saldo disponível é no valor de R${saldo:.2f}.')
            volta_menu = input('''Você deseja voltar ao menu principal?
1. Sim.
2. Não.
>> ''')
            if volta_menu == '1':
                menu = input('''
Menu:               
1. Depósito.
2. Saque.
3. Saldo.
4. Extrato.
5. Saída.
O que você deseja?
                     
>> ''')
        if menu == '4':
            print('Extrato bancário: ')
            if extrato:
                for transacao in extrato:
                    print(transacao)
            else:
                print('Nenhuma transação realizada.')
            volta_menu = input('''Você deseja voltar ao menu principal?
1. Sim.
2. Não.
>> ''')
            if volta_menu == '1':
                menu = input('''
Menu:               
1. Depósito.
2. Saque.
3. Saldo.
4. Extrato.
5. Saída.
O que você deseja?
                     
>> ''')
        if menu == '5':
            print('Obrigada, até logo!')
            break
        else:
            print('Obrigada, até logo!')
            break

    else:
        print(f'Acesso negado. Tente novamente, você utilizou {chances} das suas 3 chances.')
else:
    print('Você excedeu o número de tentativas. Acesso bloqueado.')
n = input("Aperte 'ENTER' para sair") 
