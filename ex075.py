# Script criado por Filipe Cavinato

tupla = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
         int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')))
print(f'Números digitados: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu primeiro na {tupla.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição desta Tupla!')

print('Os número pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

print('\n------ Fim do Programa ------')
