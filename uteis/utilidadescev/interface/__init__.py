# Modulo criado por Filipe Cavinato

def menu(lista):
    from time import sleep
    """
    Menu Interativo com opções numéricas.
    :return: Retorna o número da opção escolhida pelo usuário
    """
    nome = 'Menu Principal'
    tam = len(nome) + 16
    print('-' * tam)
    print(f'        {nome:}')
    print('-' * tam)
    c = 1
    for i in lista:
        print(f'\033[1;33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print('-' * tam)
    while True:
        try:
            op = int(input('Sua Opção: '))
            if op == 1 or op == 2 or op == 3:
                return op
            else:
                print('\033[31m Erro: Digite uma opção válida!\033[m')
        except (ValueError, TypeError):
            print('\033[31m Erro: Digite um número inteiro valida!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[35mPrograma encerrado manualmente\033[m', end='')
            for i in range(0, 3):
                print('\033[35m.\033[m', end='')
                sleep(1)
            print('\033[35m\nObrigado, volte sempre!\033[m')
            return 0
