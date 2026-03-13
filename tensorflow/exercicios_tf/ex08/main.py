import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Input

# 1. O link direto para a planilha do Titanic na internet
url_titanic = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# 2. A secretária (Pandas) lê a planilha e guarda na variável 'planilha'
print("Baixando a planilha da internet...")
planilha = pd.read_csv(url_titanic)

# 3. Pedimos para ela mostrar apenas as 5 primeiras linhas para não inundar o terminal
print("\nAs 5 primeiras linhas do arquivo:")
print(planilha.info())


print("\nIniciando a faxina nos dados...")

# 1. O comando .drop() joga fora a lista de colunas inuteis que atrapalham a IA. 
# O axis=1 avisa que estamos deletando colunas inteiras (na vertical).
planilha = planilha.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# 2. O comando .fillna() preenche os buracos vazios da coluna Idade. 
# O comando .mean() pega a media matematica das idades que ja existem.
planilha['Age'] = planilha['Age'].fillna(planilha['Age'].mean())

# 3. Fazendo o Raio-X novamente para ver se a casa esta limpa
print("\nNovo Raio-X apos a limpeza:")
print(planilha.info())

planilha['Sex'] = planilha['Sex'].map({'male': 0, 'female':1})
print("\nRaio-X final para confirmar o sexo traduzido:")
print(planilha.info())
print(planilha.head())

print("\nSeparando as perguntas do gabarito...")

# 1. As entradas: Pegamos a planilha inteira e "deletamos" a coluna Survived. 
# O que sobra são apenas as perguntas.
entradas = planilha.drop('Survived', axis=1)

# 2. O gabarito: Pegamos APENAS a coluna Survived da planilha original.
gabarito = planilha['Survived']

print("\nFormato das Entradas (Perguntas):")
print(entradas.info())

print("\nFormato do Gabarito (Respostas):")
print(gabarito.head())

print("\nSeparando as perguntas do gabarito...")

# 1. As entradas: Pegamos a planilha inteira e "deletamos" a coluna Survived. 
# O que sobra são apenas as perguntas.
entradas = planilha.drop('Survived', axis=1)

# 2. O gabarito: Pegamos APENAS a coluna Survived da planilha original.
gabarito = planilha['Survived']

print("\nFormato das Entradas (Perguntas):")
print(entradas.info())

print("\nFormato do Gabarito (Respostas):")
print(gabarito.head())

modelo = Sequential()
modelo.add(Input(shape=(6,)))
modelo.add(Dense(units=8, activation='sigmoid'))
modelo.add(Dense(units=1, activation='sigmoid'))
modelo.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

historico = modelo.fit(entradas, gabarito, epochs=200)

print("\nAnalisando o passageiro fantasma...")

# 1. O dicionário com os dados do Pedro
# A ordem tem que ser exatamente a mesma das colunas que sobraram na faxina
dados_pedro = {
    'Pclass': [3], # Viajando na 3a classe (a mais barata)
    'Sex': [0],    # 0 porque traduzimos 'male' (homem) para 0
    'Age': [23],   # Coloquei 23 anos como exemplo, pode alterar para a sua idade exata
    'SibSp': [0],  # Nenhum irmao ou esposa a bordo
    'Parch': [0],  # Nenhum pai ou filho a bordo
    'Fare': [8.05] # Pagou 8 dolares na passagem
}

# 2. A secretária transforma o dicionário em uma mini-planilha de 1 linha
passageiro_fantasma = pd.DataFrame(dados_pedro)

# 3. O Chefe avalia a chance de sobrevivência
chance_sobreviver = modelo.predict(passageiro_fantasma)

print("\nA chance de sobrevivencia e de:")
print(chance_sobreviver)
