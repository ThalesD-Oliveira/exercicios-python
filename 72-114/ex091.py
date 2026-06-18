"""
DESAFIO 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário. No final, coloque esse dicionário 
em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

# Criando o dicionário com os resultados dos 4 jogadores
jogo = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}

ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

# Ordenando o dicionário: itemgetter(1) pega o valor (o número do dado) 
# e reverse=True coloca do maior para o menor.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 20)
print(' == RANKING DOS JOGADORES == ')

for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)