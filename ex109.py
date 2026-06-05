# Script criado por Filipe Cavinato

from uteis.utilidadescev import moeda

val = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(val)} é {moeda.metade(val, formatar=True)}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.dobro(val, formatar=True)}')
print(f'Aumentando 10% de {moeda.moeda(val)}, temos {moeda.aumentar(val, 10, formatar=True)}')
print(f'Diminuindo 13% de {moeda.moeda(val)}, temos {moeda.diminuir(val, 13, formatar=True)}')

print('------ Fim do Programa ------')
