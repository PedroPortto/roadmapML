import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense, Input
from keras.models import Sequential

modelo = Sequential()

resposta = np.array([1,1], [0,0], [1,0], [0,1])
gabarito = np.array([0], [0], [1], [1])

modelo.add(Input(shape=2,))
modelo.add(Dense(units=2, activation='sigmoid'))
modelo.add(Dense(units=1, activation='sigmoid'))

modelo.compile(loss='mean_squared_error',optimizer='adam')
grafico = modelo.fit(resposta, gabarito,epochs=10000,verbose=0)

previsoes = modelo.predict(resposta)
print("Previsões:")
print("-" * 30)
print(previsoes)

plt.plot(grafico.history['loss'])
plt.title('A Montanha do Erro (Loss)')
plt.ylabel('Tamanho do Erro')
plt.xlabel('Epocas (Tempo de Estudo)')

plt.show()