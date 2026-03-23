import pandas as pd

# 1. Criando nossa tabela na memória RAM
dados = {
    "id_transacao": [1001, 1002, 1003],
    "produto": ["Notebook", "Mouse", "Teclado"],
    "valor": [5500.00, 150.00, 350.00]
}
df_vendas = pd.DataFrame(dados)

print("Tabela original na RAM:")
print(df_vendas)

# 2. CREATE: Salvando a tabela no HD usando o superpoder do Parquet
nome_arquivo = "vendas_massivas.parquet"

print(f"\nComprimindo e guardando nas 'gavetas' do arquivo {nome_arquivo}...")
# O Pandas usa o pyarrow automaticamente aqui!
df_vendas.to_parquet(nome_arquivo, index=False)

# 3. READ: Lendo o arquivo Parquet de volta para a RAM
print("\nAbrindo o arquivo Parquet...")
df_recuperado = pd.read_parquet(nome_arquivo)

print("\nDados recuperados na velocidade da luz:")
print(df_recuperado)