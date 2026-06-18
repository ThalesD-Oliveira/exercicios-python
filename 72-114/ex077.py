"""
DESAFIO 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

# Tupla com as palavras conforme o desafio
palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

# Loop principal para percorrer cada palavra da tupla
for p in palavras:
    # Exibe a palavra formatada em maiúsculas
    print(f'\nNa palavra {p.upper():<12} temos ', end='')
    
    # Loop interno para analisar cada letra da palavra atual
    for letra in p:
        # Verifica se a letra é uma vogal
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# Pula uma linha final para organização
print()