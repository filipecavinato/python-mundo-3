# Script criado por Filipe Cavinato
lista = []
lista_par = []
lista_impar = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    print('Valor Adicionado com Sucesso!!')
    while True:
        op = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print('Opção Invalida! Digite apenas [S/N]')
    if op == 'N':
        break

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'Lista Completa: {lista}')
print(f'Lista com valores Pares: {lista_par}')
print(f'Lista com valores Ímpares: {lista_impar}')
print('------ Fim do Programa ------')
