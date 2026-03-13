import numpy as np

def sigmoid(z):
    return 1/ (1 + np.exp(-z))

def derivada_sigmoid(x):
    return x * (1-x)

entradas = np.array([
    [1,1],
    [0,0],
    [1,0],
    [0,1]
])

gabaritos = np.array([
    [1], 
    [1], 
    [0], 
    [0]
])

# Isso garante que o aleatório seja sempre o mesmo toda vez que você rodar o código
np.random.seed(42) 

# Camada Oculta (2 Detetives)
# Como temos 2 entradas e 2 detetives, a tabela de pesos precisa ser 2x2
pesos_detetives = np.random.uniform(size=(2, 2)) 
vies_detetives = np.random.uniform(size=(1, 2))

# Camada de Saída (1 Chefe)
# O chefe ouve 2 detetives, então a tabela dele é 2x1
pesos_chefe = np.random.uniform(size=(2, 1)) 
vies_chefe = np.random.uniform(size=(1, 1))

# 1. As entradas batem de frente com os pesos dos detetives
soma_detetives = np.dot(entradas, pesos_detetives) + vies_detetives

# 2. Passamos no Sigmoide para virar porcentagem
opiniao_detetives = sigmoid(soma_detetives)

# 3. As opiniões dos detetives batem de frente com os pesos do chefe
soma_chefe = np.dot(opiniao_detetives, pesos_chefe) + vies_chefe

# 4. O chefe dá o veredito final
previsao_final = sigmoid(soma_chefe)

print("Previsões do Chefe antes de estudar:")
print(previsao_final)

taxa_aprendizado = 0.5
epocas = 10000

# O Laço de Treinamento
for epoca in range(epocas):
    
    # --- A Linha de Montagem (Forward Pass) ---
    soma_detetives = np.dot(entradas, pesos_detetives) + vies_detetives
    opiniao_detetives = sigmoid(soma_detetives)
    
    soma_chefe = np.dot(opiniao_detetives, pesos_chefe) + vies_chefe
    previsao_final = sigmoid(soma_chefe)
    
    # --- O Jogo da Culpa (Backpropagation) ---
    
    # 1. Calculamos o erro puro do chefe (Gabarito menos Palpite)
    erro_chefe = gabaritos - previsao_final
    # O tamanho do passo de ajuste é o erro multiplicado pela derivada
    ajuste_chefe = erro_chefe * derivada_sigmoid(previsao_final)
    
    # 2. O Chefe joga a culpa nos Detetives
    # Usamos o .T para deitar a tabela de pesos e a multiplicação encaixar
    erro_detetives = ajuste_chefe.dot(pesos_chefe.T)
    ajuste_detetives = erro_detetives * derivada_sigmoid(opiniao_detetives)
    
    # 3. Atualizamos a mente de todo mundo (Os Novos Pesos)
    # Usamos o .T de novo para encaixar as tabelas na hora de somar o aprendizado
    pesos_chefe += opiniao_detetives.T.dot(ajuste_chefe) * taxa_aprendizado
    vies_chefe += np.sum(ajuste_chefe, axis=0, keepdims=True) * taxa_aprendizado
    
    pesos_detetives += entradas.T.dot(ajuste_detetives) * taxa_aprendizado
    vies_detetives += np.sum(ajuste_detetives, axis=0, keepdims=True) * taxa_aprendizado

# O Boletim Final depois do estagiário ler o manual 10.000 vezes
print("Previsões Finais após 10.000 épocas de estudo:")
print(previsao_final)