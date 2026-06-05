# Script criado por Filipe Cavinato
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=-'*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count}', end=' ')
            count += passo
            sleep(0.5)
    else:
        count = inicio
        while count >= fim:
            print(f'{count}', end=' ')
            count -= passo
            sleep(0.5)
    print()

contador(1, 10, 1)
contador(10, 0, 2)
print('-=-'*20)
print('Contagem Personalizada: ')
inicio = int(input('Digite o Inicio: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)

print('------ Fim do Programa ------')
