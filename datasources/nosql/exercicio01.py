from pymongo import MongoClient

# Conecta ao MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Cria um banco de dados chamado 'teste'
db = client["cinema"]

# Cria uma collection e insere um documento
db["usuarios"].insert_many([
    {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 17, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 34, "cidade": "Curitiba"},
    {"nome": "Diego", "idade": 22, "cidade": "São Paulo"},
])

# Imprime maiores de 18 anos
print("--------------MAIORES DE 18 ANOS---------------")
for doc in db["usuarios"].find({"idade": { "$gt": 18}}):
    print(doc)

# Imprime usuários de São Paulo
print("--------------MORADORES DE SÃO PAULO---------------")
for doc in db["usuarios"].find({"cidade": "São Paulo"}):
    print(doc)

#Insira um novo usuário chamado Eduardo, 25 anos, Belo Horizonte, mas com um campo extra chamado filmes_favoritos contendo uma lista com pelo menos 2 filmes. 
# Depois busque e imprima ele.
print("--------------EDUARDO---------------")
db["usuarios"].insert_one(
    {"nome": "Eduardo", "idade": 25, "cidade": "Belo Horizonte", "filmes_favoritos": ["Batman", "Superman"]}
)
for doc in db["usuarios"].find({"nome": "Eduardo"}):
    print(doc)

# Limpa o banco de teste 
client.drop_database("cinema")
print("Tudo certo!")
