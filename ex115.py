# Script criado por Filipe Cavinato
from uteis.utilidadescev import interface, dado
from time import sleep

while True:
    op = interface.menu(['Ver Pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if op == 0:
        break
    if op == 1:
        dados = dado.mostrar_dados("banco-de-dados.json")
        for p in dados:
            print(f'{p['nome']:<30}{p['idade']:<3}anos')
        print('-' * 37)
    if op == 2:
        pessoa = dado.cadastrar_pessoa("banco-de-dados.json")
        print('\033[36mCadastrando\033[m', end='')
        for i in range(0,3):
            print('\033[36m.\033[m', end='')
            sleep(1)
        print('\n\033[36mPessoa cadastrada com sucesso!!\033[m')
        sleep(1)
    if op == 3:
        print('\033[35mEncerrando Programa\033[m', end='')
        for i in range(0,3):
            print('\033[35m.\033[m', end='')
            sleep(1)
        print('\033[35m\nObrigado, volte sempre!\033[m')
        break
    sleep(1)
