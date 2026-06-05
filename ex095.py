# Script criado por Filipe Cavinato

jogadores = []

while True:
    jogador = dict()
    gols = []
    soma_gols = 0
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
        soma_gols += gols[i]
    jogador['gols'] = gols
    jogador['total de gols'] = soma_gols
    jogadores.append(jogador)
    del jogador

    while True:
        op = str(input('Deseja Continuar ? [S/N] '))[0].strip().upper()
        if op in 'SN':
            break
        print('Opção Invalida! Digite apenas [S/N].')
    if op == 'N':
        break
print('-=-'*25)
print(jogadores)
print('-=-'*25)

print(f'{"Cod":<4} {"Nome":<15} {"Gols":<20} {"Total"}')
for i in range(0, len(jogadores)):
    print(f'{i:>4} {(jogadores[i]["nome"]):<15} {str(jogadores[i]["gols"]):<20} {(jogadores[i]["total de gols"])}')
    jogadores[i]["cod"] = i
print('-'*40)
while True:
    while True:
        op2 = int(input('Mostrar dados de qual jogador ? [999 para SAIR] '))
        if op2 < len(jogadores) or op2 == 999:
            break
        print(f'ERRO não existe jogador com código {op2}. Tente novamente.')
    if op2 == 999:
        break
    print(f'=> Levantamento do Jogador {jogadores[op2]["nome"]}: ')
    for i in range(0, len(jogadores[op2]["gols"])):
        print(f'No jogo {i + 1} fez {jogadores[op2]["gols"][i]} gols')
    print('-'*40)

print('------ Fim do Programa ------')
