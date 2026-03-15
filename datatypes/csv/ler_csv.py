import pandas as pd

# 1. Lendo o arquivo CSV do disco rígido
df = pd.read_csv("datatypes/csv/clientes.csv")

# 2. Mostrando a "planilha" na tela
print("Olha como o Pandas organiza os dados:")
print(df)

# 3. Explorando os superpoderes (Acessando uma coluna específica)
print("\nPegando apenas a coluna de idades:")
idades = df['idade']
print(idades)