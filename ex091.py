# Script criado por Filipe Cavinato

from random import randint
from time import sleep
from operator import itemgetter

maior = 0
ranking = dict()
for i in range(0,4):
    ranking[f'jogador_{i + 1}'] = randint(1,6)
    if i == 0:
        maior = ranking[f'jogador_{i + 1}']
    elif ranking[f'jogador_{i + 1}'] > maior:
        maior = ranking[f'jogador_{i + 1}']

print('-=-'*15)
print('Valores Sorteados: ')
for k, v in ranking.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('-=-'*15)
print('Ranking dos Jogadores:')
ordenado = sorted(ranking.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ordenado):
    print(f'{k + 1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
print('------ Fim do Programa ------')
