"""
DESAFIO 090:
Faça um programa que leia nome e média de um aluno, guardando também 
a situação em um dicionário. No final, mostre o conteúdo da estrutura 
na tela.
"""

# Criando o dicionário para armazenar os dados do aluno
aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

# Lógica para definir a situação (Aprovado ou Reprovado)
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' * 30)

# Exibição dos dados do dicionário
# Usamos o método .items() para percorrer chave e valor
for k, v in aluno.items():
    print(f'  - {k.capitalize()} é igual a {v}')