"""
DESAFIO 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as 
suas respectivas posições na lista.
"""

listanum = []

# Leitura dos 5 valores
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))

# Identificação dos valores extremos usando funções nativas
maior = max(listanum)
menor = min(listanum)

print('-=' * 30)
print(f'Você digitou os valores {listanum}')

# Exibição do maior valor e suas posições
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()

# Exibição do menor valor e suas posições
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()