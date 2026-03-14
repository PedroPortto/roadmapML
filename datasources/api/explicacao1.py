import requests

#Salvando o endereço em uma variavel
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

#Fazendo a primeira requisição no endereço
resposta = requests.get(url)

#Verificando se conectou
if resposta.status_code == 200:
    print("Conectado com sucesso!")

    #Transformando em JSON
    dados = resposta.json()

    #Dados sem especificar qual você quer
    print(f"Dados cru:\n{dados}")

    #Extraindo somente o necessario
    precoBitCoin = float(dados['price'])
    print(f"Preco do bitcoin hoje:\n{precoBitCoin}")

else:
    print(f"Ocorreu algum erro na conexão.\nCodigo do erro:\n{resposta.status_code}")

