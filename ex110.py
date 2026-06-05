# Script criado por Filipe Cavinato

from uteis.utilidadescev import moeda

val = float(input('Digite o preço: R$ '))
a = float(input('Qual a Porcentagem do aumento: '))
d = float(input('Qual a Porcentagem da diminuição: '))
moeda.resumo(val, a, d, formatar=True)

print('------ Fim do Programa ------')
