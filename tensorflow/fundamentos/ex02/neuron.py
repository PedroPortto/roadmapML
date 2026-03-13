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
    
    def forward_pass(self, entrada):
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