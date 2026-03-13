import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, GlobalAveragePooling1D, Dense, TextVectorization
from keras.optimizers import Adam

print("1. Recebendo as mensagens interceptadas da rede...")
mensagens = [
    "Oi, voce vem para a reuniao de terca?",         # 0 (Seguro)
    "O relatorio financeiro esta no servidor.",      # 0 (Seguro)
    "Vamos almocar naquele restaurante hoje?",       # 0 (Seguro)
    "URGENTE Sua conta foi bloqueada clique aqui",   # 1 (Golpe)
    "Voce ganhou um iphone acesse o link agora",     # 1 (Golpe)
    "Aviso Atualize sua senha bancaria urgente"      # 1 (Golpe)
]

gabarito = np.array([0, 0, 0, 1, 1, 1])

print("2. Ligando o liquidificador de palavras (TextVectorization)...")
# SUA MISSÃO AQUI:
# - Crie a maquina_texto (TextVectorization) limitando a 100 palavras e tamanho de caixa 10.
# - Use o .adapt() para a maquina ler as mensagens.
# - Transforme as mensagens em numeros padronizados guardando na variavel 'mensagens_prontas'.
tesoura = TextVectorization(max_tokens=100, output_sequence_length=10)
tesoura.adapt(mensagens)
mensagensProntas = tesoura(mensagens)
print(mensagensProntas)

print("3. Construindo a Mente do Cao de Guarda...")
modelo_seguranca = Sequential()

# SUA MISSÃO AQUI:
# - Adicione o Embedding (input_dim=100, output_dim=16, input_length=10)
# - Adicione o resumidor (GlobalAveragePooling1D)
# - Adicione os seus 32 detetives (Dense com relu)
# - Adicione o chefe final (Dense com 1 saida e sigmoid)
modelo_seguranca.add(Embedding(input_dim=100, output_dim=16))
modelo_seguranca.add(GlobalAveragePooling1D())
modelo_seguranca.add(Dense(units=32, activation='relu'))
modelo_seguranca.add(Dense(units=1, activation='sigmoid'))

print("4. Treinando a IA de Defesa...")
# SUA MISSÃO AQUI:
# - Crie o otimizador Adam (pode colocar o learning_rate=0.05 para turbinar)
# - Compile o modelo (binary_crossentropy, otimizador, accuracy)
# - Mande o modelo treinar (fit) usando as 'mensagens_prontas' por umas 30 epocas.
modelo_seguranca.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
modelo_seguranca.fit(mensagensProntas,gabarito,epochs=30,verbose=1)

print("\nSistema de Defesa Online e Treinado!")

mensagens_teste = [
    "IMPORTANTE Sua senha do seu banco foi hackeada, clique aqui e mude agora"
]

mensagens_teste_regularizado = tesoura(mensagens_teste)
resultado_final = modelo_seguranca.predict(mensagens_teste_regularizado)

print(resultado_final[0][0])

if resultado_final < 0.5:
    print("É seguro")
else:
    print("É golpe")