# Script criado por Filipe Cavinato

def fatorial(n=1,show=False):
    """
    — > Função que calcula Fatorial de um valor.
    :param n: O número a ser calculado.
    :param show: (opcional) Indica se será mostrado o cálculo detalhado.
    :return: O valor do Fatorial no número n.
    Criado por: Filipe Cavinato
    """
    fat = 1
    print(f'{n}! =', end=' ')
    for i in range(n, 0, -1):
        fat *= i
        if show:
            if i > 1:
                print(f'{i}', end=' x ')
            else:
                print(f'{i} = {fat}')
    if not show:
        print(f'{fat}')
    return fat


help(fatorial)
val = int(input('Digite um número para ver o Fatorial: '))
fatorial(val, show=True)
print('\n------ Fim do Programa ------')
