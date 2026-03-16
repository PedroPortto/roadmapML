import pandas as pd

arquivoJSON = "usuarios.json"
df = pd.read_json(arquivoJSON)

print("Veja como o pandas viu o JSON")
print(df)
