import pandas as pd

dfCasas = pd.read_csv("datatypes/csv/imoveis.csv")
print(dfCasas) 
print("-" * 30)
print(dfCasas['preco'])         