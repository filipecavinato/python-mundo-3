# Script criado por Filipe Cavinato

def area(lar:float, comp:float):
    print(f'A Area de um Terreno de {lar} x {comp} é: {lar * comp} m²')

print(f'{"Controle de Terrenos: ":^25}')
print('-'*25)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l,c)
print('------ Fim do Programa ------')
