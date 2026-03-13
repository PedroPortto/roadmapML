import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, TextVectorization
from keras.optimizers import Adam
import numpy as np

avaliacoes = [
    "o filme nao e nada bom muito chato", # 0 (Odiou)
    "historia pessima odiei tudo",        # 0 (Odiou)
    "nao gostei achei o filme chato",     # 0 (Odiou)
    "nada de chato o filme e muito bom",  # 1 (Amou)
    "o filme nao e chato eu adorei",      # 1 (Amou) -> Olha a gente ensinando que "nao e chato" é bom!
    "muito bom o filme perfeito",         # 1 (Amou)
    "nao e chato gostei",
    "o filme nao e chato"
]
gabarito = np.array([0, 0, 0, 1, 1, 1, 1, 1])

tesoura = TextVectorization(max_tokens=75, output_sequence_length=10)
tesoura.adapt(avaliacoes)

modeloAvaliacoesFilme = Sequential()
modeloAvaliacoesFilme.add(tesoura)
modeloAvaliacoesFilme.add(Embedding(input_dim=75, output_dim=16, mask_zero=True))
modeloAvaliacoesFilme.add(LSTM(units=16))
modeloAvaliacoesFilme.add(Dense(units=1, activation='sigmoid'))
modeloAvaliacoesFilme.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.02), metrics=['accuracy'])
modeloAvaliacoesFilme.fit(tf.constant(avaliacoes), gabarito, epochs=50)

testeFilme = ['o filme nao e chato']
resultadoFinal = modeloAvaliacoesFilme.predict(tf.constant(testeFilme))

print(resultadoFinal)
if resultadoFinal < 0.5:
    print("Filme é muito ruim")
else:
    print("Filme é muito bom")