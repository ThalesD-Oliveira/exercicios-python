"""
DESAFIO 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente.
"""

numeros = list()

while True:
    # Captura a entrada do usuário
    n = int(input('Digite um valor: '))
    
    # Validação de duplicidade
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    # Pergunta se o usuário deseja continuar
    # Adicionamos .strip().upper() para garantir que 's' ou 'n' funcionem bem
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if continuar == 'N':
        break

print('-=' * 30)

# Ordenação da lista
numeros.sort()

print(f'Você digitou os valores {numeros}')