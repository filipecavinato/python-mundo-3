# Script criado por Filipe Cavinato

def menu():
    nome_sistema = 'Sistema de Ajuda PyHelp'
    tam = len(nome_sistema) + 4
    print('\033[33m-\033[m' * tam)
    print(f'\033[33m  {nome_sistema}\033[m')
    print('\033[33m-\033[m' * tam)

def procura(op):
    from time import sleep
    nome_sistema = f'Acessando Manual da função {op}()'
    tam = len(nome_sistema) + 4
    print('\033[34m-\033[m' * tam)
    print(f'\033[34m  {nome_sistema}\033[m')
    print('\033[34m-\033[m' * tam)
    sleep(2)
    help(op)
    sleep(2)
    return 0

while True:
    menu()
    while True:
        op = str(input('Função ou Biblioteca > ')).strip().lower()
        if not op.isnumeric():
            break
        print('\033[31mOpção Invalida! Digite o nome de uma Função ou Biblioteca\033[m')
    if op.upper() == 'FIM':
        break
    procura(op)
print('\033[36mAté Logo!!!\033[m')
print('------ Fim do Programa ------')
