# Script criado por Filipe Cavinato

lista = []

for i in range(0,5):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if len(lista) == 0:
        lista.append(n)
        print('Valor adicionado ao final da lista!')
    elif n <= lista[i - 1]:
        for i in range(0,5):
            if i >= 1:
                if n <= lista[i - 1]:
                    lista.insert(i - 1, n)
                    print(f'Valor adicionado na posição {i - 1} da lista!')
                    break
    elif n > lista[i - 1]:
        lista.append(n)
        print('Valor adicionado ao final da lista!')
print('-=-' * 12)
print('Lista Ordenada: ', end='')
print(lista)
print('------ Fim do Programa ------')
