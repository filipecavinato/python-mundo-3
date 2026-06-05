# Script criado por Filipe Cavinato

from datetime import date
def voto(ano=0):
    """
    — > Função que verifica se uma pessoa precisa votar, baseado em sua data de nascimento.
    :param ano: Ano de Nascimento
    :return: Retorna se a pessoa precisa votar ou não
    Criado por: Filipe Cavinato
    """
    global idade
    if 18 <= idade <= 65:
        return 'Voto Obrigatório'
    else:
        return 'Não Vota'


n = int(input("Digite o ano em que você nasceu: "))
idade = date.today().year - n
print(f'Com {idade} anos: {voto(n)}')
print('------ Fim do Programa ------')
