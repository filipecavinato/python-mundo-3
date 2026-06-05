# Script criado por Filipe Cavinato
lista = []
x = str(input('Digite a expressão: '))
for i in x:
    lista.append(i)
a = lista.count('(')
b = lista.count(')')
if a == b:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')

print('------ Fim do Programa ------')
