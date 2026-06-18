"""
DESAFIO 086:
Crie um programa que declare uma matriz de dimensão 3x3 e preencha-a 
com valores lidos pelo teclado. No final, mostre a matriz na tela, 
com a formatação correta.
"""

# Inicializamos a matriz 3x3 com zeros (ou lista vazia)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Leitura da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

# Exibição da matriz formatada
for l in range(0, 3):
    for c in range(0, 3):
        # O :^5 centraliza o número em um espaço de 5 caracteres
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # Pula linha ao final de cada linha da matriz