# Script criado por Filipe Cavinato

from datetime import date

funcionario = dict()
aposenta = 0
ano_atual = date.today().year
funcionario['nome'] = str(input('Nome Completo: ')).strip().title()
funcionario['idade'] = ano_atual - int(input('Ano de Nascimento: '))
funcionario['ctps'] = int(input('Carteira de Trabalho [0 se não tiver]: '))

if funcionario['ctps'] != 0:
    funcionario['contratação'] = int(input('Digite o ano de contratação: '))
    funcionario['salario'] = float(input('Digite seu sálario: R$ '))
    aposenta = 35 - (ano_atual - funcionario['contratação'])
else:
    funcionario['ctps'] = 0
print('-=-'*15)
for k, v in funcionario.items():
    print(f'=> {k.capitalize()}:{" R$" if k == "salario" else ""} {v}')
if funcionario['ctps'] != 0:
    print(f'Irá se aposentar aos {(aposenta + funcionario['idade'])} anos')

print('------ Fim do Programa ------')
