# Modulo criado por Filipe Cavinato

def aumentar(x, p, formatar=False):
    res = x + (x * p/100)
    if formatar:
        return moeda(res)
    else:
        return res

def diminuir(x, p, formatar=False):
    res = x - (x * p/100)
    if formatar:
        return moeda(res)
    else:
        return res

def dobro(x, formatar = False):
    res = 2 * x
    if formatar:
        return moeda(res)
    else:
        return res

def metade(x, formatar=False):
    res = x / 2
    if formatar:
        return moeda(res)
    else:
        return res

def moeda(x=0, simbolo='R$'):
    return f'{simbolo} {x:.2f}'.replace('.',',')

def resumo(x=0, aumenta=10, diminui=5, formatar=False):
    if formatar:
        f = True
    else:
        f = False
    titulo = 'Resumo do Valor'
    tam = 1 + 19 + (len(titulo))
    print('-' * tam)
    print(f'          {titulo}')
    print('-' * tam)
    print(f'{"Valor analisado:":<25}{moeda(x)}')
    print(f'{"O dobro do preço:":<25}{dobro(x, formatar=f)}')
    print(f'{"A metade do preço:":<25}{metade(x, formatar=f)}')
    print(f'{f"{aumenta}% de Aumento:":<25}{aumentar(x, aumenta, formatar=f)}')
    print(f'{f"{diminui}% de Redução:":<25}{diminuir(x, diminui, formatar=f)}')
    print('-'*tam)
