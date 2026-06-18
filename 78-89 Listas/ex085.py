"""
DESAFIO 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma única lista que mantenha separados os valores pares 
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

# Lista composta: num[0] para pares, num[1] para ímpares
num = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    
    # Classificação direta ao inserir
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)

# Ordenação interna das sublistas
num[0].sort()
num[1].sort()

# Exibição organizada
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')