# Script criado por Filipe Cavinato

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-PR', 'Bragantino', 'Coritiba', 'São Paulo',
         'Bahia', 'Cruzeiro', 'Botafogo', 'Vitória', 'Atlético-MG', 'Internacional', 'Grêmio',
         'Corinthians', 'Vasco', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

print('Os 5 Primeiros colocados são: ',end='')
print(f'{times[0:5]}')
print('-' * 40)
print('Os 4 últimos colocados: ', end='')
print(f'{times[-4:]}')
print('-' * 40)
print('Times por ordem alfabética: ', end='')
print(sorted(times))
print('-' * 40)
print(f'A Chapecoense está no {times.index('Chapecoense') + 1}º lugar')
print('\n------ Fim do Programa ------')
