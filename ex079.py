# Script criado por Filipe Cavinato

num = []

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado, não pode ser adicionado novamente!!')
    while True:
        op = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print('Opção Invalida!! Digite apenas [S/N]')
    if op == 'N':
        break
num.sort()
print(f'Você digitou os valores {num}')
print('------ Fim do Programa ------')
