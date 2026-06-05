# Script criado por Filipe Cavinato

lista = []
count = 0
while True:
    pessoa = dict()
    count += 1
    print('-'*20)
    print(f'{f"Pessoa {count}":^20}')
    print('-'*20)
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: '))[0].strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Sexo Invalido!! Digite apenas [M/F].')
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa)
    del pessoa
    while True:
        op = str(input('Deseja continuar ? [S/N] '))[0].strip().upper()
        if op in 'SN':
            break
        print('Opção Invalid!! Digite apenas [S/N].')
    if op == 'N':
        break
print('-=-'*35)
print(lista)
print('-=-'*35)

print(f'=> Total de {len(lista)} pessoas cadastradas.')
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]['idade']
print(f'=> A média de idade do grupo é de {soma/len(lista)} anos')
print(f'=> Lista de Mulheres: ', end='')
for i in range(0, len(lista)):
    if lista[i]['sexo'] == 'F':
        print(f'{lista[i]["nome"]} ', end='... ')
print()
print(f'=> Lista de Pessoas acima da idade média:')
for i in range(0, len(lista)):
    if lista[i]['idade'] > soma/len(lista):
        print(f' - Nome: {lista[i]["nome"]}; Sexo: {lista[i]["sexo"]} ; Idade: {lista[i]["idade"]} ')
print('------ Fim do Programa ------')
