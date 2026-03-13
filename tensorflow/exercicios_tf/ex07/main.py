import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
import matplotlib.pyplot as plt

# 1. Dados do Apagao
entradas = np.array([[1, 0], [0, 1], [0, 0], [1, 1]])
gabaritos = np.array([[1], [1], [0], [0]])

# 2. Montando o Predio (Com a porta de entrada separada)
modelo = Sequential()
modelo.add(Input(shape=(2,)))
modelo.add(Dense(units=2, activation='sigmoid'))
modelo.add(Dense(units=1, activation='sigmoid'))

# 3. Regras do Jogo
modelo.compile(loss='mean_squared_error', optimizer='adam')

print("Iniciando o treinamento pesado. Aguarde...")

# 4. O Treinamento (Guardando o boletim na variavel historico)
historico = modelo.fit(entradas, gabaritos, epochs=10000, verbose=0)

# 5. O Teste Final
previsoes = modelo.predict(entradas)
print("Previsoes do Chefe apos estudar pelo Keras:")
print(previsoes)

# 6. Desenhando a Montanha do Erro
plt.plot(historico.history['loss'])
plt.title('A Montanha do Erro (Loss)')
plt.ylabel('Tamanho do Erro')
plt.xlabel('Epocas (Tempo de Estudo)')

# Essa e a linha que liga a televisao e mostra a imagem!
plt.show()