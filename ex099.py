# Script criado por Filipe Cavinato
from time import sleep

def maior(*num):
    m = 0
    print('-=-'*20)
    print('Analisando os valores passados...')
    for i in num:
        print(i, end=' ')
        sleep(0.5)
        if i > m:
            m = i
    print()
    print(f'Foram informados {len(num)} valores')
    print(f'O Maior número é o {m}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print('------ Fim do Programa ------')
