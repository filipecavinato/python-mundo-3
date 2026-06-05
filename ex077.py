# Script criado por Filipe Cavinato

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for n in palavras:
    print(f'\nNa palavra {n.upper()} temos as vogais: ', end='')
    for i in range(0, len(n)):
        if n[i].lower() in 'aeiou':
            print(n[i], end=' ')

print('\n------ Fim do Programa ------')
