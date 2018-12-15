import requests

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://devopers.com.br'}

meus_cookies = {'Ultima-visita': '201812142246'}

dados = {'username': 'vinicius',
         'password': '123456'}

requisicao = requests.post('https://putsreq.com/pxGHz0rnFbrVdJjEuyuj',
                           headers=cabecalho,
                           cookies=meus_cookies,
                           data=dados)

print(requisicao.text)
