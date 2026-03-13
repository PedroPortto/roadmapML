import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential
from keras.optimizers import Adam
import matplotlib.pyplot as plt

# Temperaturas em Celsius
entradas = np.array([-40, -10,  0,  8, 15, 22,  38])
# Mesmas temperaturas em Fahrenheit
gabarito = np.array([-40,  14, 32, 46, 59, 72, 100])

modelo = Sequential()
modelo.add(Input(shape=(1,)))
modelo.add(Dense(units=1))
modelo.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.1))
grafico = modelo.fit(entradas, gabarito, epochs=2000, verbose=0)

previsoes = modelo.predict(np.array([100]))
print("Resultados:")
print("-"*30)
print(previsoes)

plt.plot(grafico.history['loss'])

plt.title("A motanha do erro")
plt.ylabel("A curva do erro")
plt.xlabel("Epocas")

plt.show()