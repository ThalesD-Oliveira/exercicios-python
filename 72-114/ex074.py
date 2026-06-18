"""
DESAFIO 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o 
menor e o maior valor que estão na tupla.
"""

from random import randint

# Gerando a tupla com 5 números aleatórios entre 1 e 10
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))

# Melhoria: Usando o desempacotamento '*' para imprimir os números
# de forma rápida e limpa sem precisar de um laço 'for'.
print(f"Os valores sorteados foram: ", end='')
print(*numeros)

# Exibindo os resultados usando as funções built-in do Python
print(f"O maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")