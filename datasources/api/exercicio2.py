import requests
import time 

url = "https://pokeapi.co/api/v2/item"
todos_os_itens = []
pagina = 0

while url and pagina < 2:

    resposta = requests.get(url)

    if resposta.status_code == 200:

        dados = resposta.json()
        for name in dados['results']:
            todos_os_itens.append(name['name'])

        pagina += 1
        url = dados['next']
        time.sleep(2)

    else:
        print(f"Erro ao conectar: {resposta.status_code}")

print("Coleta finalizada")
print(f"Total de intens armazenados:{len(todos_os_itens)}")