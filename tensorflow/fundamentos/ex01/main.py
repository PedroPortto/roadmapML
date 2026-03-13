# Crie uma classe Python chamada Neuron.
# No construtor (__init__), inicialize dois atributos: uma lista de pesos (coloque os valores [10, 1]) e um vies (valor -5). 
# Se quiser, use o decorador @property para deixá-los protegidos.
# Crie um método chamado forward_pass(entradas) que receba uma lista de valores (ex: [1, 0]).
# Dentro desse método, faça a multiplicação e soma (como no produto escalar que você treinou na Álgebra). 
# Adicione o viés no final para encontrar o z.
# Use a biblioteca math (math.exp()) para calcular e retornar a probabilidade final do Sigmoide.


from neuron import Neuron

# Instanciando o neurônio com os pesos da Internet (10), Impressora (1) e Viés (-5)
meu_neuronio = Neuron(pesoAtribuido=[10, 1], viesAtribuido=-5)

# Testando um chamado onde a internet caiu (1) e a impressora está ok (0)
ticket_entrada = [1, 0]
probabilidade = meu_neuronio.forward_pass(ticket_entrada)

print(f"A probabilidade do chamado ser urgente é: {probabilidade * 100:.2f}%")