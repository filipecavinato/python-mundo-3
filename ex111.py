# Script criado por Filipe Cavinato

from uteis.utilidadescev import moeda

val = float(input('Digite o preço: R$ '))
a = int(input('Qual a Porcentagem do aumento: '))
d = int(input('Qual a Porcentagem da diminuição: '))
moeda.resumo(val, a, d, formatar=True)

print('------ Fim do Programa ------')
