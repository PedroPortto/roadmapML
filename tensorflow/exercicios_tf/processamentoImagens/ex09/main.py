from keras.models import Sequential
from keras.layers import Dense, Flatten
import numpy as np
# Importando o pacote de imagens de roupas direto do Keras
from keras.datasets import fashion_mnist

print("Baixando o guarda-roupa da internet...")

# O Keras baixa tudo e ja separa as perguntas (fotos) do gabarito (qual roupa e)
(fotos_treino, gabarito_treino), (fotos_teste, gabarito_teste) = fashion_mnist.load_data()

print("\nDownload concluido com sucesso!")
print("Quantidade de fotos para treinar os detetives:", len(fotos_treino))
print("Quantidade de fotos separadas para o teste final:", len(fotos_teste))

print("\nFacilitando a matematica para os detetives (Normalizacao)...")

# Dividimos o valor de todos os pixels das 60 mil fotos por 255
fotos_treino = fotos_treino / 255.0

# Fazemos a mesma coisa com as 10 mil fotos da prova final
fotos_teste = fotos_teste / 255.0

print("Fotos normalizadas com sucesso! Os valores agora estao entre 0 e 1.")

print("\nConstruindo o cerebro da maquina...")

modelo = Sequential()

# 1. A porta de entrada que estica o quadrado 28x28 em uma linha reta de 784 numeros
modelo.add(Flatten(input_shape=(28, 28)))

# 2. O batalhao com 128 detetives para encontrar padroes no desenho (usando o veloz relu)
modelo.add(Dense(units=128, activation='relu'))

# 3. A saida com 10 especialistas (um para cada tipo de roupa) e o ativador de porcentagem multipla
modelo.add(Dense(units=10, activation='softmax'))

# 4. As regras do jogo. 
# Como agora e multipla escolha (0 a 9) e nao mais Sim/Nao, a regua do erro muda de nome:
modelo.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Iniciando o treinamento intensivo (5 epocas)...")

# Vamos treinar com a pasta de 60 mil fotos por apenas 5 epocas para o computador nao fritar
historico = modelo.fit(fotos_treino, gabarito_treino, epochs=5)

print("\nTreinamento Finalizado!")

print("\n--- HORA DA VERDADE: A PROVA FINAL ---")

# O professor Adam aplica a prova nas 10 mil fotos ineditas e calcula a nota
loss_teste, acuracia_teste = modelo.evaluate(fotos_teste, gabarito_teste)

print("\nNota final na prova inesquecivel:", acuracia_teste)

print("\n--- TESTE AO VIVO: PREVENDO UMA ROUPA MISTERIOSA ---")

# Criamos um dicionario simples para traduzir o numero de 0 a 9 para o nome humano
nomes_roupas = ['Camiseta', 'Calca', 'Sueter', 'Vestido', 'Casaco', 
                'Sandalia', 'Camisa', 'Tenis', 'Bolsa', 'Bota']

# Pegamos apenas a FOTO 0 da pasta de testes
# Colocamos o [0:1] porque o Keras so aceita ler fotos se estiverem no formato de "lista"
foto_misteriosa = fotos_teste[0:1]

# O Chefe analisa a foto e gera as 10 porcentagens
previsoes = modelo.predict(foto_misteriosa)

print("\nO que o cerebro da IA pensou (As 10 porcentagens de certeza):")
print(previsoes)

# O argmax procura qual foi a maior porcentagem e devolve o numero do especialista vencedor
numero_vencedor = np.argmax(previsoes)

# Traduzimos o numero vencedor para a palavra humana
palpite_da_ia = nomes_roupas[numero_vencedor]

# Pegamos a resposta verdadeira no nosso gabarito para comparar
resposta_real = nomes_roupas[gabarito_teste[0]]

print("\nRESULTADO FINAL:")
print(f"A Inteligencia Artificial apostou que a foto e: {palpite_da_ia}")
print(f"O gabarito oficial diz que a foto e: {resposta_real}")

print("\nSalvando o cerebro da IA no disco...")

# O final .keras e o formato oficial e moderno para salvar Inteligencias Artificiais
modelo.save('cerebro_roupas.keras')

print("Cerebro salvo com sucesso no arquivo 'cerebro_roupas.keras'!")