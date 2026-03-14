from pymongo import MongoClient

# 1. Conexão
cliente = MongoClient("mongodb://localhost:27017/")

# 2. Selecionando o Banco (Armário) e a Coleção (Gaveta)
db = cliente['recomendacao_db']
colecao = db['cliques_filmes']

# 3. CREATE: Dicionário corrigido 
dic1 = {
    "id_usuario" : 99,
    "filme": "Matrix",
    "tempo_assistido_segundos": 350
}

# Inserindo na coleção correta
colecao.insert_one(dic1)
print("Dado inserido com sucesso!")

# 4. READ: Buscando pela chave exata q
print("\nBuscando o usuário 99 no banco:")
for doc in colecao.find({"id_usuario": 99}):
    print(doc)

