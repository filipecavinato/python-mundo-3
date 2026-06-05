# Script criado por Filipe Cavinato

jogador = dict()
gols = []
soma_gols = 0
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
    soma_gols += gols[i]
jogador['gols'] = gols
jogador['total de gols'] = soma_gols
print('-=-'*25)
print(jogador)
print('-=-'*25)
for k, v in jogador.items():
    if k != 'partidas':
        print(f'{k.title()}: {v}')
print('-=-'*25)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for c, i in enumerate(jogador['gols']):
    print(f'=> Na Partida {c}, fez {i} gols.')
print(f'Foi um total de {jogador['total de gols']} gols.')
print('------ Fim do Programa ------')
