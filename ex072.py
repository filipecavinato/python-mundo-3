# Script criado por Filipe Cavinato

num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
               'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
               'Dezenove', 'Vinte')
n = 0
op = 'S'

while op == 'S':
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Valor Invalido! Digite um número entre 0 e 20!')
    print(f'Você digitou o número {num_extenso[n]}')

    while True:
        op = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if op in 'SN':
            break
        print('Dados Inválidos! Digite apenas [S/N]')
print('------ Fim do Programa ------')
