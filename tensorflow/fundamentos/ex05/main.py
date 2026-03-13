from neuron import Neuron

# Criando os detetives da Camada Oculta com os pesos perfeitos
neuronio_A = Neuron(pesoAtribuido=[20.0, 20.0], viesAtribuido=-10.0)
neuronio_B = Neuron(pesoAtribuido=[20.0, 20.0], viesAtribuido=-30.0)
neuronio_C = Neuron(pesoAtribuido=[0.0 , 10.0], viesAtribuido=-5)

# Criando o Chefe da Camada de Saída com os pesos perfeitos
# Note que o peso para o Detetive B é fortemente negativo (-40)
neuronio_Chefe = Neuron(pesoAtribuido=[20.0, -40.0, 5.0], viesAtribuido=-10.0)

# Testando o cenário onde TUDO caiu (Era para dar Normal, próximo de 0%)
chamado_apagao = [1, 1]

det1 = neuronio_A.forwardPass(chamado_apagao)
det2 = neuronio_B.forwardPass(chamado_apagao)
det3 = neuronio_C.forwardPass(chamado_apagao)
listaVeredito = [det1, det2, det3]

print(neuronio_Chefe.forwardPass(listaVeredito))