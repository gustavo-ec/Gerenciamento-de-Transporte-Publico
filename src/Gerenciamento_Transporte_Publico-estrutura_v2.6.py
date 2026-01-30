# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet (como por exemplo códigos gerados por IA).
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# IMPLEMENTAR OS VALORES DAS VARIÁVEIS QUE SERÃO USADAS AO DECORRER DO CÓDIGO
saldo_padrao = 0
saldo_est_ido = 0
saldo_social = 0
valor_passagem = 0
recarga_total_padrao = 0
recarga_total_est_ido = 0
recarga_total_social = 0
quantidade_recarga_padrao = 0
quantidade_recarga_est_ido = 0 
quantidade_recarga_social = 0
quantidade_passagem_comprada_padrao = 0
quantidade_passagem_comprada_est_ido = 0
quantidade_passagem_comprada_social = 0
valor_gasto_padrao = 0
valor_gasto_est_ido = 0
valor_gasto_social = 0
total_passagem_padrao = 0
total_passagem_est_ido = 0
total_passagem_social = 0
passagem_usada_padrao = 0
passagem_usada_est_ido = 0
passagem_usada_social = 0

# MENSAGEM DE BOAS-VINDAS PARA ESTABELECER UMA CONEXÃO EMOCIONAL
print('-'*43)
print('BEM-VINDO AO NOSSO SISTEMA DE TRANSPORTE <3')
print('PRESSIONE QUALQUER TECLA PARA CONTINUAR.')
input('-'*43)

# SOLICITAR O VALOR DA PASSAGEM E VERIFICAR SE É UM NÚMERO POSITIVO
while valor_passagem <= 0:
    entrada = input('POR FAVOR, DIGITE O VALOR DA PASSAGEM EM R$: ').strip()
    if entrada.replace('.', '', 1).isdigit(): # VERIFIÇÃO DA QUANTIDADE DE DECIMAIS
        valor_passagem = float(entrada)
        if valor_passagem > 0:
            print(f'VALOR DA PASSAGEM CONFIGURADO PARA R${valor_passagem:.2f}.')
        else:
            print('ERRO! O VALOR DA PASSAGEM NÃO PODE SER NEGATIVO.')
    else:
        print('ERRO! APENAS VALORES NUMÉRICOS.')

# MENU PARA A ESCOLHA DAS OPÇÕES 
menu = True
while menu:
    print('[ 1 ] RECARREGAR SALDO\n'
    '[ 2 ] COMPRAR PASSAGEM\n'
    '[ 3 ] VERIFICAR EMBARQUE\n'
    '[ 4 ] CONSULTAR SALDO\n'
    '[ 5 ] GERAR RELATÓRIO\n'
    '[ 6 ] SAIR')
    escolha = input()
    match escolha:
        case '1': # CASO A OPÇÃO RECARREGAR SALDO(1) FOR ESCOLHIDA
            print('VOCÊ ESCOLHEU RECARREGAR SALDO.')
            recarga = input('VALOR DA RECARGA EM R$: ').strip()
            if recarga.replace('.', '', 1).isdigit() and float(recarga) > 0:
                categoria = input('[ 1 ] PADRÃO\n'
                '[ 2 ] ESTUDANTE/IDOSO\n'
                '[ 3 ] SOCIAL\n'
                '[ 4 ] VOLTAR AO MENU\n'
                'ESCOLHA A OPÇÃO: ')
                recarga = float(recarga)
                if categoria == '1': 
                    saldo_padrao += recarga
                    quantidade_recarga_padrao += 1
                    recarga_total_padrao += recarga
                    print(f'REGARGA DE R${recarga:.2f} CONCLUÍDA. SEU SALDO ATUAL É {saldo_padrao:.2f}')
                elif categoria == '2' and recarga > 0:
                    saldo_est_ido += recarga
                    recarga_total_est_ido += recarga
                    quantidade_recarga_est_ido += 1
                    print(f'REGARGA DE R${recarga:.2f} CONCLUÍDA. SEU SALDO ATUAL É {saldo_est_ido:.2f}')
                elif categoria == '3' and recarga > 0:
                    saldo_social += recarga
                    quantidade_recarga_social += 1
                    recarga_total_social += recarga
                    print(f'REGARGA DE R${recarga:.2f} CONCLUÍDA. SEU SALDO ATUAL É {saldo_social:.2f}')
                elif categoria == '4':
                    print('VOLTANDO AO MENU...')
                else:
                    print('ERRO! OPÇÂO INVÁLIDA.')
            else:
                print('ERRO! OPÇÃO INVÁLIDA.')

        case '2': # CASO A OPÇÃO COMPRAR PASSAGEM(2) FOR ESCOLHIDA
            print('VOCÊ ESCOLHEU COMPRAR PASSAGEM')
            categoria = input('[ 1 ] PADRÃO\n'
            '[ 2 ] ESTUDANTE/IDOSO (50% DE DESCONTO)\n'
            '[ 3 ] SOCIAL (80% DE DESCONTO)\n'
            '[ 4 ] VOLTAR AO MENU\n'
            'ESCOLHA A OPÇÃO: ')
            if categoria == '1':
                if saldo_padrao >= valor_passagem:
                    saldo_padrao -= valor_passagem
                    quantidade_passagem_comprada_padrao += 1
                    valor_gasto_padrao += valor_passagem
                    total_passagem_padrao += 1
                    print(f'PASSAGEM COMPRADA COM SUCESSO. VALOR: R${valor_passagem}')
                else:
                    print(f'SALDO INSUFICIENTE! SEU SALDO ATUAL É R${saldo_padrao}, VOCÊ PRECISA DE R${valor_passagem}')
                    print('FAÇA UMA RECARGA PARA CONTINUAR')
            elif categoria == '2':
                desconto = valor_passagem * 0.5
                if saldo_est_ido >= desconto:
                    saldo_est_ido -= desconto
                    quantidade_passagem_comprada_est_ido += 1
                    valor_gasto_est_ido += desconto
                    total_passagem_est_ido += 1
                    print(f'PASSAGEM COMPRADA COM SUCESSO. VALOR: R${desconto}')
                else:
                    print(f'SALDO INSUFICIENTE! SEU SALDO ATUAL É R${saldo_est_ido}, VOCÊ PRECISA DE R${desconto}')
                    print('FAÇA UMA RECARGA PARA CONTINUAR')

            elif categoria == '3':
                desconto = valor_passagem * 0.2
                if saldo_social >= desconto:
                    saldo_social -= desconto
                    quantidade_passagem_comprada_social += 1
                    valor_gasto_social += desconto
                    total_passagem_social += 1
                    print(f'PASSAGEM COMPRADA COM SUCESSO. VALOR: R${desconto}')
                else:
                    print(F'SALDO INSUFICIENTE! SEU SALDO ATUAL É R${saldo_social}, VOCÊ PRECISA DE R${desconto}')
                    print('FAÇA UMA RECARGA PARA CONTINUAR')
            elif categoria == '4':
                print('VOLTANDO AO MENU...')
            else:
                print('ERRO! OPÇÃO INVÁLIDA')

        case '3': # CASO A OPÇÃO VERIFICAR EMBARQUE(3) FOR ESCOLHIDA
            print('VOCÊ ESCOLHEU VERIFICAR EMBARQUE.')
            categoria = input('[ 1 ] PADRÃO\n'
            '[ 2 ] ESTUDANTE/IDOSO (50% DE DESCONTO)\n'
            '[ 3 ] SOCIAL (80% DE DESCONTO)\n'
            '[ 4 ] VOLTAR AO MENU\n'
            'ESCOLHA A OPÇÃO: ')
            if categoria == '1':
                if total_passagem_padrao > 0:
                    passagem_usada_padrao = passagem_usada_padrao + 1
                    total_passagem_padrao = total_passagem_padrao - 1
                    print('EMBARQUE REALIZADO COM SUCESSO.')
                else:
                    print('VOCÊ NÃO TEM PASSAGEM PARA EMBARQUE. COMPRE NO MENU PRINCIPAL')    
            elif categoria == '2':
                if total_passagem_est_ido > 0:
                    passagem_usada_est_ido = passagem_usada_est_ido + 1
                    total_passagem_est_ido = total_passagem_est_ido - 1
                    print('EMBARQUE REALIZADO COM SUCESSO.')
                else:
                    print('VOCÊ NÃO TEM PASSAGEM PARA EMBARQUE. COMPRE NO MENU PRINCIPAL')    
            elif categoria == '3':
                if total_passagem_social > 0:
                    passagem_usada_social = passagem_usada_social + 1
                    total_passagem_social = total_passagem_social - 1
                    print('EMBARQUE REALIZADO COM SUCESSO')
                else:
                    print('VOCÊ NÃO TEM PASSAGEM PARA EMBARQUE. COMPRE NO MENU PRINCIPAL')
            elif categoria == '4':
                print('VOLTANDO AO MENU...')
            else:
                print('ERRO! OPÇÃO INVÁLIDA')

        case '4': # CASO A OPÇÃO CONSULTAR SALDO(4) FOR ESCOLHIDA
            print('VOCÊ ESCOLHEU CONSULTAR SALDO.')
            categoria = input('[ 1 ] PADRÃO\n'
            '[ 2 ] ESTUDANTE/IDOSO\n'
            '[ 3 ] SOCIAL\n'
            '[ 4 ] VOLTAR AO MENU\n'
            'ESCOLHA A OPÇÃO: ')
            if categoria == '1':
                print(f'SEU SALDO ATUAL É DE R${saldo_padrao}')
            elif categoria == '2':
                print(f'SEU SALDO ATUAL É DE R${saldo_est_ido}')
            elif categoria == '3':
                print(f'SEU SALDO ATUAL É DE R${saldo_social}')
            elif categoria == '4':
                print('VOLTANDO AO MENU...')
            else:
                print('ERRO! OPÇÃO INVÁLIDA!')
        

        case '5': # CASO A OPÇÃO GERAR RELATÓRIO(5) FOR ESCOLHIDA
            print('-'*26,'GERANDO RELATÓRIO...','-'*25)
            print(f'RECARGA TOTAL: PADRÃO = {recarga_total_padrao}, ESTUDANTE/IDOSO = {recarga_total_est_ido} e SOCIAL = {recarga_total_social}\n'
                  f'QUANTIDADE DE RECARGAS: PADRÃO = {quantidade_recarga_padrao}, ESTUDANTE/IDOSO = {quantidade_recarga_est_ido} E SOCIAL = {quantidade_recarga_social}\n'
                  f'PASSAGENS USADAS: PADRÃO = {passagem_usada_padrao}, ESTUDANTE/IDOSO = {passagem_usada_est_ido} E SOCIAL = {passagem_usada_social}\n'
                  f'VALOR GASTO: PADRÃO = {valor_gasto_padrao}, ESTUDANTE/IDOSO = {valor_gasto_est_ido} E SOCIAL = {valor_gasto_social}\n'
                  f'SALDO RESTANTE: PADRÃO = {saldo_padrao}, ESTUDANTE/IDOSO = {saldo_est_ido} E SOCIAL = {saldo_social}')
            print('-'*73)
        

        case '6': # CASO A OPÇÃO SAIR(6) FOR ESCOLHIDA
            print('SAINDO DO SISTEMA...')
            menu = False

        case _: # CASO O USUÁRIO INFORME UMA OPÇÃO INVÁLIDA
            print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
