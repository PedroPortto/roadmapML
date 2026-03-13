from neuron import Neuron

# Criando o neurônio (vamos usar pesos zerados para ver ele aprender do absoluto zero)
meuNeuronio = Neuron(pesoAtribuido=[0.0, 0.0], viesAtribuido=0.0)

entradaTeste = [1, 1] # Exemplo: Caiu a internet e acabou o toner
gabaritoTeste = 1     # O gabarito diz que é um chamado urgente!

print(f"Pesos ANTES de aprender: {meuNeuronio.pesos}")
print(f"Viés ANTES de aprender: {meuNeuronio.vies}")
print(f"Previsão ANTES: {meuNeuronio.forwardPass(entradaTeste):.4f}")

# Fazendo o neurônio aprender com esse exemplo UMA vez
meuNeuronio.treinar(entradaTeste, gabaritoTeste)

print("-" * 30)
print(f"Pesos DEPOIS de aprender: {meuNeuronio.pesos}")
print(f"Viés DEPOIS de aprender: {meuNeuronio.vies}")
print(f"Previsão DEPOIS: {meuNeuronio.forwardPass(entradaTeste):.4f}")