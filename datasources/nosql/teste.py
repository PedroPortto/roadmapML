from pymongo import MongoClient

# Conecta ao MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Cria um banco de dados chamado 'teste'
db = client["teste"]

# Cria uma collection e insere um documento
db["teste_collection"].insert_one({"mensagem": "MongoDB funcionando!"})

# Busca e imprime o documento
doc = db["teste_collection"].find_one()
print(doc)

# Limpa o banco de teste
client.drop_database("teste")
print("Tudo certo!")