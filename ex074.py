# Script criado por Filipe Cavinato

from random import randint

tupla = (randint(1,10), randint(1,10), randint(1,10),
         randint(1,10), randint(1,10))

print('Os valores sorteados foram: ', end='')
for num in tupla:
    print(num, end =' ')
    if tupla.index(num) == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'\nO Maior valor sorteado foi o {maior}')
print(f'O Menor valor sorteado foi o {menor}')
print('------ Fim do Programa ------')
