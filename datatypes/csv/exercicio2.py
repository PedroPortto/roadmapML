import pandas as pd

# 1. Criando dados "na mão" (simulando dados que vieram de uma API, por exemplo)
dados_coletados = {
    "id_cliente": [101, 102, 103],
    "idade": [25, 34, 29],
    "comprou_produto": ["sim", "nao", "sim"]
}

# 2. Transformando o Dicionário em um DataFrame (Tabela na RAM)
df_clientes = pd.DataFrame(dados_coletados)
print("Tabela na memória RAM:")
print(df_clientes)

# 3. O Comando Mágico: Salvando no Disco Rígido
nome_do_arquivo = "meus_clientes_processados.csv"

print(f"\nSalvando os dados no arquivo: {nome_do_arquivo}...")
df_clientes.to_csv(nome_do_arquivo, index=False)

print("Sucesso! Pode olhar na sua pasta, o arquivo físico está lá!")