import pandas as pd

df = pd.read_excel("vendas_2023.xlsx", sheet_name="trimestre_4")
df.to_csv("dados_q4_prontos.csv", index=False)
print("Arquivo convertido e salvo com sucesso!")