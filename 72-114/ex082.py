"""
DESAFIO 082:
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lista_completa = []
lista_pares = []
lista_impares = []

while True:
    # Coleta do dado
    num = int(input('Digite um valor: '))
    lista_completa.append(num)
    
    # Classificação imediata (Diligência na organização)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    
    # Validação da continuação
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 30)

# Exibição dos resultados
print(f'A lista completa é: {lista_completa}')
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de ímpares é: {lista_impares}')