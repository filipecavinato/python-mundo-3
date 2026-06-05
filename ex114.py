# Script criado por Filipe Cavinato
import urllib.request

try:
    url = 'https://www.pudim.com.br'
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    urllib.request.urlopen(req)
except:
    print('\033[31m O Site Pudim não está acessível no momento.\033[m')
else:
    print('\033[35m Consegui acessar o site Pudim com sucesso!.\033[m')
print('------ Fim do Programa ------')
