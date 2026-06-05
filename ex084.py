# Script criado por Filipe Cavinato

geral = []
pessoa = []
maior = menor = 0
while True:
    nome = str(input('Digite o nome: ')).strip().capitalize()
    peso = float(input('Digite o peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    geral.append(pessoa[:])
    pessoa.clear()
    while True:
        op = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print("Opção Invalida! Digite apenas [S/N]")
    if op == 'N':
        break

print(f'Total de {len(geral)} pessoas cadastradas')
for n in geral:
    if maior == menor == 0:
        maior = menor = n[1]
    if n[1] > maior:
        maior = n[1]
    elif n[1] < menor:
        menor = n[1]

print(f'O maior peso foi de {maior:.1f} KG. Peso de ', end='')
for n in geral:
    if n[1] >= maior:
        print(f'[{n[0]}]', end=' ')

print(f'\nO menor peso foi de {menor:.1f} Kg. Peso de ', end='')
for n in geral:
    if n[1] <=  menor:
        print(f'[{n[0]}]', end=' ')

print('\n------ Fim do Programa ------')
