import requests
import time # 1. Trazemos a biblioteca de tempo do Python

# 2. A URL inicial (Página 1)
url_atual = "https://pokeapi.co/api/v2/pokemon"
todos_pokemons = []
paginas_coletadas = 0

print("Iniciando a coleta profissional...\n")

# 3. O Loop Infinito (com limite de segurança de 3 páginas)
while url_atual and paginas_coletadas < 3:
    
    # Fazemos o pedido da página atual
    resposta = requests.get(url_atual)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # 4. Extraindo a lista de pokemons desta página
        resultados_da_pagina = dados['results']
        for pokemon in resultados_da_pagina:
            todos_pokemons.append(pokemon['name']) # Guardamos na nossa lista
            
        paginas_coletadas += 1
        print(f"Página {paginas_coletadas} coletada! (Total acumulado: {len(todos_pokemons)})")
        
        # 5. O Pulo do Gato: Pegando a URL da PRÓXIMA página
        url_atual = dados['next'] 
        
        # 6. Respirando para não tomar Rate Limit (Bloqueio)
        print("Garçom descansando por 1 segundo...")
        time.sleep(1) 
        
    else:
        print(f"Erro! O servidor nos bloqueou ou caiu. Status: {resposta.status_code}")
        break # Para o loop em caso de erro

print("\nColeta finalizada com sucesso!")
print(f"Nós capturamos {len(todos_pokemons)} Pokémon no total.")