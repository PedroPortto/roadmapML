# A Missão
# Nós vamos expandir a sua classe Neuron.
# Pegue a sua classe Neuron que já está funcionando com o método forward_pass.
# Adicione um novo método chamado prever_lote(self, lista_de_eventos).
# Esse método vai receber uma matriz (uma lista de listas). Por exemplo:
# O seu método prever_lote deve usar um laço for para passar cada um desses eventos pelo método forward_pass que você já criou.
# Ele deve retornar uma nova lista contendo as probabilidades de cada evento ser um ataque.

from neuron import Neuron
# Instanciando o neurônio de segurança
neuronio_seguranca = Neuron(pesoAtribuido=[0.8, 3.5, 2.0], viesAtribuido=-4.0)

logs_de_rede = [
    [1, 0, 0],  # Evento A
    [6, 1, 1],  # Evento B
    [3, 0, 1]   # Evento C
]

# Processando o lote inteiro de uma vez
resultados = neuronio_seguranca.preverLote(logs_de_rede)

# Imprimindo os resultados
for i, prob in enumerate(resultados):
    print(f"Evento {i+1} - Probabilidade de Ataque: {prob * 100:.2f}%")