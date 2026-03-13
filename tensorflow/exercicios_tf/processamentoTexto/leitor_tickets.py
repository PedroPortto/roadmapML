# O segredo esta em colocar o "tensorflow." antes do keras
from keras.layers import TextVectorization

print("1. Recebendo os chamados de TI...")

chamados = [
    "O sistema travou e a tela ficou preta",
    "O servidor caiu de novo",
    "A tela do sistema travou"
]

# Criando a tesoura
tesoura = TextVectorization(max_tokens=100, output_sequence_length=10)

print("\n2. A IA esta lendo os textos e criando o dicionario de RGs...")
tesoura.adapt(chamados)

dicionario_da_ia = tesoura.get_vocabulary()
print("Dicionario criado:")
print(dicionario_da_ia)

print("\n3. Traduzindo o portugues para a linguagem matematica...")
chamados_em_numeros = tesoura(chamados)

print("Como a IA enxerga o Chamado 1 agora:")
print(chamados_em_numeros[0])

print("\n4. Padronizando o tamanho das caixas (Padding)...")


print("Como a IA enxerga o Chamado 1 padronizado:")
print(chamados_em_numeros[0])

print("Como a IA enxerga o Chamado 2 padronizado:")
print(chamados_em_numeros[1])