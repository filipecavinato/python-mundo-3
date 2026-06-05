# Script criado por Filipe Cavinato

matriz = []
n = []
soma_par = soma_col = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        val = int(input(f'Digite o valor para a posição [{i}, {j}]: '))
        n.append(val)
    matriz.append(n[:])
    n.clear()
print('-=-'*15)
print('Matriz:')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print('\n')

print('-=-'*15)
print('Analises:')
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
        if j == 2:
            soma_col += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

print(f'A soma de todos os valores Pares é {soma_par}')
print(f'A soma dos valores da 3ª Coluna é {soma_col}')
print(f'O maior valor da 2ª Linha é {maior}')
print('------ Fim do Programa ------')
