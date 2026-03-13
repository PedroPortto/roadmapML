import tensorflow as tf
from keras.layers import Input, Embedding, MultiHeadAttention, Flatten, Dense, TextVectorization, Add
from keras.models import Model
import numpy as np

chamados = [
    "roteador principal queimou ontem", # 1 (Critico)
    "sistema esta rapido e bom"         # 0 (Normal)
]
gabarito = np.array([1, 0])

tamanho_da_frase = 15 # Definimos um tamanho fixo para as cadeiras do cinema

print("1. Ligando a Tesoura...")
tesoura = TextVectorization(max_tokens=50, output_sequence_length=tamanho_da_frase)
tesoura.adapt(chamados)

print("2. A Prancheta de Engenheiro com Ingressos...")
entrada_texto = Input(shape=(1,), dtype=tf.string)
texto_cortado = tesoura(entrada_texto)

# PASSO C.1: O DNA das palavras (Quem é quem)
mapa_palavras = Embedding(input_dim=50, output_dim=16)(texto_cortado)

# PASSO C.2: A impressora de ingressos (Positional Encoding)
# Cria uma lista de cadeiras [0, 1, 2, 3, 4, 5]
cadeiras = tf.range(start=0, limit=tamanho_da_frase, delta=1) 

# A CIRURGIA MAGICA AQUI: Embrulhamos os ingressos em um pacote unico para o Keras nao confundir
cadeiras = tf.expand_dims(cadeiras, axis=0)

# Cria um mapa matematico so para os numeros das cadeiras
mapa_cadeiras = Embedding(input_dim=tamanho_da_frase, output_dim=16)(cadeiras)

# PASSO C.3: Entregando o ingresso na mao de cada palavra (Soma)
texto_com_ingresso = Add()([mapa_palavras, mapa_cadeiras])

# PASSO D: A Atencao (Agora ela cruza a informacao sabendo a ordem exata!)
atencao = MultiHeadAttention(num_heads=2, key_dim=16)(texto_com_ingresso, texto_com_ingresso)

# PASSO E e F: Resumo e Veredito
# PASSO E e F: Resumo e Veredito
resumo = Flatten()(atencao)
saida = Dense(units=1, activation='sigmoid')(resumo)

print("3. Treinando o verdadeiro Transformer...")
modelo_completo = Model(inputs=entrada_texto, outputs=saida)

modelo_completo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
modelo_completo.fit(tf.constant(chamados), gabarito, epochs=50, verbose=1)

print("\nSeu Transformer 100% completo nasceu!")
print("\n--- O TESTE DE FOGO DO TRANSFORMER ---")
# Uma frase nova, cheia de palavras extras, simulando um usuario real
frase_nova = tf.constant(["o sistema queimou a minha paciencia mas esta rapido e bom"])

# Pedimos para a maquina usar os fios invisiveis e dar o veredito
resultado_final = modelo_completo.predict(frase_nova)

print(f"Chance de ser um problema Critico (Gaveta 1): {resultado_final[0][0]}")

if resultado_final[0][0] > 0.5:
    print("Veredito: Chamado Critico! A atencao achou o roteador queimado.")
else:
    print("Veredito: Tudo Normal.")