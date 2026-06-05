# Script criado por Filipe Cavinato
lista = [[],[]]

for i in range(0,7):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('-=-'*10)
print(f'Valores Pares: {lista[0]}')
print(f'Valores Ímpares: {lista[1]}')

print('------ Fim do Programa ------')
