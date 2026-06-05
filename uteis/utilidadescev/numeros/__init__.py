# Modulo criado por Filipe Cavinato

def fatorial(x):
    """
    -> Calculo de Fatorial de um número qualquer.
    :param x: qualquer número inteiro.
    :return: resultado do fatorial do número.
    Criado por: Filipe Cavinato
    """
    fat = 1
    for i in range(x, 0, -1):
        fat *= i
    return fat

def dobro(x):
    return 2 * x

def triplo(x):
    return 3 * x
