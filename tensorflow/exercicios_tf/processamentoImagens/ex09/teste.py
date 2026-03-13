# No topo do seu arquivo novo, chame a ferramenta de carregar
from keras.models import load_model

print("Acordando o detetive com a memoria intacta...")

# O modelo ja nasce treinado e pronto para fazer previsoes!
modelo_treinado = load_model('cerebro_roupas.keras')

print("Detetive pronto para trabalhar!")