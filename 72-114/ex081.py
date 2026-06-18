"""
DESAFIO 081:
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    
    # Validação robusta da resposta do usuário
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 30)

# A) Quantidade de números digitados
print(f'Você digitou {len(valores)} elementos.')

# B) Lista ordenada de forma decrescente
# Usamos reverse=True para ordenar do maior para o menor
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

# C) Verificação da existência do valor 5
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')