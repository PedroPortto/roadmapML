# A Missão:
# Crie uma função chamada calcularErro(gabarito, previsao).
# Dentro dela, escreva a fórmula da Entropia Cruzada Binária.
# Lembre-se de importar o módulo math para usar math.log().
# Retorne o valor do erro calculado.

import math

def calcularErro(gabarito, palpite):
    return -(gabarito * math.log(palpite) + (1 - gabarito) * math.log(1 - palpite))

gabaritoReal = 1
palpiteBom = 0.99  # O neurônio tem quase certeza que é 1
palpiteRuim = 0.01 # O neurônio tem quase certeza que é 0

erro1 = calcularErro(gabaritoReal, palpiteBom)
erro2 = calcularErro(gabaritoReal, palpiteRuim)

print(f"Erro do palpite bom: {erro1}")
print(f"Erro do palpite ruim: {erro2}")