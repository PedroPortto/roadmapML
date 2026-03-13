import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, GlobalAveragePooling1D, Dense, TextVectorization
from keras.optimizers import Adam

print("1. Recebendo os chamados de TI...")
chamados = [
    "O sistema travou e a tela ficou preta", # Problema Local (0)
    "O servidor caiu de novo",               # Problema de Infraestrutura (1)
    "A tela do sistema travou"               # Problema Local (0)
]

print("2. Criando o gabarito oficial...")
gabarito = np.array([0, 1, 0])

print("3. Cortando as palavras e criando os RGs...")
tesoura = TextVectorization(max_tokens=100, output_sequence_length=10)
tesoura.adapt(chamados)
chamados_padronizados = tesoura(chamados)

print("\n5. Construindo o cerebro leitor (Rede Neural NLP)...")
modelo_nlp = Sequential()

# O Mapa de Significado (Embedding): 
# 100 palavras no limite do dicionario, 16 coordenadas de profundidade, e 10 espacos na caixa
modelo_nlp.add(Embedding(input_dim=100, output_dim=16, input_length=10))

# O Resumidor: Pega a vibe geral da frase
modelo_nlp.add(GlobalAveragePooling1D())

# Os Detetives: 24 detetives procurando padroes ocultos
modelo_nlp.add(Dense(units=24, activation='relu'))

# O Chefe Final: 1 unico chefe que diz se e 0 (Local) ou 1 (Infraestrutura)
modelo_nlp.add(Dense(units=1, activation='sigmoid'))

# As regras do jogo mudaram um pouco: usamos 'binary_crossentropy' porque so temos 2 opcoes (0 ou 1)
modelo_nlp.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.05), metrics=['accuracy'])

print("\n6. Treinando a IA a ler chamados de suporte...")
# Coloquei 50 epocas porque textos demoram um pouco mais para a IA pegar o padrao
modelo_nlp.fit(chamados_padronizados, gabarito, epochs=50, verbose=1)

print("\nTreinamento de Leitura Finalizado!")

print("\n--- TESTE AO VIVO: LENDO UM CHAMADO NOVO ---")

# 1. Um usuario abriu um ticket novo que a IA nunca viu na vida
chamado_novo = ["A tela do meu pc travou tudo"]

# 2. Passamos a mesma tesoura para traduzir para a matematica
chamado_novo_padronizado = tesoura(chamado_novo)

# 3. Colocamos os zeros para a caixa ficar com 10 espacos perfeitos
print("\nComo a IA enxerga o chamado novo:")
print(chamado_novo_padronizado[0])

# 4. A maquina faz a previsao! 
# Como usamos o ativador 'sigmoid', ela cospe uma porcentagem entre 0.0 e 1.0
previsao = modelo_nlp.predict(chamado_novo_padronizado)

# Pegando o numero exato da resposta
porcentagem_ia = previsao[0][0]

print(f"\nA porcentagem crua da mente da IA: {porcentagem_ia}")

# 5. Traduzindo a porcentagem para a resposta humana
# Se for menor que 0.5 (50%), esta mais perto do 0 (Local). Se for maior, esta perto do 1 (Infraestrutura)
if porcentagem_ia < 0.5:
    print("VEREDITO: A IA diz que e um Problema Local (Gaveta 0)")
else:
    print("VEREDITO: A IA diz que e um Problema de Infraestrutura (Gaveta 1)")