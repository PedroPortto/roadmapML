import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, TextVectorization
from keras.optimizers import Adam
import numpy as np

print("1. Recebendo os chamados confusos...")
# Repare que as duas frases tem exatamente as mesmas palavras!
chamados = [
    "o sistema nao esta bom travou tudo", # 1 (Critico)
    "esta tudo bom o sistema nao travou"  # 0 (Resolvido)
]

gabarito = np.array([1, 0])

print("2. Ligando a Tesoura (TextVectorization)...")
# SUA MISSAO 1:
# - Crie a tesoura limitando a 50 palavras e tamanho de caixa 8.
# - Faca ela aprender as palavras (adapt).

tesoura = TextVectorization(max_tokens=50, output_sequence_length=8)
tesoura.adapt(chamados)


print("3. Construindo o Cerebro com Memoria...")
modelo_memoria = Sequential()

# SUA MISSAO 2:
# - Adicione a tesoura como a primeirissima camada.
# - Adicione o Mapa de Significados (Embedding) com input_dim=50 e output_dim=16.
modelo_memoria.add(tesoura)
modelo_memoria.add(Embedding(input_dim=50,output_dim=16))
# A GRANDE MAGICA DE HOJE:
# Vamos demitir o resumidor e contratar o leitor com caderninho!
modelo_memoria.add(LSTM(units=16))

# SUA MISSAO 3:
# - Adicione o Juiz Final (Dense com 1 unit e ativador sigmoid). Nao precisamos dos 32 detetives hoje para um teste rapido.
modelo_memoria.add(Dense(units=1,activation='sigmoid'))

print("4. Treinando o leitor...")
# SUA MISSAO 4:
# - Compile o modelo (binary_crossentropy, Adam com learning_rate=0.02, accuracy).
# - Treine (fit) usando a caixa oficial do tf.constant(chamados) e o gabarito. Coloque umas 50 epocas.
modelo_memoria.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.02), metrics=['accuracy'])
modelo_memoria.fit(tf.constant(chamados), gabarito, epochs=50, verbose=1)

print("\n--- TESTE DE MEMORIA ---")
# Vamos ver se ele entendeu a ordem da primeira frase!
frase_teste = tf.constant(["esta tudo bom o sistema nao travou"])
resultado = modelo_memoria.predict(frase_teste)

print(f"Porcentagem de ser um erro Critico (Gaveta 1): {resultado[0][0]}")