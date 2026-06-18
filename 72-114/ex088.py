"""
DESAFIO 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

lista = []
jogos = []

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))

# Otimização: Usamos um laço para controlar o número de jogos
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        # Verifica se o número já está na lista para garantir números únicos
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    
    lista.sort()  # Ordena cada jogo para facilitar a leitura
    jogos.append(lista[:])  # Adiciona uma cópia da lista à lista de jogos
    lista.clear()  # Limpa a lista temporária
    tot += 1

print(f'-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)

# Exibição organizada com um pequeno atraso para dar suspense
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)