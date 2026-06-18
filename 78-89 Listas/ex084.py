"""
DESAFIO 084:
Faça um programa que leia nome e peso de várias pessoas, guardando tudo 
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    # Se for o primeiro cadastro, define maior e menor peso
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        # Atualiza os valores extremos conforme necessário
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
            
    princ.append(temp[:])  # Faz uma cópia da lista temp para a lista principal
    temp.clear()           # Limpa a lista temporária para o próximo cadastro
    
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')

# Exibição do maior peso
print(f'O maior peso foi de {mai}kg. Peso de: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()

# Exibição do menor peso
print(f'O menor peso foi de {men}kg. Peso de: ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()