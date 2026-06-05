# Script criado por Filipe Cavinato

matriz = []
n = []

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
        print(f'[{(matriz[i][j]):^5}]', end=' ')
    print()
print('------ Fim do Programa ------')
