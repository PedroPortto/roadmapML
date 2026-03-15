##Exercicio utilizando o mongodb para armazenar dados consumidos de uma api
from pymongo import MongoClient
import requests
import time

connection = MongoClient("mongodb://localhost:27017/")
db = connection['pokedex_db']
collection = db['pokemons_coletados']

url = "https://pokeapi.co/api/v2/pokemon"
paginas = 0

while url and paginas < 2:

    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        dados = resposta.json()
        for y in dados['results']:
            collection.insert_one(y)

        url = dados['next']
        paginas += 1

        print(f"Página {paginas} salva no MongoDB! Indo dormir...")     
        time.sleep(2)
    
    else:
        print(f"Conexao problematica: {resposta.status_code}")

print(f"Primeiro pokemon: \n{collection.find_one()}")