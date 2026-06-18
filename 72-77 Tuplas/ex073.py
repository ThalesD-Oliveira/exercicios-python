"""
DESAFIO 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""

# Tupla com os times (mantida a ordem original da sua imagem)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

# Usamos uma linha separadora para facilitar a leitura no console
linha = '-=' * 20

print(f"\n{linha}")
print(f"Lista de times do Brasileirão: {times}")
print(linha)

# A) Os 5 primeiros (fatiamento de 0 até 4)
print(f"Os 5 primeiros são: {times[:5]}")
print(linha)

# B) Os 4 últimos (fatiamento usando índices negativos)
print(f"Os 4 últimos são: {times[-4:]}")
print(linha)

# C) Times em ordem alfabética
# Dica: sorted() retorna uma lista, o que é ótimo para visualização
print(f"Times em ordem alfabética: {sorted(times)}")
print(linha)

# D) Posição da Chapecoense
# Adicionamos um tratamento para caso o time não esteja na lista
time_busca = 'Chapecoense'
if time_busca in times:
    posicao = times.index(time_busca) + 1
    print(f"O {time_busca} está na {posicao}ª posição.")
else:
    print(f"O {time_busca} não está na lista.")
print(linha)