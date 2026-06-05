# Script criado por Filipe Cavinato

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    while True:
        op = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print('Opção Incorreta! Digite apenas [S/N]')
    if op == 'N':
        break

print(f'\nForam digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Lista Decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista na posição {lista.index(5)}')
else:
    print('O valor 5 não foi digitado!')
print('------ Fim do Programa ------')
