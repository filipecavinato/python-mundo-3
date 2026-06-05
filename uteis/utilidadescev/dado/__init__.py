# Modulo criado por Filipe Cavinato
from encodings import utf_8


def leia_dinheiro(msg):
    while True:
        x = str(input(msg)).strip()
        if x.isalpha() or x == '':
            print(f'\033[31m ERRO: "{x.title()}" é um preço inválido!\033[m')
        else:
            if ',' in x:
                return float(x.replace(',','.'))
            return float(x)

def leia_int(msg):
    while True:
        try:
            x = int(input(msg))
        except KeyboardInterrupt:
            print()
            print('\033[31m O usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31m ERRO: Por Favor digite um número inteiro válido\033[m')
        else:
            return x

def leia_float(msg):
    while True:
        try:
            x = float(input(msg))
        except KeyboardInterrupt:
            print()
            print('\033[31m O usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31m ERRO: Por Favor digite um número real válido\033[m')
        else:
            return x

def mostrar_dados(arquivo):
    global dados
    from pathlib import Path
    import json
    titulo = 'Pessoas Cadastradas'
    tam = len(titulo) + 18
    print('-' * tam)
    print(f'         {titulo}')
    print('-' * tam)
    local = Path("/home/filipe/projetos/curso-em-video/python/python-mundo-3/banco-de-dados.json")
    if Path(local).exists():
        arq = open(arquivo, 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()
    else:
        Path.touch(local)
        Path.write_text(local, '[]')
        arq = open(arquivo, 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()
    return dados

def cadastrar_pessoa(arquivo):
    from pathlib import Path
    import json
    titulo = 'Novo Cadastro'
    tam = len(titulo) + 16
    print('-' * tam)
    print(f'        {titulo}')
    print('-' * tam)
    while True:
        nome = str(input('Nome: ')).strip().title()
        if nome.replace(' ','').isalpha() and nome.strip() != 0:
            break
        else:
            print('\033[31m Erro: Por Favor, Digite um nome válido \033[m')
    while True:
        try:
            idade = int(input('Idade: '))
        except (TypeError, ValueError):
            print('\033[31m Erro: Por Favor, digite um número inteiro valido!\033[m')
        else:
            break

    pessoa = {"nome": nome, "idade": idade}
    local = Path("/home/filipe/projetos/curso-em-video/python/python-mundo-3/banco-de-dados.json")
    if Path(local).exists():
        arq = open(arquivo, 'r', encoding='utf-8')
        lista = json.load(arq)
        arq.close()
        lista.append(pessoa)
        arq_novo = open(arquivo, 'w', encoding='utf-8')
        json.dump(lista, arq_novo, indent=4, ensure_ascii=False)
        arq_novo.close()
