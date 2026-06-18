"""
DESAFIO 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde 
tudo em uma lista composta. No final, mostre um boletim contendo a média 
de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente.
"""

ficha = []

# 1. Entrada de Dados
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # Guardamos os dados em uma lista interna [nome, [n1, n2], media]
    ficha.append([nome, [nota1, nota2], media])
    
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

# 2. Exibição do Boletim (Cabeçalho)
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')

# 3. Consulta individual de notas
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        
print('<<< VOLTE SEMPRE >>>')