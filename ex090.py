# Script criado por Filipe Cavinato

aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] > 7.0:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=-'*15)

for k, v in aluno.items():
    print(f'-> {k.capitalize()}: {v}')
print('------ Fim do Programa ------')
