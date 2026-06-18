"""
DESAFIO 087:
Aprimore o desafio anterior (086), mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

# Inicializamos a matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

# Leitura e processamento da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

# Exibição da matriz e cálculos simultâneos
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        
        # A) Soma dos pares
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
            
        # B) Soma da terceira coluna (índice 2)
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
            
        # C) Maior valor da segunda linha (índice 1)
        if l == 1:
            if c == 0 or matriz[l][c] > maior_segunda_linha:
                maior_segunda_linha = matriz[l][c]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')