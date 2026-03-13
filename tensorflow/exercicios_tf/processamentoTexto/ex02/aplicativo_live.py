import tensorflow as tf
from keras.models import load_model

print("1. Ligando o Servidor do iFood e carregando a IA...")
# Ele puxa a tesoura embutida, o dicionario e os detetives, tudo em 1 segundo!
ia_pronta = load_model(filepath='kerasBrains\cerebro_ifood.keras')

print("2. Recebendo review novo ao vivo...")
review_novo = ["lanche espetacular virei cliente"]

# Colocamos o texto novo na caixa oficial do TensorFlow para nao dar erro
review_oficial = tf.constant(review_novo)

# O predict e o soco final. Ele le e julga na mesma hora.
resultado = ia_pronta.predict(review_oficial)
porcentagem = resultado[0][0]

print(f"\nPorcentagem da IA: {porcentagem}")

# SUA MISSAO FINAL:
# A logica do nosso gabarito era: 0 (Critica) e 1 (Elogio).
if porcentagem < 0.5:
    print("ALERTA: Cliente Insatisfeito (Gaveta 0)")
else:
    print("SUCESSO: Cliente Satisfeito (Gaveta 1)")