# Script criado por Filipe Cavinato

def leia_int(valor):
    """
    — > Verifica se o número digitado é um número inteiro.
    :param valor: Número para verificar.
    :return: Retorna o valor ou uma mensagem de Erro, se estiver fora dos parâmetros.
    Criado por: Filipe Cavinato
    """
    while True:
        if valor.isnumeric():
            return valor
        else:
            print(f'\033[31mERRO: Digite um número inteiro valido!!\033[m')
            valor = input('Digite um número: ').strip()


n = leia_int(input('Digite um número: ').strip())
print(f'Você digitou o número {n}')
print('------ Fim do Programa ------')
