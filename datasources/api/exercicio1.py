import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
resposta = requests.get(url)

if resposta.status_code == 200:
    print("Conectado com sucesso!")

    dados = resposta.json()

    pesoPikachu = float(dados['weight'])
    print(f"O peso do pikachu:\n{pesoPikachu}")

else:
    print(f"Erro na conexao:\n{resposta.status_code}")