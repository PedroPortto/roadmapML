from neuron import Neuron

# Criando o neurônio (vamos usar pesos zerados para ver ele aprender do absoluto zero)
meuNeuronio = Neuron(pesoAtribuido=[0.0, 0.0], viesAtribuido=0.0)


baseDeDados = [
    [1, 0],  # Chamado 1
    [0, 1],  # Chamado 2
    [1, 1],  # Chamado 3
    [0, 0]   # Chamado 4
]

gabaritos = [1,0,1,0]     # O gabarito diz que é um chamado urgente!

# Fazendo o neurônio aprender com esse exemplo 1000 vezes
for epoca in range(1000):

    for i in range(len(gabaritos)):
        meuNeuronio.treinar(baseDeDados[i], gabaritos[i])

print("-" * 30)
print(f"Pesos DEPOIS de aprender: {meuNeuronio.pesos}")
print(f"Viés DEPOIS de aprender: {meuNeuronio.vies}")
for i in range(len(gabaritos)):
    print(f"Previsão DEPOIS: {meuNeuronio.forwardPass(baseDeDados[i]):.4f}")