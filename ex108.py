# Script criado por Filipe Cavinato

from uteis.utilidadescev import moeda

val = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}')
print(f'Aumentando 10% de {moeda.moeda(val)}, temos {moeda.moeda(moeda.aumentar(val, 10))}')
print(f'Diminuindo 13% de {moeda.moeda(val)}, temos {moeda.moeda(moeda.diminuir(val, 13))}')

print('------ Fim do Programa ------')
