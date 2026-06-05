# Script criado por Filipe Cavinato

turma = []
aluno = []
qt = 0
while True:
    print('-'*15)
    print(f'{"Aluno "f'{qt + 1}'"":^15}')
    print('-'*15)
    nome = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Digite a 1ª Nota: '))
    n2 = float(input('Digite a 2ª Nota: '))
    aluno.append(qt)
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    turma.append(aluno[:])
    aluno.clear()
    qt += 1
    while True:
        op = str(input('Deseja adicionar outro aluno ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print('Opção Invalida, digite apenas [S/N]')
    if op == 'N':
        break

print('-'*25)
print(f'{"Nº":<3}{"Nome":<12}{"Média"}')
print('-'*25)
for i in range(0, len(turma)):
    media = (turma[i][2] + turma[i][3])/2
    print(f'{turma[i][0]:<3}{turma[i][1]:<12}{media:^6.1f}')
print('-'*25)
while True:
    while True:
        op2 = int(input('Quer ver a nota de qual aluno ? [999 para SAIR] '))
        if op2 < len(turma):
            if op2 in turma[op2]:
                print(f'As notas de {turma[op2][1]} são {turma[op2][2:]}')
                print('-'*40)
                break
        if op2 == 999:
            break
        print('Valor Invalido! Digite apenas o Nº do Aluno ou [999 para SAIR]!! ')
        print('-'*40)
    if op2 == 999:
        break

print('------ Fim do Programa ------')
