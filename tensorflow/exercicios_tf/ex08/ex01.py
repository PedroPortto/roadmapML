#exercicio analisando phishing
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam

print("Baixando os logs de rede do servidor...")

# --- IGNORE ESSA PARTE --- 
# (Esse bloco apenas gera 1000 sites ficticios e bagunca alguns dados de proposito para voce limpar)
np.random.seed(42)
tamanho = np.random.randint(10, 200, 1000)
arroba = np.random.choice(['sim', 'nao'], 1000)
idade = np.random.randint(1, 120, 1000).astype(float)
redirecionamentos = np.random.randint(0, 10, 1000)
phishing = np.where((tamanho > 100) | (arroba == 'sim') | (redirecionamentos > 4), 1, 0)
idade[np.random.choice(1000, 50, replace=False)] = np.nan # Criando os buracos!

planilha = pd.DataFrame({
    'Tamanho_URL': tamanho,
    'Possui_Arroba': arroba,
    'Idade_Dominio_Meses': idade,
    'Qtd_Redirecionamentos': redirecionamentos,
    'Eh_Phishing': phishing
})
# -------------------------

# Faca um print(planilha.info()) aqui embaixo para fazer o seu Raio-X inicial!

print('Antes:')
print('-' * 30)
print(planilha.info())
print(planilha.head())


planilha['Possui_Arroba'] = planilha['Possui_Arroba'].replace({'sim': 1, 'nao': 0})
planilha['Idade_Dominio_Meses'] = planilha['Idade_Dominio_Meses'].fillna(planilha['Idade_Dominio_Meses'].mean())

print('Depois:')
print('-' * 30)
print(planilha.info())
print(planilha.head())

entradas = planilha.drop(['Eh_Phishing'], axis=1)
gabarito = planilha['Eh_Phishing']

modelo = Sequential()
modelo.add(Input(shape=(4,)))
modelo.add(Dense(units=8, activation='sigmoid'))
modelo.add(Dense(units=1, activation='sigmoid'))
modelo.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
historico = modelo.fit(entradas,gabarito,epochs=100)