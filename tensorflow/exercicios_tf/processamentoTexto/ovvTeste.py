from keras.layers import TextVectorization

# 1. Nossos chamados de treino antigos
chamados_treino = [
    "O sistema travou e a tela ficou preta",
    "O servidor caiu de novo",
    "A tela do sistema travou"
]

print("Criando a tesoura com a regra do OOV...")
# A MAGICA ACONTECE AQUI: Adicionamos o oov_token="<OOV>"
tesoura = TextVectorization(max_tokens=100,output_sequence_length=10)
tesoura.adapt(chamados_treino)

print("\nDicionario de RGs atualizado:")
print(tesoura.get_vocabulary())

# 2. O chamado novo cheio de palavras desconhecidas
chamado_novo = ["A tela do meu pc travou tudo"]

print("\nTraduzindo o chamado novo sem jogar palavras no lixo:")
chamado_novo_numeros = tesoura(chamado_novo)

print(chamado_novo_numeros[0])