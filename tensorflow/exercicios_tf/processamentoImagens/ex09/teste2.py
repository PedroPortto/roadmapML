from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

print("1. Baixando o guarda-roupa da internet...")
(fotos_treino, gabarito_treino), (fotos_teste, gabarito_teste) = fashion_mnist.load_data()

print("2. Facilitando a matematica (Normalizacao)...")
fotos_treino = fotos_treino / 255.0
fotos_teste = fotos_teste / 255.0

print("3. Preparando as fotos para a Lupa (adicionando o canal de cor)...")
# Avisando que a foto tem 28x28 de tamanho e apenas 1 canal de cor (preto e branco)
fotos_treino_cnn = fotos_treino.reshape(-1, 28, 28, 1)
fotos_teste_cnn = fotos_teste.reshape(-1, 28, 28, 1)

print("\n4. Construindo o cerebro com Olho de Aguia (CNN)...")
modelo = Sequential()

# A Lupa Magica: 32 lupas de 3x3 passeando pela foto
modelo.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# O Resumidor: Encolhe a foto pegando so os tracos mais fortes
modelo.add(MaxPooling2D((2, 2)))

# Achata tudo para a fila indiana
modelo.add(Flatten())

# O Batalhao de detetives e os 10 Especialistas finais
modelo.add(Dense(units=128, activation='relu'))
modelo.add(Dense(units=10, activation='softmax'))

# As regras do jogo
modelo.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("\n5. Treinando os detetives com a Lupa. Isso vai exigir mais do processador...")
historico = modelo.fit(fotos_treino_cnn, gabarito_treino, epochs=5)

print("\nTreinamento CNN Finalizado!")