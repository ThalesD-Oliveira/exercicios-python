"""
DESAFIO 103:
Faça um programa que tenha uma função chamada ficha(), que receba 
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.
"""

def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador de futebol com nome e número de gols.
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Programa Principal
n = str(input("Nome do Jogador: ")).strip()
g = str(input("Número de Gols: "))

# Validação: garante que, se o usuário não digitar um número, 
# o valor de gols seja tratado como 0.
if g.isnumeric():
    g = int(g)
else:
    g = 0

# Validação: se o nome estiver vazio, passamos apenas os gols para a função
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)