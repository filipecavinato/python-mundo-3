# Script criado por Filipe Cavinato

def ficha(nome, gols):
    if nome == '':
        nome = '< Desconhecido >'
    if gols == '' or gols.isalpha():
        gols = 0
    print(f'O jogador {nome} ', end='')
    print(f'fez {gols} gol(s) no campeonato')
    return 0


n = str(input('Digite o nome do jogador: ')).strip().title()
g = str(input('Digite a quantidade de gols: ')).strip()
ficha(n, g)
print('------ Fim do Programa ------')
