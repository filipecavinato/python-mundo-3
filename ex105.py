# Script criado por Filipe Cavinato

def notas(*valor, sit=False):
    """
    -> Função para analisar as notas e situações de varios alunos.
    :param valor: uma ou mais notas dos alunos (vários valores aceitos).
    :param sit: (Opcional) Indica se será mostrada a Situação perante a média.
    :return: Dicionario contendo todas as informações sobre as notas.
    Criado por: Filipe Cavinato
    """
    dic = dict()
    maior = menor = soma = count = 0
    for n in valor:
        if maior == menor == 0:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        soma += n
        count += 1
    media = soma/count
    dic['Quantidade de Notas'] = count
    dic['A Maior Nota'] = maior
    dic['A Menor Nota'] = menor
    dic['Média da Turma'] = media
    if sit:
        if media >= 7:
            dic['Situação'] = 'Boa'
        elif 5 <= media < 7:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'
    return dic

help(notas)
resp = notas(5.5, 2.5, 1.5, 7.5, 9.5, 10, 9.5, 10, sit=True)
for k, v in resp.items():
    print(f'{k}: {v}')

print('------ Fim do Programa ------')
