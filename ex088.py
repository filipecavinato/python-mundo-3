# Script criado por Filipe Cavinato

from random import randint
from time import sleep
jogos = []
palpite = []

print('-=-'* 11)
print(f'{"Gerador de Palpites Mega Sena":^33}')
print('-=-'*11)
qt = int(input('Quantos jogos você quer gerar: '))

for i in range(0, qt):
    for j in range(0,6):
        while True:
            if len(palpite) == 6:
                break
            n = randint(1,61)
            if n not in palpite:
                palpite.append(n)
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()

print('-=-'*17)
print('Sorteando Jogos....: ')
for i in range(0, qt):
    sleep(1)
    print(f'Jogo {i+1} = {jogos[i]}')
sleep(1)
print(f'{"-=-"*3}{"Boa Sorte!":^13}{"-=-"*3}\n')
print('------ Fim do Programa ------')
