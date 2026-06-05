# Script criado por Filipe Cavinato
from random import randint
from time import sleep

def sorteia():
    l = list()
    print('Valores Sorteados: ', end='')
    for i in range(0, 5):
        l.append(randint(1,10))
        print(f'{l[i]}', end=' ')
        sleep(0.5)
    print()
    return l

def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

num = sorteia()
print(f'Somando os valores Pares de {num} temos {soma_par(num)}')

print('------ Fim do Programa ------')
