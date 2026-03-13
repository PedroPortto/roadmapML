import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, GlobalAveragePooling1D, Dense, TextVectorization
from keras.optimizers import Adam

print("1. Coletando o log do chat do servidor...")
mensagens_chat = [
    "gg bom jogo galera",             # 0 (De boa)
    "onde fica a base inimiga?",      # 0 (De boa)
    "me passa uns itens ai",          # 0 (De boa)
    "seu lixo desinstala o jogo",     # 1 (Toxico)
    "time horrivel vao se ferrar",    # 1 (Toxico)
    "cala a boca seu nub",            # 1 (Toxico)
]

gabarito = np.array([0, 0, 0, 1, 1, 1])

print("2. Preparando a Maquina de Leitura...")
# SUA MISSAO 1:
# - Crie a tesoura (TextVectorization) com max_tokens=100 e tamanho de caixa 10.
# - Faca ela aprender o vocabulario (.adapt)
# - Transforme o chat em numeros e guarde na variavel 'chat_padronizado'.

tesoura = TextVectorization(max_tokens=100, output_sequence_length=10)
tesoura.adapt(mensagens_chat)
chat_padronizado = tesoura(mensagens_chat)

print("3. Construindo o Cerebro do Moderador...")
modelo_moderador = Sequential()

# SUA MISSAO 2:
# - Adicione a porta de entrada (Embedding com input_dim=100, output_dim=16)
# - Adicione o resumidor de frases (GlobalAveragePooling1D)
# - Adicione o batalhao de detetives (Dense com 32 units, ativador relu)
# - Adicione o Juiz Final (Dense com 1 unit, ativador sigmoid)
modelo_moderador.add(Embedding(input_dim=100, output_dim=16))
modelo_moderador.add(GlobalAveragePooling1D())
modelo_moderador.add(Dense(units=32, activation='relu'))
modelo_moderador.add(Dense(units=1, activation='sigmoid'))

print("4. Treinando o Moderador...")
# SUA MISSAO 3:
# - Compile o modelo (binary_crossentropy, otimizador Adam com learning_rate=0.01, metrics=['accuracy'])
# - Treine o modelo usando o 'chat_padronizado' por 40 epocas.
modelo_moderador.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
modelo_moderador.fit(chat_padronizado,gabarito,epochs=40)

print("\n--- TESTANDO O MODERADOR AO VIVO ---")
chat_novo = ["VAI SE FUDER FDP"]

# SUA MISSAO 4: O Veredito!
# - Passe o 'chat_novo' na tesoura.
# - Faca o modelo prever (predict) o resultado.
# - Imprima a porcentagem crua na tela.
# - Crie o bloco if/else para imprimir "Mensagem limpa" ou "Jogador Banido!" baseado na porcentagem.
chat_novo_padronizado = tesoura(chat_novo)
respostaModerador = modelo_moderador.predict(chat_novo_padronizado)

print(respostaModerador)
if respostaModerador < 0.5:
    print("Mensagem de boa pode passar")
else:
    print("MENSAGEM OFENSIVA")

modelo_moderador.save("cerebro_moderador.keras")