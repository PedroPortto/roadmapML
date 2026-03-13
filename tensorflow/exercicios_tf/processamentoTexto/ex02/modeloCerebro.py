import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, GlobalAveragePooling1D, Dense, TextVectorization
from keras.optimizers import Adam

print("1. Lendo os reviews do aplicativo...")
avaliacoes = [
    "comida horrivel chegou fria",       # 0 (Critica)
    "atrasou muito nao recomendo",       # 0 (Critica)
    "tudo pessimo e sem sabor",          # 0 (Critica)
    "muito bom adorei o lanche",         # 1 (Elogio)
    "perfeito chegou super rapido",      # 1 (Elogio)
    "comida maravilhosa nota dez"        # 1 (Elogio)
]
gabarito = np.array([0, 0, 0, 1, 1, 1])

# A Tesoura aprende o vocabulario solta, mas depois entra pro cerebro!
tesoura = TextVectorization(max_tokens=100, output_sequence_length=10)
tesoura.adapt(avaliacoes)

print("2. Construindo o Cerebro Embutido...")
modelo_ifood = Sequential()

# O GRANDE TRUQUE: A tesoura e a primeira camada! 
modelo_ifood.add(tesoura)

# SUA MISSAO AQUI: Complete o resto do cerebro exatamente como voce ja sabe!
# - Embedding (input_dim=100, output_dim=16)
# - GlobalAveragePooling1D()
# - Dense (32 detetives, ativador relu)
# - Dense (1 chefe final, ativador sigmoid)

modelo_ifood.add(Embedding(input_dim=100,output_dim=16))
modelo_ifood.add(GlobalAveragePooling1D())
modelo_ifood.add(Dense(units=32,activation='relu'))
modelo_ifood.add(Dense(units=1,activation='sigmoid'))


# Compilando e Treinando (Nota: Agora a gente passa as 'avaliacoes' em texto puro no fit!)
modelo_ifood.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
modelo_ifood.fit(tf.constant(avaliacoes), gabarito, epochs=30, verbose=1)

print("\n3. Salvando a IA no disco...")
modelo_ifood.save("cerebro_ifood.keras")
print("Arquivo cerebro_ifood.keras gerado com sucesso!")