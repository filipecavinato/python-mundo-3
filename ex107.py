# Script criado por Filipe Cavinato

from uteis.utilidadescev import moeda

val = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {val:.2f} é R$ {moeda.metade(val):.2f}')
print(f'O dobro de R$ {val:.2f} é R$ {moeda.dobro(val):.2f}')
print(f'Aumentando 10% de R$ {val:.2f}, temos R$ {moeda.aumentar(val, 10):.2f}')
print(f'Diminuindo 13% de R$ {val:.2f}, temos R$ {moeda.diminuir(val, 13):.2f}')

print('------ Fim do Programa ------')
