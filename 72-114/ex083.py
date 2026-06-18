"""
DESAFIO 083:
Crie um programa onde o usuário digite uma expressão qualquer que use 
parênteses. Seu aplicativo deverá analisar se a expressão passada está 
com os parênteses abertos e fechados na ordem correta.
"""

expr = input('Digite a expressão: ')

# Usamos uma lista como uma pilha (stack) para verificar a ordem
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        # Se a pilha não estiver vazia, removemos o '(' correspondente
        if len(pilha) > 0:
            pilha.pop()
        else:
            # Se tentarmos fechar um parêntese sem ter um aberto, é inválido
            pilha.append(')')
            break

# Se a pilha estiver vazia, todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')