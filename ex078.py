# Script criado por Filipe Cavinato

num = []
maior = menor = 0
for i in range(0,5):
    n = int(input(f'Digite o {i + 1}º número: '))
    num.append(n)

    if i == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f'Lista: {num}')
print(f'O maior valor digitado foi o {maior} e está nas posições ',end='')
for i in range(0, 5):
    if num[i] == maior:
        print(f'{i}', end='.. ')
print(f'\nO menor valor digitado foi o {menor} e está nas posições ', end='')
for i in range(0, 5):
    if num[i] == menor:
        print(f'{i}', end='.. ')

print('\n------ Fim do Programa ------')
