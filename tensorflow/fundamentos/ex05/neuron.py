import math

class Neuron:
    def __init__(self, pesoAtribuido, viesAtribuido):
        self._peso = pesoAtribuido
        self._vies = viesAtribuido
        
    @property
    def pesos(self):
        return self._peso
    
    @property
    def vies(self):
        return self._vies
    
    def forwardPass(self, entrada):
        soma = 0
        for x, w in zip(entrada, self._peso):
            soma += x * w
        
        somaVies = soma + self._vies
        return 1 / (1 + math.exp(- somaVies))
    
    def preverLote (self, listaDeEventos):
        listaFinal = []
        for x in listaDeEventos:
            listaFinal.append(self.forward_pass(x))

        return listaFinal
    
    def treinar(self, entrada, gabarito, taxaDeAprendizado = 0.1):
        previsao = self.forwardPass(entrada)
        erroSinal = previsao - gabarito
        self._vies -= (taxaDeAprendizado * erroSinal)

        for i in range(len(self._peso)):
            self._peso[i] -= taxaDeAprendizado * erroSinal * entrada[i]