"""
DESAFIO 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os 
em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# Leitura dos 4 valores de forma mais compacta usando tupla aninhada
# A função map() aplica o int() em cada entrada digitada
valores = tuple(int(input(f'Digite o {i+1}º valor: ')) for i in range(4))

print(f"\nVocê digitou os valores: {valores}")

# A) Contagem do valor 9
print(f"O valor 9 apareceu {valores.count(9)} vezes.")

# B) Posição do primeiro valor 3 (com tratamento de erro caso não exista)
if 3 in valores:
    print(f"O valor 3 apareceu na {valores.index(3) + 1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

# C) Números pares
print("Os valores pares digitados foram: ", end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
print() # Apenas para pular linha no final